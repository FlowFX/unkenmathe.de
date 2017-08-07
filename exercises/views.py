"""Views for exercise app."""
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Exercise


class ExerciseCreateView(CreateView):
    """Create view for a new exercise."""

    model = Exercise
    fields = ['text']
    success_url = reverse_lazy('index')
