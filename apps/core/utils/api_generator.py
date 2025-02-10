import os
import re


def convert_camel_case_for_snake_case(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def convert_snake_case_for_camel_case(name):
    return "".join(word.title() for word in name.split("_"))


def generate_serializer_from_models(models, app_name):
    base_path = f"apps/{app_name}/api/serializers"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    for model_name in models:
        file_name = convert_camel_case_for_snake_case(model_name)

        with open(f"{base_path}/{file_name}.py", "w+") as f:
            f.write(
                f"""from rest_framework.serializers import ModelSerializer
from apps.{app_name}.models import {model_name}


class {model_name}CreateSerializer(ModelSerializer):
    class Meta:
        model = {model_name}
        fields = "__all__"


class {model_name}DetailSerializer(ModelSerializer):
    class Meta:
        model = {model_name}
        fields = "__all__"


class {model_name}ReadSerializer(ModelSerializer):
    class Meta:
        model = {model_name}
        fields = "__all__"


class {model_name}UpdateSerializer(ModelSerializer):
    class Meta:
        model = {model_name}
        fields = "__all__"
"""
            )


def generate_serializer_init_from_app(app_name):
    all_files_on_serializers = os.listdir(f"apps/{app_name}/api/serializers")
    all_files_on_serializers = [
        file for file in all_files_on_serializers if file != "__init__.py" and file != "__pycache__"
    ]
    str_imports = ""
    all_names = []
    for file in all_files_on_serializers:
        file_name = file.replace(".py", "")
        serializer_names = ", ".join(
            [
                convert_snake_case_for_camel_case(file_name) + "CreateSerializer",
                convert_snake_case_for_camel_case(file_name) + "DetailSerializer",
                convert_snake_case_for_camel_case(file_name) + "ReadSerializer",
                convert_snake_case_for_camel_case(file_name) + "UpdateSerializer",
            ]
        )
        all_names.append(serializer_names)

        str_imports += f"from apps.{app_name}.api.serializers.{file_name} import {serializer_names}\n"
    serializer_names = ['", "'.join(name.split(", ")) for name in all_names]

    str_imports += f"""\n__all__ = ["{'", "'.join(serializer_names)}"]\n"""

    with open(f"apps/{app_name}/api/serializers/__init__.py", "w+") as f:
        f.write(str_imports)


def generate_filtersets_from_models(models, app_name):
    base_path = f"apps/{app_name}/api/filtersets"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    for model_name in models:
        file_name = convert_camel_case_for_snake_case(model_name)
        with open(f"{base_path}/{file_name}.py", "w+") as f:
            f.write(
                f"""from django_filters.rest_framework import FilterSet
from apps.{app_name}.models import {model_name}


class {model_name}Filterset(FilterSet):
    class Meta:
        model = {model_name}
        fields = []
"""
            )


def generate_filterset_init_from_app(app_name):
    all_files_on_filtersets = os.listdir(f"apps/{app_name}/api/filtersets")
    all_files_on_filtersets = [
        file for file in all_files_on_filtersets if file != "__init__.py" and file != "__pycache__"
    ]
    str_imports = ""
    all_names = []
    for file in all_files_on_filtersets:
        file_name = file.replace(".py", "")
        filterset_name = convert_snake_case_for_camel_case(file_name) + "Filterset"
        all_names.append(filterset_name)
        str_imports += f"from apps.{app_name}.api.filtersets.{file_name} import {filterset_name}\n"

    str_imports += f"""\n__all__ = ["{'", "'.join(all_names)}"]\n"""

    with open(f"apps/{app_name}/api/filtersets/__init__.py", "w+") as f:
        f.write(str_imports)


def generate_viewsets_from_models(models, app_name):
    base_path = f"apps/{app_name}/api/viewsets"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    for model_name in models:
        file_name = convert_camel_case_for_snake_case(model_name)

        with open(f"{base_path}/{file_name}.py", "w+") as f:
            f.write(
                f"""from apps.{app_name}.api.filtersets import {model_name}Filterset
from apps.{app_name}.api.serializers import (
    {model_name}CreateSerializer,
    {model_name}DetailSerializer,
    {model_name}ReadSerializer,
    {model_name}UpdateSerializer,
)
from apps.{app_name}.models import {model_name}
from apps.core.api.viewsets import BaseModelViewSet


class {model_name}ViewSet(BaseModelViewSet):
    model = {model_name}
    filterset_class = {model_name}Filterset
    serializer_class = {model_name}ReadSerializer

    action_serializer_classes = {{
        "list": {model_name}ReadSerializer,
        "retrieve": {model_name}DetailSerializer,
        "create": {model_name}CreateSerializer,
        "update": {model_name}UpdateSerializer,
        "partial_update": {model_name}UpdateSerializer,
    }}
    search_fields = {model_name}.get_search_fields()
"""
            )


def generate_viewset_init_from_app(app_name):
    all_files_on_viewsets = os.listdir(f"apps/{app_name}/api/viewsets")
    all_files_on_viewsets = [file for file in all_files_on_viewsets if file != "__init__.py" and file != "__pycache__"]
    str_imports = ""
    all_names = []
    for file in all_files_on_viewsets:
        file_name = file.replace(".py", "")
        viewset_name = convert_snake_case_for_camel_case(file_name) + "ViewSet"
        all_names.append(viewset_name)

        str_imports += f"from apps.{app_name}.api.viewsets.{file_name} import {viewset_name}\n"

    str_imports += f"""\n__all__ = ["{'", "'.join(all_names)}"]\n"""

    with open(f"apps/{app_name}/api/viewsets/__init__.py", "w+") as f:
        f.write(str_imports)


def generate_routers_from_viewsets(models, app_name):
    viewset_names = [model + "ViewSet" for model in models]
    router_names = [convert_camel_case_for_snake_case(model).replace("_", "-") for model in models]
    with open(f"apps/{app_name}/api/__init__.py", "w+") as f:
        pass

    router_register = ""
    for viewset_name, router_name in zip(viewset_names, router_names):
        router_register += f"""router.register("{router_name}", {viewset_name}, basename="{router_name}")\n"""

    with open(f"apps/{app_name}/api/routers.py", "w+") as f:
        f.write(
            f"""from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.{app_name}.api.viewsets import {", ".join(viewset_names)}

router = SimpleRouter()
{router_register}

urlpatterns = [
    path("", include(router.urls)),
]
"""
        )


def api_generator_from_app_model_names(model_names, app_name):
    generate_serializer_from_models(model_names, app_name)
    generate_serializer_init_from_app(app_name)
    generate_filtersets_from_models(model_names, app_name)
    generate_filterset_init_from_app(app_name)
    generate_viewsets_from_models(model_names, app_name)
    generate_viewset_init_from_app(app_name)
    generate_routers_from_viewsets(model_names, app_name)
