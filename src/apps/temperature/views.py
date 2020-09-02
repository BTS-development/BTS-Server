import jwt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Temperature
from .serializers import TemperatureSerializer
from rest_framework import generics

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.authentication import JSONWebTokenAuthentication
from utils.permissions import ReadOnly, IsGroupAdmin, IsOwnerOnly
from rest_framework.permissions import IsAuthenticated
from config import Config


class TemperatureDetail(APIView):
    permission_classes = [IsOwnerOnly | IsGroupAdmin & IsAuthenticated & ReadOnly]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def get_object(self, pk):
        try:
            obj = Temperature.objects.get(id=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Temperature.DoesNotExist:
            return Response({"message": "Temperature DoesNotExist"}, status=404)

    @action(detail=False, methods=["get"])
    def group_temperatures(self, request, pk=None):
        temperature = self.get_object(pk=pk)

    @action(detail=False, methods=["get"])
    def my_temperatures(self, request, format=None):
        token = request.auth
        payload = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)

        queryset = Temperature.objects.filter(owner_id=payload["user_id"])
        serializer = TemperatureSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, pk):
        temperature = self.get_object(pk=pk)
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)

    def post(self, request):
        token = request.auth
        payload = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)

        serializer = TemperatureSerializer(
            data={"value": request.data["value"], "owner": payload["user_id"],}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        self.perform_create(serializer)

        return Response(serializer.data)

