from django.urls import path

from .views import (
    GetGroupTemperatureAPI,
    GetMyTemperatureAPI,
    GetTemperatureAPI,
    CreateTemperatureAPI,
)

urlpatterns = [
    path("", CreateTemperatureAPI.as_view()),
    path("<id>", GetTemperatureAPI.as_view()),
    path("group/<group_id>", GetGroupTemperatureAPI.as_view()),
    path("my/", GetMyTemperatureAPI.as_view()),
]
