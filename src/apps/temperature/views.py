import jwt
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .models import Temperature
from apps.group.models import LinkedUserGroup
from .serializers import TemperatureSerializer

from utils.authentication import JSONWebTokenAuthentication
from utils.permissions import ReadOnly, IsGroupAdmin, OwnerOnly
from rest_framework.permissions import IsAuthenticated


class CreateTemperatureAPI(generics.CreateAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer

    def post(self, request, *args, **kwargs):
        request.data["owner"] = self.request.user.id
        return super().post(request, *args, **kwargs)


class GetTemperatureAPI(generics.RetrieveAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return Temperature.objects.get(id=self.kwargs["id"])


class GetGroupTemperatureAPI(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        users = LinkedUserGroup.objects.filter(group=self.kwargs["group_id"]).values(
            "member"
        )

        temperatures = Temperature.objects.none()

        for user in users:
            temperatures |= Temperature.objects.filter(owner_id=user["member"])

        return temperatures.order_by("id")


class GetMyTemperatureAPI(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Temperature.objects.filter(owner_id=self.request.user.id)
