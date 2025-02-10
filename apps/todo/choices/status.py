from django.db.models import IntegerChoices


class Status(IntegerChoices):
    TODO = 1, "A fazer"
    DOING = 2, "Fazendo"
    DONE = 3, "Feito"
    CANCELED = 4, "Cancelado"
