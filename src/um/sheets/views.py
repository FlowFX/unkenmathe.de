"""Views for sheets app."""
from django.contrib.auth.mixins import LoginRequiredMixin  # , UserPassesTestMixin
from django.views.generic import CreateView  # , DeleteView, DetailView, ListView, UpdateView

from .forms import SheetForm
from .models import Sheet


class SheetCreateView(LoginRequiredMixin, CreateView):
    """Create view for a new exercise sheet."""

    model = Sheet
    form_class = SheetForm
    # success_url = reverse_lazy('index')
    context_object_name = 'sheet'
