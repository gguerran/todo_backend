from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from apps.core.utils import api_generator_from_app_model_names


class Command(BaseCommand):
    help = "List all models for a given app"

    def add_arguments(self, parser):
        parser.add_argument(
            "args",
            metavar="app_label[.ModelName]",
            nargs="*",
            type=str,
            help="The label of the application",
        )

    def handle(self, *app_labels, **options):
        if not app_labels:
            app_list = [
                app_config.label for app_config in apps.get_app_configs() if app_config.models_module is not None
            ]
            if not app_list:
                raise CommandError("There are no models to generate API")
            for app_label in app_list:
                try:
                    app_config = apps.get_app_config(app_label)
                    models = app_config.get_models()
                    model_names = [model.__name__ for model in models]
                    api_generator_from_app_model_names(model_names, app_label)
                    self.stdout.write(f"API's GERADAS PARA OS MODELS DA APP '{app_label}':")
                    for model_name in model_names:
                        self.stdout.write(f" - {model_name}")
                except LookupError:
                    raise CommandError(f"App '{app_label}' not found")
                except Exception as e:
                    raise CommandError(f"Error: {e}")
        else:
            for app_label in app_labels:
                try:
                    app_label, model_label = app_label.split(".")
                except ValueError:
                    app_label, model_label = app_label, None
                try:
                    app_config = apps.get_app_config(app_label)
                    if model_label:
                        model = app_config.get_model(model_label)
                        model_names = [model.__name__]
                    else:
                        models = app_config.get_models()
                        model_names = [model.__name__ for model in models]
                    api_generator_from_app_model_names(model_names, app_label)
                    self.stdout.write(f"API's GERADAS PARA OS MODELS DA APP '{app_label}':")
                    for model_name in model_names:
                        self.stdout.write(f" - {model_name}")
                except LookupError as e:
                    print(e)
                    raise CommandError(f"App '{app_label}' not found")
                except Exception as e:
                    raise CommandError(f"Error: {e}")
