import jwt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Temperature
from .serializers import TemperatureSerializer

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.authentication import JSONWebTokenAuthentication
from utils.permissions import ReadOnly, IsGroupAdmin, IsOwnerOnly
from rest_framework.permissions import IsAuthenticated
from config import Config


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    permission_classes = [IsOwnerOnly | IsGroupAdmin & IsAuthenticated & ReadOnly]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    @action(detail=False, methods=["get"], permission_classes=[IsGroupAdmin])
    def group_temperatures(self, request, pk=None):
        self.check_object_permissions(self.request, pk)

    @action(detail=False, methods=["get"])
    def my_temperatures(self, request, format=None):
        token = request.auth
        payload = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)

        queryset = Temperature.objects.filter(owner_id=payload["user_id"])
        serializer = TemperatureSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        self.check_object_permissions(self.request, pk)
        queryset = Temperature.objects.get(id=pk)
        serializer = TemperatureSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        token = request.auth
        payload = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)

        serializer = TemperatureSerializer(
            data={"value": request.data["value"], "owner": payload["user_id"],}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        self.perform_create(serializer)

        return Response(serializer.data)

