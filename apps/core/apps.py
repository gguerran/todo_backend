from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    verbose_name = "Dados Base"

    def ready(self):
        from apps.core import signals as core_signals  # noqa
