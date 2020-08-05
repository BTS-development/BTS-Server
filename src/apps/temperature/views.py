from .models import Temperature
from .serializers import TemperatureSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from config import Config
from rest_framework.response import Response


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def create(self, request):
        token = request.auth
        token.decode("utf-8")

        decoded = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)

        serializer = TemperatureSerializer(
            data={"value": request.data["value"], "owner": decoded["user_id"],}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)

