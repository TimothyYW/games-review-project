from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
from allauth.account.models import EmailConfirmation, EmailAddress
from datetime import timedelta


class Command(BaseCommand):
    help = 'Cleanup expired email confirmations and unused email addresses'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=3,
            help='Number of days after which to remove expired tokens'
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Calculate cutoff date
                days = options['days']
                cutoff_date = timezone.now() - timedelta(days=days)

                # Delete expired email confirmations
                expired_tokens = EmailConfirmation.objects.filter(
                    created__lt=cutoff_date
                )
                count = expired_tokens.count()
                expired_tokens.delete()

                # Delete unverified email addresses older than cutoff
                unverified_emails = EmailAddress.objects.filter(
                    verified=False,
                    user__date_joined__lt=cutoff_date
                )
                unverified_count = unverified_emails.count()
                unverified_emails.delete()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully deleted {count} expired tokens and '
                        f'{unverified_count} unverified email addresses'
                    )
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f'Error during cleanup: {str(e)}'
                )
            ) 