from rest_framework import serializers
from .models import Group,LinkedUserGroup


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class LinkedUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedUserGroup
        fields = "__all__"
