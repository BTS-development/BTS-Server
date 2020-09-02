from rest_framework import permissions
from apps.temperature.models import Temperature
from apps.group.models import Group, LinkedUserGroup


class IsOwnerOnly(permissions.BasePermission):
    message = "you are not owner this temperature"

    def has_object_permission(self, request, view, obj):
        return obj.owner_id == request.user.id


class IsGroupAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        linkedUserGroup_querysets = LinkedUserGroup.objects.filter(
            member=obj.owner_id
        )  # 내가 접근 하려는 온도 주인이 속하는 그룹 쿼리셋 들

        for queryset in linkedUserGroup_querysets:
            group_queryset = Group.objects.get(id=queryset.group_id)
            if group_queryset.owner.id == request.user.id:
                return True
        return False


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
