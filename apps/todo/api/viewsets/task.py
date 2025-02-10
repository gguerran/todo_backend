from apps.todo.api.filtersets import TaskFilterset
from apps.todo.api.serializers import (
    TaskCreateSerializer,
    TaskDetailSerializer,
    TaskReadSerializer,
    TaskUpdateSerializer,
)
from apps.todo.models import Task
from apps.core.api.viewsets import BaseModelViewSet


class TaskViewSet(BaseModelViewSet):
    model = Task
    filterset_class = TaskFilterset
    serializer_class = TaskReadSerializer

    action_serializer_classes = {
        "list": TaskReadSerializer,
        "retrieve": TaskDetailSerializer,
        "create": TaskCreateSerializer,
        "update": TaskUpdateSerializer,
        "partial_update": TaskUpdateSerializer,
    }
    search_fields = Task.get_search_fields()

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
