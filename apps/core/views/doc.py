from django.views.generic import TemplateView
from django.urls import reverse


class DocView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Doc. ToDo API"
        base_path = self.request.build_absolute_uri("/")[:-1]
        context["url"] = base_path + reverse("schema")
        return context
