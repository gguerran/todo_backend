from django.contrib.auth.password_validation import validate_password

from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
    SerializerMethodField,
)

from apps.accounts.models import User


class UserCreateSerializer(ModelSerializer):
    profile_image = Base64ImageField(required=False)
    password = CharField(write_only=True)
    password_confirmation = CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "created_by",
            "modified_by",
            "created_at",
            "modified_at",
            "name",
            "email",
            "profile_image",
            "password",
            "password_confirmation",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_by": {"read_only": True},
            "modified_by": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }

    def validate(self, data):
        if data.get("password") != data.pop("password_confirmation"):
            raise ValidationError("As senhas não conferem")
        validate_password(data.get("password"))
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance


class UserReadSerializer(ModelSerializer):
    profile_image = SerializerMethodField()

    def get_profile_image(self, obj) -> str:
        request = self.context.get("request")
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)
        return None

    class Meta:
        model = User
        fields = [
            "id",
            "created_by",
            "modified_by",
            "created_at",
            "modified_at",
            "name",
            "email",
            "profile_image",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_by": {"read_only": True},
            "modified_by": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }


class UserDetailSerializer(ModelSerializer):
    profile_image = SerializerMethodField()

    def get_profile_image(self, obj) -> str:
        request = self.context.get("request")
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)
        return None

    class Meta:
        model = User
        fields = [
            "id",
            "created_by",
            "modified_by",
            "created_at",
            "modified_at",
            "name",
            "email",
            "is_staff",
            "is_active",
            "profile_image",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_by": {"read_only": True},
            "modified_by": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }


class UserUpdateSerializer(ModelSerializer):
    profile_image = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "created_by",
            "modified_by",
            "created_at",
            "modified_at",
            "name",
            "email",
            "profile_image",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_by": {"read_only": True},
            "modified_by": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }


class UserUpdatePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True)
    password_confirmation = CharField(write_only=True)
    last_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["password", "password_confirmation", "last_password"]

    def validate(self, data):
        user = self.instance
        if not user.check_password(data.pop("last_password")):
            raise ValidationError({"last_password": "Senha atual incorreta"})

        if data.get("password") != data.pop("password_confirmation"):
            raise ValidationError({"password_confirmation": "As senhas não conferem"})
        try:
            validate_password(data.get("password"))
        except Exception as e:
            raise ValidationError({"password": e.messages})
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance


class UserUpdateProfileImageSerializer(ModelSerializer):
    profile_image = Base64ImageField(required=True)

    class Meta:
        model = User
        fields = ["profile_image"]
        extra_kwargs = {"profile_image": {"required": True}}
