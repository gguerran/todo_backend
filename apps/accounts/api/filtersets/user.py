from django_filters.rest_framework import FilterSet, CharFilter

from apps.accounts.models import User


class UserFilterset(FilterSet):
    groups = CharFilter(field_name="groups__name", lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["name", "email"]
