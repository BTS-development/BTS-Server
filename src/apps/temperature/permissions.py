from rest_framework import permissions
from .models import Temperature


class IsGroupAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        temperature_queryset = Temperature.objects.get(id=obj)
        # group_queryset = Group.objects.get(owner=temperature_queryset.owner_id)
        # obj로 접근하려는 temperature id 가져옴

    # def has_permission(self, request, view):
    # user model 가져오고
    # group.get()
    # group model 가져오고 owner == request.user 맞나 본다


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
