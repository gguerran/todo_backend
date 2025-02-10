from django.contrib.admin import ModelAdmin


class SettingsAdminAdmin(ModelAdmin):
    list_display = ["key", "value"]
    list_filter = ["key"]
    ordering = ["key"]
    fields = ["key", "value"]
