from django.urls import path
from .views import InputReview, Reviews, DeleteReview, EditReview, ReviewDetail


urlpatterns = [
    path("", InputReview.as_view(), name="input_review"),
    path("reviews/", Reviews.as_view(), name="reviews"),
    path("delete/<slug:pk>/", DeleteReview.as_view(), name="delete_review"),
    path("edit/<slug:pk>/", EditReview.as_view(), name="edit_review"),
    path("<slug:pk>", ReviewDetail,as_view(), name="review_detail"),
]
