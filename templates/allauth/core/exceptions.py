from typing import Union
from django.http import HttpResponse


class ImmediateHttpResponse(Exception):
    """
    Exception for immediate HTTP responses.
    
    This exception is used to interrupt the flow of processing to immediately
    return a custom HttpResponse.
    """

    def __init__(self, response: Union[HttpResponse, str]):
        """
        Initialize the exception.
        
        Args:
            response: Either an HttpResponse object or a string message
        """
        if isinstance(response, str):
            from django.http import HttpResponse
            response = HttpResponse(response)
        
        self.response = response
        super().__init__(str(response))
