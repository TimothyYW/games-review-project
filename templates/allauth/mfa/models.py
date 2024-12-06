from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AuthenticatorManager(models.Manager):
    def delete_dangling_recovery_codes(self, user):
        """Delete recovery codes if they're the only authenticator left."""
        with self.model._default_manager.select_for_update().filter(user=user) as qs:
            deleted_authenticator = None
            if not qs.exclude(type=self.model.Type.RECOVERY_CODES).exists():
                deleted_authenticator = qs.first()
                qs.delete()
            return deleted_authenticator


class Authenticator(models.Model):
    class Type(models.TextChoices):
        RECOVERY_CODES = "recovery_codes", _("Recovery codes")
        TOTP = "totp", _("TOTP Authenticator")

    objects = AuthenticatorManager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="mfa_authenticators"
    )
    type = models.CharField(
        max_length=20, 
        choices=Type.choices,
        db_index=True
    )
    data = models.JSONField(help_text=_("Encrypted authenticator data"))
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True
    )
    last_used_at = models.DateTimeField(
        null=True,
        db_index=True
    )

    class Meta:
        unique_together = (("user", "type"),)
        indexes = [
            models.Index(fields=['user', 'type']),
            models.Index(fields=['type', 'created_at']),
        ]
        verbose_name = _("MFA Authenticator")
        verbose_name_plural = _("MFA Authenticators")

    def __str__(self):
        return f"{self.get_type_display()} - {self.user}"

    def wrap(self):
        """Get the appropriate authenticator wrapper class."""
        from allauth.mfa.recovery_codes import RecoveryCodes
        from allauth.mfa.totp import TOTP

        wrapper_map = {
            self.Type.TOTP: TOTP,
            self.Type.RECOVERY_CODES: RecoveryCodes,
        }
        return wrapper_map[self.type](self)

    def record_usage(self):
        """Record when this authenticator was last used."""
        self.last_used_at = timezone.now()
        self.save(update_fields=["last_used_at"])
