from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichtextField
from django_resized import ResizedImageField

class Review(models.Model):
    """
    A model to add and manage reviews
    """
    user = models.ForgenKey(User, related_name='review_owner', on_delete=models.CASCADE)
    game_name = models.CharField(max_length=300, null=False, blank=False)
    review = RichtextField(max_length=500, null=False, blank=False)
    image = ResizedImageField(
        size = [400, None], quality=80, upload_to='game/', force_format='WEBP',
        blank=False, null=False
    )
image_alt = models.CharField(max_length=100, null=False, blank=False)
type_game = modelsCharField(max_length=50, null=False, blank=False)