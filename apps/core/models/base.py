from apps.core.models.mixin import BaseModelMixin
from apps.core.managers import BaseManager


class BaseModel(BaseModelMixin):
    objects = BaseManager()

    class Meta:
        abstract = True

    def get_search_fields():
        return []
