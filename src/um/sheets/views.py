"""Views for sheets app."""
from django.contrib.auth.mixins import LoginRequiredMixin  # , UserPassesTestMixin
from django.views.generic import CreateView, DetailView  # , DeleteView, ListView, UpdateView

from .forms import SheetForm
from .models import Sheet


class SheetCreateView(LoginRequiredMixin, CreateView):
    """Create view for a new exercise sheet."""

    model = Sheet
    form_class = SheetForm
    context_object_name = 'sheet'

    def form_valid(self, form):
        """Add the current user as the author of the exercise sheet."""
        self.object = form.save(commit=False)
        self.object.author = self.get_form_kwargs()['user']
        self.object.save()

        return super(SheetCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        """Add user as keyword argument."""
        kwargs = super(SheetCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs


class SheetDetailView(DetailView):
    """Detail view for an exercise."""

    model = Sheet
    context_object_name = 'sheet'

    def get_context_data(self, **kwargs):
        """Add data to the template context."""
        context = super(SheetDetailView, self).get_context_data(**kwargs)

        # Determine whether or not the user gets shown the edit and delete buttons
        obj = self.get_object()
        user = self.request.user
        context['can_edit'] = True if user == obj.author or user.is_staff else False

        return context