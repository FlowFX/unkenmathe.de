"""Views for exercise app."""
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ExerciseForm
from .models import Exercise


class ExcerciseListView(ListView):
    """List all exercises."""

    model = Exercise
    context_object_name = 'exercises'
    template_name = 'exercises/exercise_list.html'


class ExerciseCreateView(CreateView):
    """Create view for a new exercise."""

    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('index')
    context_object_name = 'exercise'


class ExerciseUpdateView(UpdateView):
    """Update view for an exercise."""

    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('index')
    context_object_name = 'exercise'


class ExerciseDetailView(DetailView):
    """Detail view for an exercise."""

    model = Exercise
    success_url = reverse_lazy('index')
    context_object_name = 'exercise'
