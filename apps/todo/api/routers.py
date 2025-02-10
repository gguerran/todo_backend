from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.todo.api.viewsets import TaskViewSet

router = SimpleRouter()
router.register("task", TaskViewSet, basename="task")


urlpatterns = [
    path("", include(router.urls)),
]
