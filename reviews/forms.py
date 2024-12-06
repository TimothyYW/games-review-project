from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form to create and edit reviews"""

    class Meta:
        model = Review
        fields = [
            "title",
            "game_name",
            "review",
            "image",
            "image_alt",
            "type_game",
            "genre",
            "developer",
        ]

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "game_name": forms.TextInput(attrs={'class': 'form-control'}),
            "review": RichTextWidget(),
            "image_alt": forms.TextInput(attrs={'class': 'form-control'}),
            "developer": forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Review Title",
            "game_name": "Game Name",
            "review": "Your Review",
            "image": "Game Picture",
            "image_alt": "Image Description",
            "type_game": "Game Type",
            "genre": "Genre",
            "developer": "Developer",
        }

    def clean_image(self):
        """Validate image size"""
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError("Image file too large ( > 2MB )")
        return image
