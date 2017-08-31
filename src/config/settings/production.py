"""Django configuration for production environment."""
from .common import *

# Core Settings
ALLOWED_HOSTS = ['www.unkenmathe.de']

# Security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = False  # could be True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True  # Force HTTPS

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 3600*24  # 24 hours

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

# Configure location of static files
STATIC_ROOT = os.path.abspath('/var/www/static/unkenmathe.de')
MEDIA_ROOT = os.path.abspath('/var/www/media/unkenmathe.de')

# Cache
CACHES = {
    'default': {  # Redislabs
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': get_secret('REDIS_LOCATION'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': get_secret('REDIS_PASSWORD'),
        }
    },
}

# Use Rollbar in production
# MIDDLEWARE += 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
# LOGGING['loggers']['']['handlers'].append('rollbar')
