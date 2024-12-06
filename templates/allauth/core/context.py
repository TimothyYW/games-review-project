from contextlib import contextmanager
from contextvars import ContextVar
from typing import Optional, Any
from django.http import HttpRequest


_request_var: ContextVar[Optional[HttpRequest]] = ContextVar("request", default=None)


def get_request() -> Optional[HttpRequest]:
    """
    Get the current request from context.
    
    Returns:
        Optional[HttpRequest]: The current request or None if not set
    """
    return _request_var.get()


def __getattr__(name: str) -> Any:
    """
    Attribute getter for backward compatibility.
    
    Args:
        name: Attribute name to get
        
    Returns:
        Any: The requested attribute
        
    Raises:
        AttributeError: If attribute doesn't exist
    """
    if name == "request":
        return get_request()
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


@contextmanager
def request_context(request: HttpRequest):
    """
    Context manager for request scope.
    
    Args:
        request: The request to set in context
    """
    token = _request_var.set(request)
    try:
        yield
    finally:
        _request_var.reset(token)
