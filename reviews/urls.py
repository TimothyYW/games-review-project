from django.urls import path
from .views import InputReview


urlpatterns = [
    path('', InputReview.as_view(), name='input_review'),
    
]