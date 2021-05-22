import environ

from pathlib import Path

# Dirs
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
BASE_DIR = ROOT_DIR / "task_manager"

# Envs
env = environ.Env()
env.read_env(str(ROOT_DIR / ".env"))

# Secrets
SECRET_KEY = env.str("SECRET_KEY")

# Allowed Hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "drf_spectacular",
    "rest_framework",
    "rest_framework.authtoken",
]

LOCAL_APPS = [
    "accounts",
    "core",
    "categories",
    "tasks",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLs
ROOT_URLCONF = "task_manager.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# WSGI
WSGI_APPLICATION = "task_manager.wsgi.application"

# Databases
DATABASES = {
    "default": env.db("DATABASE_URL"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env.str("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# Auth
AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Intl
LANGUAGE_CODE = "en"

TIME_ZONE = "Asia/Almaty"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Locale
LOCALE_PATHS = [
    ROOT_DIR / "locale",
]

# Static
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    # BASE_DIR / "static",
]

STATIC_ROOT = ROOT_DIR / "staticfiles"

# Media
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# Default Auto Field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email
EMAIL_TIMEOUT = 5

# DRF
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAdminUser",
    ],
}

# Docs
SPECTACULAR_SETTINGS = {
    "TITLE": "REST Todo App",
    "DESCRIPTION": "API for REST Todo App",
    "VERSION": "1.0.0",
}
