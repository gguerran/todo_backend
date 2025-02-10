from django.contrib.auth.admin import UserAdmin as DJUserAdmin


class UserAdmin(DJUserAdmin):
    list_display = ["name", "email", "is_active", "is_superuser"]
    list_filter = ["is_active", "is_superuser"]
    ordering = ("name", "email")
    fieldsets = [
        ["Informações pessoais", {"fields": ["name", "email", "profile_image"]}],
        [
            "Dados de acesso",
            {
                "fields": [
                    "password",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                ]
            },
        ],
    ]
    add_fieldsets = [
        ["Informações pessoais", {"fields": ["name", "email", "profile_image"]}],
        [
            "Dados de acesso",
            {
                "fields": [
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                ]
            },
        ],
    ]
    search_fields = ["name", "email"]
    filter_horizontal = ["user_permissions", "groups"]
    list_editable = ["is_active", "is_superuser"]
