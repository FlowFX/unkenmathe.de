"""Django configuration for production environment."""
from .common import *

# Core Settings
ALLOWED_HOSTS = ['.unkenmathe.de']

# Configure location of static files
STATIC_ROOT = os.path.abspath('/var/www/static/unkenmathe.de')
MEDIA_ROOT = os.path.abspath('/var/www/media/unkenmathe.de')