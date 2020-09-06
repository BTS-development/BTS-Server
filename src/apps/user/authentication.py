import jwt
from rest_framework import authentication
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from apps.user.models import User
from django.conf import settings

import os
import json


class JSONWebTokenAuthentication(authentication.BaseAuthentication):
    def __init__(self):
        USER_SETTINGS = getattr(settings, "JWT_AUTH", None)

        self.JWT_SECRET_KEY = USER_SETTINGS["JWT_SECRET_KEY"]
        self.JWT_ALGORITHM = USER_SETTINGS["JWT_ALGORITHM"]

    def authenticate(self, request):
        header = self.get_header(request)
        if not header:
            return None

        if header.split()[0] not in ("jwt", "JWT",):
            return None

        token = header.split()[1]

        try:
            payload = jwt.decode(token, self.JWT_SECRET_KEY, self.JWT_ALGORITHM)
        except jwt.ExpiredSignature:
            msg = _("Signature has expired.")
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _("Error decoding signature.")
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user = self.get_user(payload)

        return (user, token)

    def get_header(self, request):
        return request.META.get("HTTP_AUTHORIZATION")

    def get_user(self, payload):
        try:
            user = User.objects.get(id=payload["user_id"])
        except User.DoesNotExist:
            msg = _("Invalud signature.")
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            mag = _("User account is disabled.")
            raise exceptions.AuthenticationFailed(msg)

        return user

