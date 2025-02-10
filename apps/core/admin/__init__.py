from django.contrib.admin import site

from apps.core.admin.settings_admin import SettingsAdminAdmin
from apps.core.models import SettingAdmin

site.register(SettingAdmin, SettingsAdminAdmin)
