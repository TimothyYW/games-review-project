from django import forms
from .models import Profile

class ProfileForm(form.ModelForm):
    """ Form to create a profile """
    class Meta:
        model = Profile
        fields = ["image", "bio"]

        labels = {
            "image": "Avatar",
            "bio": "Bio"
        }