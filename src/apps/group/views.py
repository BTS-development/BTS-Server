from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

import os
import sys 

from .models import Group,LinkedUserGroup
from .serializers import GroupSerializer,LinkedUserGroupSerializer

from ..temperature.models import Temperature
from ..temperature.serializers import TemperatureSerializer

import jwt
import json
import random
import string




class GroupViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def create(self, request):
                
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        
        while(bool(Group.objects.filter(code=code))):
            code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))



        serializer = GroupSerializer(
            data={"name": request.data["name"], "owner": request.user.id, "code":code}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)

    def list(self, request):


        queryset = Group.objects.filter(owner=request.user.id)

        serializer = GroupSerializer(queryset, many=True)

        return Response(serializer.data)


    @action(detail=False,methods=['POST'])
    def join(self,request):
    
        try:
            group = Group.objects.filter(code=request.data["code"]).values()[0]
        except:
            return Response({"message":"존재하지 않는 그룹코드입니다"})
        
        if group["owner_id"] == request.user.id :
            return Response({"message":"이 그룹의 관리자입니다"})

        group_id = group["id"]

        serializer = LinkedUserGroupSerializer(
            data= {"group":group_id, "member":request.user.id}
        )
        

        if not serializer.is_valid():
            return Response(serializer.errors)

        
        serializer.save()
      
        return Response(serializer.data)


    