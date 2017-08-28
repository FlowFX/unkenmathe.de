"""Views for exercise app."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    """Create view for a new exercise."""

    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('index')
    context_object_name = 'exercise'

    def form_valid(self, form):
        """Add the current user as the original author of the exercise."""
        self.object = form.save(commit=False)
        self.object.author = self.get_form_kwargs()['user']
        self.object.save()

        return super(ExerciseCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        """Add user as keyword argument."""
        kwargs = super(ExerciseCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ExerciseUpdateView(UserPassesTestMixin, UpdateView):
    """Update view for an exercise."""

    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('index')
    context_object_name = 'exercise'

    def test_func(self):
        obj = self.get_object()

        return self.request.user == obj.author or self.request.user.is_staff


class ExerciseDetailView(DetailView):
    """Detail view for an exercise."""

    model = Exercise
    success_url = reverse_lazy('index')
    context_object_name = 'exercise'
