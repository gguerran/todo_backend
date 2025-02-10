from django.db.models import IntegerChoices


class Priority(IntegerChoices):
    LOW = 1, "Baixa"
    MEDIUM = 2, "Média"
    HIGH = 3, "Alta"
    CRITICAL = 4, "Crítica"
