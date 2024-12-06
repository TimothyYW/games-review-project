from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountConfig(AppConfig):
    name = 'allauth.account'
    verbose_name = _("Accounts")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # Import signal handlers
        from . import signals

        # Register any app-specific checks
        from django.core.checks import register, Tags
        from .checks import check_site_id
        register(check_site_id, Tags.security)
