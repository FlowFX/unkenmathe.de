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
ALLOWED_HOSTS = []
DEBUG = False
ROOT_URLCONF = 'config.urls'
SECRET_KEY = get_secret('DJANGO_SECRET_KEY'),


# Apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django_extensions',
    'crispy_forms',
    'webpack_loader',
    'um.exercises',
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
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
            ],
        },
    },
]


# Static files
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))


# Webpack Loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}


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
