from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "game_name",
        "image",
        "developer",
        "type_game",
        "genre",
        "review",
    )
