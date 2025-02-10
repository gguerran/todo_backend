from rest_framework.decorators import action
from rest_framework.response import Response

from apps.accounts.api.filtersets import UserFilterset
from apps.accounts.api.serializers import (
    UserCreateSerializer,
    UserUpdatePasswordSerializer,
    UserUpdateProfileImageSerializer,
    UserReadSerializer,
    UserUpdateSerializer,
    UserDetailSerializer,
)
from apps.accounts.models import User
from apps.core.api.viewsets import BaseModelViewSet


class UserViewSet(BaseModelViewSet):
    model = User
    filterset_class = UserFilterset
    serializer_class = UserReadSerializer

    action_serializer_classes = {
        "list": UserReadSerializer,
        "retrieve": UserDetailSerializer,
        "create": UserCreateSerializer,
        "update": UserUpdateSerializer,
        "partial_update": UserUpdateSerializer,
        "me": {
            "GET": UserDetailSerializer,
            "PUT": UserUpdateSerializer,
        },
        "password": UserUpdatePasswordSerializer,
        "profile_image": UserUpdateProfileImageSerializer,
    }
    search_fields = ["name", "email"]
    select_related = ["address", "events"]
    prefetch_related = ["all_permissions", "groups", "module_access"]

    @action(detail=False, methods=["get", "put"])
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        if self.request.method == "GET":
            return Response(self.get_serializer(user).data)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["put"])
    def password(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=["put"])
    def profile_image(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
