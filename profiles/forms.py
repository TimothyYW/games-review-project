from django import forms
from .models import Profile
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):
    """ Form to create and edit a profile """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
        # Custom styling for image field
        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file',
            'accept': 'image/*'
        })

    def clean_image(self):
        """Validate image size and format"""
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 2 * 1024 * 1024:  # 2MB limit
                raise ValidationError("Image file too large ( > 2MB )")
            return image
        return None

    class Meta:
        model = Profile
        fields = ["image", "bio"]
        labels = {
            "image": "Avatar",
            "bio": "Bio"
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }