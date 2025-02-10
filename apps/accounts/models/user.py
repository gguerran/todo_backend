from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, EmailField, ImageField

from apps.accounts.managers import UserManager
from apps.core.models import BaseModelMixin


def upload_to(instance, filename):
    return f"profile_images/{instance.pk}/{filename}"


class User(AbstractBaseUser, PermissionsMixin, BaseModelMixin):
    name = CharField(verbose_name="nome completo", max_length=255)
    email = EmailField(verbose_name="endereço de e-mail", unique=True)
    profile_image = ImageField(verbose_name="foto de perfil", upload_to=upload_to, blank=True, null=True)

    is_staff = BooleanField(verbose_name="Pode acessar o painel", default=True)
    is_active = BooleanField(verbose_name="ativo", default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["name", "-created_at"]

    def __str__(self):
        return self.name

    @property
    def serializer_class(self):
        from apps.accounts.api.serializers.user import UserDetailSerializer

        return UserDetailSerializer

    def get_search_fields():
        return ["name", "email"]
