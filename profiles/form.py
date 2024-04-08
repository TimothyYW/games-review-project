from django import forms
from .models import Profile


class Profileform(form.Modalform):
    """Form to create a profile"""
    class Meta:
        modal = Profile
        fields = ["image", "bio"]

        labels = {
            "image": "Avatar",
            "bio": "Bio",
        }