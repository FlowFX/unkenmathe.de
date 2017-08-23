"""Custom context processors."""
from django.conf import settings  # import the settings file


def rollbar_environment(request):
    """Return a dict with the current environment."""
    return {'ROLLBAR_ENVIRONMENT': settings.ROLLBAR.get('environment')}
