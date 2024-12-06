from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Games type
GAME_TYPE = (("multiplayer", "Multiplayer"), ("single_player", "Single Player"))

GENRE_TYPE = (
    ("horror", "Horror"),
    ("action", "Action"),
    ("story_telling", "Story telling"),
)


class Review(models.Model):
    """Review model with proper CRUD functionality"""
    user = models.ForeignKey(
        User, 
        related_name="review_owner", 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    game_name = models.CharField(max_length=300)
    review = RichTextField(max_length=5000)  # Increased max length
    image = ResizedImageField(
        size=[800, None],  # Increased image size
        quality=85,
        upload_to="game/",
        force_format="WEBP",
    )
    image_alt = models.CharField(max_length=100)
    type_game = models.CharField(
        max_length=50, 
        choices=GAME_TYPE,
        default="single_player"
    )
    genre = models.CharField(
        max_length=50,
        choices=GENRE_TYPE,
        default="action"
    )
    developer = models.CharField(max_length=100)  # Increased max length
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_date']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    def get_absolute_url(self):
        return reverse('review_detail', kwargs={'pk': self.pk})

