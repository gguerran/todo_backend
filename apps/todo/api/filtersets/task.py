from django_filters.rest_framework import FilterSet
from apps.todo.models import Task


class TaskFilterset(FilterSet):
    class Meta:
        model = Task
        fields = ["title", "description", "user__name", "user__email", "priority", "status"]
