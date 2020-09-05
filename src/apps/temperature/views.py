import jwt
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .models import Temperature
from apps.group.models import LinkedUserGroup, Group
from .serializers import TemperatureSerializer

from apps.user.authentication import JSONWebTokenAuthentication
from apps.user.permissions import IsAutenticated, IsOwner, IsGroupManager


class CreateTemperatureAPI(generics.CreateAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer
    # 인증 했냐?

    def post(self, request, *args, **kwargs):
        request.data["owner"] = self.request.user.id
        return super().post(request, *args, **kwargs)


class GetTemperatureAPI(generics.RetrieveAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer
    permission_classes = [IsOwner]  # 접근할려는 오브젝트 주인이냐?

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        obj = Temperature.objects.get(id=self.kwargs["id"])
        self.check_object_permissions(self.request, obj)
        return obj


class GetGroupTemperatureAPI(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer
    permission_classes = [IsGroupManager]  # 그룹 주인이냐?

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        group = Group.objects.get(id=self.kwargs["groip_id"])

        self.check_object_permissions(self.request, group)

        users = LinkedUserGroup.objects.filter(group=group.id).values("member")

        temperatures = Temperature.objects.none()

        for user in users:
            temperatures |= Temperature.objects.filter(owner_id=user["member"])

        return temperatures.order_by("id")


class GetMyTemperatureAPI(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = TemperatureSerializer
    # 인증 했냐?

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Temperature.objects.filter(owner_id=self.request.user.id)
