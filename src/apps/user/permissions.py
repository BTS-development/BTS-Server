from rest_framework import permissions
from apps.group.models import Group, LinkedUserGroup

# 인증했냐?
class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


# 접근할려는 오브젝트 주인이냐?
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.owner_id == request.user.id)
        return obj.owner_id == request.user.id


# 그룹 관리자냐?
class IsGroupManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner_id == request.user.id
