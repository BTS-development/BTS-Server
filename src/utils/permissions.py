from rest_framework import permissions
from apps.temperature.models import Temperature
from apps.group.models import Group, LinkedUserGroup


class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        temperature_queryset = Temperature.objects.get(id=obj)
        if temperature_queryset.owner_id == request.user.id:
            return True
        return False


class IsGroupAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        temperature_queryset = Temperature.objects.get(id=obj)
        linkedUserGroup_querysets = LinkedUserGroup.objects.filter(
            member=temperature_queryset.owner_id
        )  # 내가 접근 하려는 온도 주인이 속하는 그룹 쿼리셋 들

        for linkedUserGroup_queryset in linkedUserGroup_querysets:
            group_queryset = Group.objects.get(id=linkedUserGroup_queryset.group_id)
            if group_queryset.owner.id == request.user.id:
                return True
        return False
        # obj로 접근하려는 temperature id 가져옴

    # def has_permission(self, request, view):
    # user model 가져오고
    # group.get()
    # group model 가져오고 owner == request.user 맞나 본다


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
