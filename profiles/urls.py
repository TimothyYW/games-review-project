from django.urls import path
from .views import Profiles

urlpatterns = [
    path('user/<slug:pks', Profiles.as_view(), name="profile"),
]