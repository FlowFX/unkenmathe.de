"""Django configuration for testing and CI environments."""
from .common import *

# Use in-memory file storage
DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Speed! 
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}
