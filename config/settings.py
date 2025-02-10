from datetime import timedelta
from pathlib import Path
from os import environ

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ.get("SECRET_KEY", default="^a-^xa(@")

DEBUG = bool(environ.get("DEBUG", default="False"))

ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", default="*").split(",")

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]

THIRD_PART_APPS = [
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_cleanup.apps.CleanupConfig",
    "auditlog",
    "silk",
]

LOCAL_APPS = [
    "apps.accounts",
    "apps.core",
    "apps.todo",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS

DJANGO_MIDDLEWARES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

THIRD_PART_MIDDLEWARES = [
    "auditlog.middleware.AuditlogMiddleware",
    "silk.middleware.SilkyMiddleware",
]

LOCAL_MIDDLEWARES = [
    "apps.core.middlewares.RequestMiddleware",
]

MIDDLEWARE = DJANGO_MIDDLEWARES + LOCAL_MIDDLEWARES + THIRD_PART_MIDDLEWARES

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = environ.get("CSRF_TRUSTED_ORIGINS", default="").split(",")

X_FRAME_OPTIONS = "DENY"

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for one year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "apps/core/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": environ.get("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": environ.get("DB_NAME", default="github-actions"),
        "USER": environ.get("DB_USER", default="postgres"),
        "PASSWORD": environ.get("DB_PASSWORD", default="postgres"),
        "HOST": environ.get("DB_HOST", default="localhost"),
        "PORT": environ.get("DB_PORT", default="5432"),
    }
}

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Fortaleza"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media/"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        [
            "rest_framework_simplejwt.authentication.JWTAuthentication",
            "rest_framework.authentication.SessionAuthentication",
        ]
        if DEBUG
        else ["rest_framework_simplejwt.authentication.JWTAuthentication"]
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "ORDERING_PARAM": "order_by",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SPECTACULAR_SETTINGS = {
    "TITLE": "Doc. ToDo API",
    "DESCRIPTION": "Documentação da API ToDo",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(environ.get("ACCESS_TOKEN_LIFETIME", default=5))),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=int(environ.get("REFRESH_TOKEN_LIFETIME", default=10))),
    "TOKEN_OBTAIN_SERIALIZER": "apps.accounts.api.serializers.TokenObtainPairSerializer",
}

SESSION_CACHE_ALIAS = "default"

CACHE_TTL = 60 * 1

FILTERS_DEFAULT_LOOKUP_EXPR = "icontains"

AUDITLOG_INCLUDE_ALL_MODELS = True
