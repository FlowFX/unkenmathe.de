"""Views for sheets app."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView  # , DeleteView, ListView

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


class SheetUpdateView(UserPassesTestMixin, UpdateView):
    """Update view for an exercise sheet."""

    model = Sheet
    form_class = SheetForm
    context_object_name = 'sheet'

    def test_func(self):
        """Test if user is staff or author."""
        obj = self.get_object()

        return self.request.user == obj.author or self.request.user.is_staff

    def get_form_kwargs(self):
        """Add user as keyword argument."""
        kwargs = super(SheetUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model.
        
        The redirect to the success url or return to the update view.
        """
        self.object = form.save()

        if 'continue' in self.request.POST:
            url = reverse('sheets:update', kwargs={'pk': self.object.pk})
            return redirect(url)
        
        return HttpResponseRedirect(self.get_success_url())
