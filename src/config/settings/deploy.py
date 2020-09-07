from .base import *
import django_heroku
import os
import dj_database_url

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

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

MIDDLEWARE += "whitenoise.middleware.WhiteNoiseMiddleware"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")

django_heroku.settings(locals())
