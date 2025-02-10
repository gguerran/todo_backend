from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.conf import settings

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import GenericViewSet


class CachedMixin:
    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BaseGenericViewSet(GenericViewSet):
    parser_classes = [JSONParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    model = None
    serializer_class = None  # Default
    action_serializer_classes = {
        # 'list': None,
        # 'retrieve': None,
        # 'create': None,
        # 'update': None,
        # 'partial_update': None,
        # 'destroy': None,
    }
    filterset_class = None
    queryset = None
    module_codename = None
    get_modules_codename = []
    select_related = []
    prefetch_related = []

    def get_queryset(self):
        if self.model:
            return (
                self.model.objects.select_related(*self.select_related).prefetch_related(*self.prefetch_related).all()
            )
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in self.action_serializer_classes:
            if isinstance(self.action_serializer_classes[self.action], dict):
                return self.action_serializer_classes[self.action][self.request.method]
            return self.action_serializer_classes[self.action]
        return self.serializer_class

    @property
    def search_fields(self):
        return self.filterset_class._meta.search_fields if self.filterset_class else []


class ListModelViewSet(BaseGenericViewSet, ListModelMixin):
    pass


class BaseReadOnlyModelViewSet(BaseGenericViewSet, RetrieveModelMixin, ListModelMixin):
    pass


class BaseModelViewSet(
    BaseGenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    pass
