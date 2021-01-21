from django.urls import path

from .views import GetUserAPI

urlpatterns = [path("<user_id>", GetUserAPI.as_view())]
