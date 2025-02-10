from django.contrib.admin import site 
from apps.todo.admin.task import TaskAdmin
from apps.todo.models import Task

site.register(Task, TaskAdmin)
