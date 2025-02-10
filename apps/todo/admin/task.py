from django.contrib.admin import ModelAdmin


class TaskAdmin(ModelAdmin):
    list_display = ["title", "description", "due_date", "delivery_date", "user", "priority", "status", "created_at", "modified_at"]
    search_fields = ["title", "description"]
    list_filter = ["priority", "status"]
    fields = ["title", "description", "due_date", "delivery_date", "user", "priority", "status"]
    readonly_fields = ["created_at", "modified_at"]
    autocomplete_fields = ["user"]
    list_editable = ["status"]
