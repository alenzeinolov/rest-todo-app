from django.urls import path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from categories.api.viewsets import CategoryViewSet
from tasks.api.viewsets import TaskViewSet

router = SimpleRouter()
router.register("categories", CategoryViewSet)
router.register("tasks", TaskViewSet)

app_name = "api"
urlpatterns = [
    path("auth-token", obtain_auth_token),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="api:schema"), name="redoc"),
] + router.urls
