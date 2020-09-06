from .base import *
import django_heroku
import os

DEBUG = False
WSGI_APPLICATION = "config.wsgi.application"
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".herokuapp.com",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

MIDDLEWARE += "whitenoise.middleware.WhiteNoiseMiddleware"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")

django_heroku.settings(locals())
