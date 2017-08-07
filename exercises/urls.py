"""URL configuration for exercises app."""
from django.conf.urls import url

from .views import ExerciseCreateView


urlpatterns = [
    url(r'^new$', ExerciseCreateView.as_view(), name='create'),
]
