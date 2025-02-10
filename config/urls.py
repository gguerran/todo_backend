from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urls_v1 = [
    path("api/v1/", include("apps.urls_v1")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    *urls_v1,
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path("silk/", include("silk.urls", namespace="silk")),
]

admin.site.site_header = "ToDo Admin"
admin.site.site_title = "Administração do ToDo"
admin.site.index_title = "Bem-vindo ao ToDo Admin"
