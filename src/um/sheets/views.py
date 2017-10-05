"""Views for sheets app."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView  # , DeleteView, ListView

from .forms import SheetForm
from .models import Sheet

from ..core.views import SaveAndContinueMixin, UserFormKwargsMixin, UserCanEditMixin, TestFuncMixin


class SheetCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    """Create view for a new exercise sheet."""

    model = Sheet
    form_class = SheetForm
    context_object_name = 'sheet'

    def form_valid(self, form):
        """Add the current user as the author of object."""
        self.object = form.save(commit=False)
        self.object.author = self.get_form_kwargs()['user']
        self.object.save()

        return super(SheetCreateView, self).form_valid(form)


class SheetDetailView(UserCanEditMixin, DetailView):
    """Detail view for an exercise."""

    model = Sheet
    context_object_name = 'sheet'


class SheetUpdateView(TestFuncMixin, UserPassesTestMixin, SaveAndContinueMixin, UserFormKwargsMixin, UpdateView):
    """Update view for an exercise sheet."""

    model = Sheet
    form_class = SheetForm
    context_object_name = 'sheet'

    def get_update_url(self):
        return reverse('sheets:update', kwargs={'pk': self.object.pk})
