from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Create your views here.


class GetUserAPI(generics.RetrieveAPIView):
    authentication_classes = []
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return User.objects.get(id=self.kwargs["user_id"])
