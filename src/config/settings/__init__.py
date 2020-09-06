import os

# DJANGO_SETTINGS_MODULE 환경변수가 지정되지 않거나 config.settings인 경우
SETTINGS_MODULE = os.environ.get("DJANGO_SETTINGS_MODULE")
if not SETTINGS_MODULE or SETTINGS_MODULE == "config.settings":
    from .deploy import *
