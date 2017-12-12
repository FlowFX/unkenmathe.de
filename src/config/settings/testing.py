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
        'NAME': ':memory:',
        'TEST': {}
    }
}

env = get_secret("ENVIRONMENT")

import sys

if os.path.isdir('/Volumes/RAMDisk') and not env == 'ci' and not 'create-db' in sys.argv:
    # and this allows you to use --reuse-db to skip re-creating the db,
    # even faster!
    DATABASES['default']['TEST']['NAME'] = '/Volumes/RAMDisk/unkenmathe.test.db.sqlite3'
