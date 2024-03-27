from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class Reviewform(forms.ModelForm):
    """ Form to leave the review """
    class Meta:
        model = Review
        fields = ['game_name', 'review', 'image', 'image_alt', 'type_game', 'genre', 'developer']

        review = forms.CharField(widget=RichTextWidget())
        
        widgets = {
            'review': forms.Textarea(attrs={'rows': 5}),
        }

        labels = {
            'user': 'Username',
            'review': 'Review',
            'image': 'Game picture',
            'image_alt': 'Describ image',
            'type_game': 'Type game',
            'genre': 'Genre',
            'developer': 'Developer'
        }