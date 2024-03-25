from django.urls import path
from .views import InputReview, Reviews


urlpatterns = [
    path('', InputReview.as_view(), name='input_review'),
    path('reviews/',Reviews.as_view(), name='reviews'), 
]