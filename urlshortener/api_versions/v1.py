""" Contain all APIs routing for version 1 (/api/v1/) """

from django.urls import path, include

from rest_framework.routers import DefaultRouter


app_name = "api_v1"

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
