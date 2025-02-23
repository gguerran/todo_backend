from django.urls import path, include

urlpatterns = [
    # DOCS
    path("", include("apps.doc_urls")),
    # API
    path("", include("apps.accounts.api.routers")),
    path("", include("apps.todo.api.routers")),
]
