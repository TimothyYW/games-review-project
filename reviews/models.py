from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Games type
GAME_TYPE = (
    ('multiplayer', 'Multiplayer'),
    ('single_player', 'Single Plyer')
)

GENRE_TYPE = (
    ('horror', 'Horror'),
    ('action', 'Action'),
    ('story_telling', 'Story telling'),
)

class Review(models.Model):
    """
    A model to add and manage reviews
    """
    user = models.ForeignKey(User, related_name='review_owner', on_delete=models.CASCADE)
    game_name = models.CharField(max_length=300, null=False, blank=False)
    review = RichTextField(max_length=500, null=False, blank=False)
    image = ResizedImageField(
        size = [400, None], quality=80, upload_to='game/', force_format='WEBP',
        blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    type_game = models.CharField(max_length=50, choices=GAME_TYPE, default="Single Player")
    genre = models.CharField(max_length = 50, choices=GENRE_TYPE, default="Games")
    developer = models.CharField(max_length=20, null=False, blank=False)
    posted = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['posted_date']

def __str__(self):
    return str(self.title)