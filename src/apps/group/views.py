from .models import Group,LinkedUserGroup
from .serializers import GroupSerializer,LinkedUserGroupSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from config import Config
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json

import random
import string



class GroupViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def create(self, request):

        #-------------------------
        token = request.auth
        token.decode("utf-8")

        decoded = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)
        #------------------------------------

        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        
        while(bool(Group.objects.filter(code=code))):
            code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

        

        serializer = GroupSerializer(
            data={"name": request.data["name"], "owner": decoded["user_id"], "code":code}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
                
                
           

            
        return Response(serializer.data)



    def list(self, request):

        #---------------------
        token = request.auth
        token.decode("utf-8")

        decoded = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)
        #------------------------------

        queryset = Group.objects.filter(owner=decoded["user_id"])
        
        serializer = GroupSerializer(queryset, many=True)

        return Response(serializer.data)


        def retrieve(self, request, pk=None):
    
            #---------------------
            token = request.auth
            token.decode("utf-8")

            decoded = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)
            #------------------------------

            queryset = Group.objects.all()
            group = get_object_or_404(queryset,pk=pk)
            serializer = GroupSerializer(group)

            if not serializer.is_valid():
                return Response(serializer.errors)   

            return Response(serializer.data)



class MemberViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def create(self,request):

         #-------------------------
        token = request.auth
        token.decode("utf-8")

        decoded = jwt.decode(token, Config.SECRET_KEY, Config.ALGORITHM)
        #------------------------------------

        group = Group.objects.filter(code=request.data["code"]).values()
        group_id = group[0]["id"]

        serializer = LinkedUserGroupSerializer(
            data= {"group":group_id, "member":decoded["user_id"]}
        )
        

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)