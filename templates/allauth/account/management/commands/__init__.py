"""
Management commands for the allauth.account app.
"""

from .cleanup_auth_tokens import Command as CleanupAuthTokensCommand

__all__ = ['CleanupAuthTokensCommand']
