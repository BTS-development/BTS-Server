from .base import *
import os
import json

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = True
WSGI_APPLICATION = "config.wsgi.application"
ALLOWED_HOSTS += "*"

DATABASES = config_secret_deploy["django"]["databases"]

