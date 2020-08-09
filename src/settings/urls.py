"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from apps.user.views import UserViewSet
from apps.temperature.views import TemperatureViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

router = DefaultRouter()
router.register(r"users/account", UserViewSet)
router.register(r"temperatures", TemperatureViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^users/account/login", obtain_jwt_token),
    url(r"^users/account/refresh", refresh_jwt_token),
    url(r"^users/account/verify", verify_jwt_token),
    url(r"^users/account/signup", include("rest_auth.registration.urls")),
]
