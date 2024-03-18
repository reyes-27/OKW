from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE
import os


INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = [
    "127.0.0.1",
]

MEDIA_ROOT = os.path.join(BASE_DIR / "media")
MEDIA_URL = "/media/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}