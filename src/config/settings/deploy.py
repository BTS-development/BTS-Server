from .base import *

DEBUG = False
WSGI_APPLICATION = "config.wsgi.application"
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "bts-server.eba-mykyf6m2.us-east-1.elasticbeanstalk.com",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
