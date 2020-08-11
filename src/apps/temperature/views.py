from .models import Temperature
from .serializers import TemperatureSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from config import Config
from rest_framework.response import Response
from .permissions import ReadOnly, IsGroupAdmin


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    permission_classes = [IsGroupAdmin | IsAuthenticated | ReadOnly]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def retrieve(self, request, pk):
        self.check_object_permissions(self.request, pk)
        queryset = Temperature.objects.get(id=pk)
        serializer = TemperatureSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        token = request.auth
        token.decode("utf-8")

        decoded = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)

        serializer = TemperatureSerializer(
            data={"value": request.data["value"], "owner": decoded["user_id"],}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        self.perform_create(serializer)

        return Response(serializer.data)

