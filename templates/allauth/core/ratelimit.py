import hashlib
import time
from collections import namedtuple
from typing import List, Optional, Tuple

from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


Rate = namedtuple("Rate", "amount duration per")

DURATION_UNITS = {
    's': 1,        # seconds
    'm': 60,       # minutes
    'h': 3600,     # hours
    'd': 86400,    # days
}


def _parse_duration(duration: str) -> float:
    """Parse duration string into seconds."""
    if not duration:
        raise ValueError("Empty duration")
    
    unit = duration[-1]
    if unit not in DURATION_UNITS:
        raise ValueError(f"Invalid duration unit: {unit}")
    
    try:
        value = float(duration[:-1]) if len(duration) > 1 else 1
        return value * DURATION_UNITS[unit]
    except ValueError:
        raise ValueError(f"Invalid duration value: {duration[:-1]}")


def _parse_rate(rate: str) -> Rate:
    """Parse single rate string into Rate object."""
    parts = rate.split('/')
    if len(parts) not in (2, 3):
        raise ValueError(f"Invalid rate format: {rate}")
    
    amount = int(parts[0])
    duration = _parse_duration(parts[1])
    per = parts[2] if len(parts) == 3 else "ip"
    
    if per not in ("ip", "user", "key"):
        raise ValueError(f"Invalid rate target: {per}")
    
    return Rate(amount, duration, per)


def _parse_rates(rates: Optional[str]) -> List[Rate]:
    """Parse multiple rates string into list of Rate objects."""
    if not rates:
        return []
    return [_parse_rate(r.strip()) for r in rates.split(',') if r.strip()]


def _get_rate_source(request: HttpRequest, rate: Rate, key: Optional[str] = None,
                    user: Optional['User'] = None) -> Tuple[str, str]:
    """Get rate limiting source identifier."""
    from allauth.account.adapter import get_adapter
    
    if rate.per == "ip":
        return "ip", get_adapter().get_client_ip(request)
    elif rate.per == "user":
        if not user and not request.user.is_authenticated:
            raise ImproperlyConfigured("Rate limit per user requires authentication")
        return "user", str((user or request.user).pk)
    elif rate.per == "key":
        if not key:
            raise ImproperlyConfigured("Rate limit per key requires a key")
        return "key", hashlib.sha256(key.encode("utf8")).hexdigest()
    
    raise ValueError(f"Invalid rate target: {rate.per}")


def _cache_key(request, *, action, rate, key=None, user=None):
    from allauth.account.adapter import get_adapter

    if rate.per == "ip":
        source = ("ip", get_adapter().get_client_ip(request))
    elif rate.per == "user":
        if user is None:
            if not request.user.is_authenticated:
                raise ImproperlyConfigured(
                    "ratelimit configured per user but used anonymously"
                )
            user = request.user
        source = ("user", str(user.pk))
    elif rate.per == "key":
        if key is None:
            raise ImproperlyConfigured(
                "ratelimit configured per key but no key specified"
            )
        key_hash = hashlib.sha256(key.encode("utf8")).hexdigest()
        source = (key_hash,)
    else:
        raise ValueError(rate.per)
    keys = ["allauth", "rl", action, *source]
    return ":".join(keys)


def clear(request, *, action, key=None, user=None):
    from allauth.account import app_settings

    rates = _parse_rates(app_settings.RATE_LIMITS.get(action))
    for rate in rates:
        cache_key = _cache_key(request, action=action, rate=rate, key=key, user=user)
        cache.delete(cache_key)


def consume(request, *, action, key=None, user=None):
    from allauth.account import app_settings

    if not request or request.method == "GET":
        return True

    rates = _parse_rates(app_settings.RATE_LIMITS.get(action))
    if not rates:
        return True

    allowed = True
    for rate in rates:
        if not _consume_rate(request, action=action, rate=rate, key=key, user=user):
            allowed = False
    return allowed


def _consume_rate(request, *, action, rate, key=None, user=None):
    """
    Consume a rate limit attempt with improved caching.
    Uses Redis pipeline if available for atomic operations.
    """
    cache_key = _cache_key(request, action=action, rate=rate, key=key, user=user)
    
    try:
        # Try to use Redis pipeline for atomic operations
        if hasattr(cache, 'pipeline'):
            with cache.pipeline() as pipe:
                pipe.multi()
                history = pipe.get(cache_key) or []
                now = time.time()
                
                # Clean old entries
                history = [t for t in history if t > (now - rate.duration)]
                
                if len(history) < rate.amount:
                    history.insert(0, now)
                    pipe.set(cache_key, history, rate.duration)
                    allowed = True
                else:
                    allowed = False
                
                pipe.execute()
                return allowed
    except AttributeError:
        # Fall back to regular cache if Redis isn't available
        history = cache.get(cache_key, [])
        now = time.time()
        history = [t for t in history if t > (now - rate.duration)]
        
        allowed = len(history) < rate.amount
        if allowed:
            history.insert(0, now)
            cache.set(cache_key, history, rate.duration)
        
        return allowed


def consume_or_429(request, *args, **kwargs):
    from allauth.account import app_settings

    if not consume(request, *args, **kwargs):
        return render(request, "429." + app_settings.TEMPLATE_EXTENSION, status=429)
