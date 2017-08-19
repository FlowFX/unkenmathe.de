"""Views for exercise app."""

import os
import tempfile
from subprocess import PIPE, Popen

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ExerciseForm
from .models import Exercise

from ..core.jinja2 import jinja2_latex_env

from django.http import HttpResponse


def exercise_pdf_view(request, pk):
    """Return PDF version of the single exercise."""
    obj = Exercise.objects.get(pk=pk)

    if not obj.text_tex:  # pragma: no
        obj.render_tex()

    # Create PDF
    env = jinja2_latex_env
    template = env.get_template('exercise_detail.j2.tex')
    context = {'exercise': obj, }

    rendered_template = template.render(context)

    encoded_template = rendered_template.encode('utf-8')

    with tempfile.TemporaryDirectory() as tempdir:
        for _ in range(2):  # noqa: F402
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(encoded_template)

        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:

            # Return PDF
            response = HttpResponse(content=f.read())
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
