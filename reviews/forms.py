from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review
from .forms import Reviewform

class Reviewform (forms.ModelForm):
    """ Form to leave the review """
    class Meta:
        model = Review
        form_class = Reviewform
        field = ['user', 'game_name', 'review', 'image', 'image_alt', 'type_game', 'genre', 'developer']

        review = form.CharField(Widget=RichTextWidget())
        
        widgets = {
            'review': form.TextArea(attrs={'rows': 5}),
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