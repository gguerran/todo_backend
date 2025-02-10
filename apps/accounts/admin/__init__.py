from django.contrib.admin import site
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from apps.accounts.admin.user import UserAdmin
from apps.accounts.models import User

site.register(User, UserAdmin)

site.unregister(OutstandingToken)
site.unregister(BlacklistedToken)
