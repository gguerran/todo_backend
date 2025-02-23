from django.urls import path

from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from apps.core.views.doc import DocView

urlpatterns = [
    path("schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("doc/", DocView.as_view(), name="doc"),
]
