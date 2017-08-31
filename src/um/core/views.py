"""Core views."""
from django.views.generic import RedirectView, TemplateView


favicon_view = RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=False)

robots_txt_view = TemplateView.as_view(template_name='robots.txt', content_type='text/plain')
