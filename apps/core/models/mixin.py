import uuid

from django.db.models import Model, UUIDField, DateTimeField, PROTECT, ForeignKey


class BaseModelMixin(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = ForeignKey(
        to="accounts.User",
        verbose_name="criado por",
        on_delete=PROTECT,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    modified_by = ForeignKey(
        to="accounts.User",
        verbose_name="modificado por",
        on_delete=PROTECT,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
    )
    created_at = DateTimeField(auto_now_add=True, verbose_name="criado em")
    modified_at = DateTimeField(auto_now=True, verbose_name="modificado em")

    class Meta:
        abstract = True
        ordering = ["-created_at"]
