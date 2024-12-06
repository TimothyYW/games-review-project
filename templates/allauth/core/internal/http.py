import json
from typing import Dict, Any

from django import shortcuts
from django.http import QueryDict, HttpRequest, HttpResponse
from django.urls import NoReverseMatch
from django.core.serializers.json import DjangoJSONEncoder


def serialize_request(request: HttpRequest) -> str:
    """
    Serialize a request object to JSON string.
    
    Args:
        request: The HttpRequest object to serialize
        
    Returns:
        str: JSON serialized request data
    """
    serializable_meta = {
        k: v for k, v in request.META.items() 
        if isinstance(v, (str, int, float, bool, list, dict))
    }
    
    return json.dumps({
        'path': request.path,
        'path_info': request.path_info,
        'META': serializable_meta,
        'GET': request.GET.urlencode(),
        'POST': request.POST.urlencode(),
        'method': request.method,
    }, cls=DjangoJSONEncoder)


def deserialize_request(serialized_data: str, request: HttpRequest) -> HttpRequest:
    """
    Deserialize JSON data back into a request object.
    
    Args:
        serialized_data: JSON string containing request data
        request: Base request object to populate
        
    Returns:
        HttpRequest: The populated request object
    """
    try:
        data = json.loads(serialized_data)
        request.GET = QueryDict(data['GET'])
        request.POST = QueryDict(data['POST'])
        request.META = data['META']
        request.path = data['path']
        request.path_info = data['path_info']
        request.method = data['method']
        return request
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Invalid request data format: {e}")


def redirect(to: str) -> HttpResponse:
    """
    Safe redirect that handles both URL names and direct paths.
    
    Args:
        to: URL name or path to redirect to
        
    Returns:
        HttpResponse: Redirect response
    """
    try:
        return shortcuts.redirect(to)
    except NoReverseMatch:
        return shortcuts.redirect(f"/{to}")
