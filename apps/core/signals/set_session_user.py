from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.core.models import BaseModelMixin
from apps.core.utils import get_request_user


@receiver(pre_save)
def set_session_user(sender, instance, **kwargs):
    user = get_request_user()

    if user and issubclass(sender, BaseModelMixin):
        if not instance.created_by:
            instance.created_by = user
        instance.modified_by = user
