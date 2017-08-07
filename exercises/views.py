"""Views for exercise app."""
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Exercise


class ExcerciseListView(ListView):
    """List all exercises."""

    model = Exercise
    context_object_name = 'exercises'
    template_name = 'exercises/exercise_list.html'


class ExerciseCreateView(CreateView):
    """Create view for a new exercise."""

    model = Exercise
    fields = ['text']
    success_url = reverse_lazy('index')
