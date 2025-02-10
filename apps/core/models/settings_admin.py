from apps.core.models.base import BaseModel
from django.db.models import CharField


class SettingAdmin(BaseModel):
    key = CharField(max_length=255, unique=True)
    value = CharField(max_length=255)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Configuração Administrativa"
        verbose_name_plural = "Configurações Administrativas"
