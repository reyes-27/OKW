from .base import BASE_DIR
import os

MEDIA_ROOT = os.path.join(BASE_DIR / "media")
MEDIA_URL = "/media/"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}