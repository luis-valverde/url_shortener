""" Contain all APIs routing for version 1 (/api/v1/) """

from django.urls import path

from url.views import UrlAPIView


app_name = "api_v1"

urlpatterns = [
    path("url_shortener/", UrlAPIView.as_view()),
]
