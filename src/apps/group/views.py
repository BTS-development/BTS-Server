from .models import Group,LinkedUserGroup
from .serializers import GroupSerializer,LinkedUserGroupSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from config import Config
from rest_framework.response import Response

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

        while True:

            try :
                
                code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

                serializer = GroupSerializer(
                    data={"name": request.data["name"], "owner": decoded["user_id"], "code":code}
                )

                if not serializer.is_valid():
                    return Response(serializer.errors)

                serializer.save()
                
                break
            
            except:
                pass

            
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
