"""Django configuration for production environment."""
from .common import *

# Core Settings
ALLOWED_HOSTS = ['.unkenmathe.de']

# Security
SECURE_SSL_REDIRECT = True

# Configure location of static files
STATIC_ROOT = os.path.abspath('/var/www/static/unkenmathe.de')
MEDIA_ROOT = os.path.abspath('/var/www/media/unkenmathe.de')

# Use Rollbar in production
MIDDLEWARE += 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
# LOGGING['loggers']['']['handlers'].append('rollbar')
