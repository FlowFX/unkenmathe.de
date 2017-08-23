"""Views for exercise app."""
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ExerciseForm
from .models import Exercise

from ..core.jinja2 import jinja2_latex_env
from ..core.utils import pdflatex

from django.http import HttpResponse


def exercise_pdf_view(request, pk):
    """Return PDF version of the single exercise."""
    obj = Exercise.objects.get(pk=pk)

    if not obj.text_tex:  # pragma: no cover
        obj.render_tex()

    # Prepare LaTeX template
    env = jinja2_latex_env
    template = env.get_template('exercise_detail.j2.tex')
    context = {'exercise': obj, }

    rendered_template = template.render(context)

    # Generate PDF from template
    pdf = pdflatex(rendered_template)

    # HTTP response
    response = HttpResponse(content=pdf)
    response['Content-Type'] = 'application/pdf'

    filename = 'exercise.pdf'
    response['Content-Disposition'] = f'inline; filename={filename}'

    return response


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
