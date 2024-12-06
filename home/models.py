from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='reviews/')
    # Add other fields as necessary

    def __str__(self):
        return self.title
