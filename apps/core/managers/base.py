from django.db.models.manager import Manager


class BaseManager(Manager):
    def get_or_none(self, *args, **kwargs):
        try:
            return super().get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None
