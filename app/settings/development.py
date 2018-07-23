from os import path
from .base import *


DEBUG = True
ALLOWED_HOSTS = ["*"]
LIVE_RELOAD = config('LIVE_RELOAD', default=None)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(BASE_DIR, 'db.sqlite3'),
    }
}