"""Core views."""
from django.views.generic import RedirectView


favicon_view = RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=True)
