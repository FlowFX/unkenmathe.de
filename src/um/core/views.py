"""Core views."""
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView


favicon_view = RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=False)

robots_txt_view = TemplateView.as_view(template_name='robots.txt', content_type='text/plain')


class IndexView(TemplateView):
    """The home page."""

    template_name = 'index.html'


class UserCanEditMixin(object):

    def get_context_data(self, **kwargs):
        """Add data to the template context."""
        context = super(UserCanEditMixin, self).get_context_data(**kwargs)

        # Determine whether or not the user gets shown the edit and delete buttons
        obj = self.get_object()
        user = self.request.user
        context['can_edit'] = True if user == obj.author or user.is_staff else False

        return context


class SaveAndContinueMixin(object):

    def form_valid(self, form):
        """If the form is valid, save the associated model.
        
        The redirect to the success url or return to the update view.
        """
        self.object = form.save()

        if 'continue' in self.request.POST:
            return HttpResponseRedirect(self.get_update_url())
        
        return HttpResponseRedirect(self.get_success_url())


class UserFormKwargsMixin(object):

    def get_form_kwargs(self):
        """Add user as keyword argument."""
        kwargs = super(UserFormKwargsMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs


class TestFuncMixin(object):

    def test_func(self):
        """Test if user is staff or author."""
        obj = self.get_object()

        return self.request.user == obj.author or self.request.user.is_staff
