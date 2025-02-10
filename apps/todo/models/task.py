from django.db.models import CharField, DateTimeField, TextField, ForeignKey, CASCADE, PositiveIntegerField

from apps.core.models import BaseModel
from apps.todo.choices import Priority, Status


class Task(BaseModel):
    title = CharField(max_length=255, verbose_name="Título")
    description = TextField(verbose_name="Descrição", null=True, blank=True)
    due_date = DateTimeField(verbose_name="Data de vencimento", null=True, blank=True)
    delivery_date = DateTimeField(verbose_name="Data de entrega", null=True, blank=True)
    user = ForeignKey(to="accounts.User", on_delete=CASCADE, verbose_name="Usuário", related_name="tasks")
    priority = PositiveIntegerField(choices=Priority.choices, default=Priority.LOW, verbose_name="Prioridade")
    status = PositiveIntegerField(choices=Status.choices, default=Status.TODO, verbose_name="Status")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ["status", "priority", "due_date", "title"]

    @staticmethod
    def get_search_fields():
        return ["title", "description", "user__name", "user__email"]
