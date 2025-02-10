from rest_framework.serializers import ModelSerializer
from apps.todo.models import Task


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskDetailSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskReadSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
