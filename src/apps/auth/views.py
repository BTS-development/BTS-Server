from django.shortcuts import render
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from apps.user.serializers import UserDetailsSerializer
from .serializers import JSONWebTokenSerializer
from rest_framework.response import Response

# Create your views here.


class ObtainJSONWebToken(ObtainJSONWebToken):
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get("user") or request.user
            token = serializer.object.get("token")
            response_data = self.jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
                response.set_cookie(
                    api_settings.JWT_AUTH_COOKIE,
                    token,
                    expires=expiration,
                    httponly=True,
                )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def jwt_response_payload_handler(self, token, user=None, request=None):
        return {
            "token": token,
            "user": UserDetailsSerializer(user).data,
        }
