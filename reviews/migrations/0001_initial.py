# Generated by Django 4.2.11 on 2024-03-20 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_name", models.CharField(max_length=300)),
                ("review", djrichtextfield.models.RichTextField(max_length=500)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=80,
                        scale=None,
                        size=[400, None],
                        upload_to="game/",
                    ),
                ),
                ("image_alt", models.CharField(max_length=100)),
                (
                    "type_game",
                    models.CharField(
                        choices=[
                            ("fps", "FPS"),
                            ("third_person_shooter", "Third Person Shooter"),
                            ("rpg", "RPG"),
                        ],
                        default="games",
                        max_length=50,
                    ),
                ),
                ("developer", models.CharField(max_length=20)),
                ("posted", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
