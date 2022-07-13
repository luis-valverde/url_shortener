""" Contain all project URLs """

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from rest_framework_simplejwt import views as jwt_views
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/v1/", include("urlshortener.api_versions.v1", namespace='v1')),

    # Swagger documentation
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="URL Shortener Project",
        description="APIs for URL Shortener",
        version="1.0.0"
    ), name='openapi-schema'),
]
