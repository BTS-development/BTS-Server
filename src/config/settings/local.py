from .base import *

DEBUG = True
WSGI_APPLICATION = "config.wsgi.application"
ALLOWED_HOSTS += "*"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
