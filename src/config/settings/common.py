import os

import json

# Never import from Django directly into settings. Except this.
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# JSON-based secrets module (cf. Two Scoops of Django)
try:
    with open(os.path.join(BASE_DIR, 'secrets.json')) as f:
        secrets = json.loads(f.read())
except FileNotFoundError:
    error_msg = 'secrets.json file is missing.'
    raise ImproperlyConfigured(error_msg)


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        # Return either environment variable or setting from secrets module
        value = os.environ.get(setting)
        if value is None:
            value = secrets[setting]
        return value
    except KeyError:
        error_msg = f'Set the {setting} environment variable!'
        raise ImproperlyConfigured(error_msg)


# Core
DEBUG = False
SECRET_KEY = get_secret('DJANGO_SECRET_KEY'),

ALLOWED_HOSTS = []
APPEND_SLASH = True
ROOT_URLCONF = 'config.urls'
SITE_ID = 1


# Apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'authtools',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'compressor',
    'crispy_forms',
    'webpack_loader',
    'um.core',
    'um.exercises',
    'um.sheets',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': get_secret('DB_HOST'),
        'PORT': get_secret('DB_PORT'),
    }
}


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'um/templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'um.core.context_processors.rollbar_environment',
            ],
        },
    },
]


# User authentication
AUTH_USER_MODEL = 'authtools.User'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'index'


# https://django-allauth.readthedocs.io/en/latest/configuration.html
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Sessions https://docs.djangoproject.com/en/1.11/topics/http/sessions/
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 1209600  # (2 weeks, in seconds)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


# Static files
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}


# Webpack Loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}


# Compressor
COMPRESS_ENABLED = True
COMPRESS_CACHE_BACKEND = 'default'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]


# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Error tracking
ROLLBAR = {
    'access_token': get_secret("ROLLBAR_ACCESS_TOKEN"),
    'environment': get_secret("ENVIRONMENT"),
    'branch': 'master',
    'root': BASE_DIR,
}


# Logging
# cf. https://www.miximum.fr/blog/an-effective-logging-strategy-with-django/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        # Send all messages to console
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'rollbar': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'access_token': ROLLBAR['access_token'],
            'environment': ROLLBAR['environment'],
            'class': 'rollbar.logger.RollbarHandler'
        },
    },
    'loggers': {
        # This is the "catch all" logger
        '': {
            'handlers': ['console'],
            'level': DEBUG,
            'propagate': False,
        },
    }
}
