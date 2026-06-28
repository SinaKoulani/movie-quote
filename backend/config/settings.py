from pathlib import Path
from datetime import timedelta
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("CONFIG_SECRET_KEY", "django-insecure-dev-key")

DEBUG = bool(int(os.environ.get("CONFIG_DEBUG", 1)))

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("CONFIG_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if host.strip()
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'statistic.apps.StatisticConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

dev_db = "sqlite:///" + str(BASE_DIR / "db.sqlite3")
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL", dev_db)
    )
}

PASSWORD_VALIDATOR = 'django.contrib.auth.password_validation.'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{PASSWORD_VALIDATOR}UserAttributeSimilarityValidator'},
    {'NAME': f'{PASSWORD_VALIDATOR}MinimumLengthValidator'},
    {'NAME': f'{PASSWORD_VALIDATOR}CommonPasswordValidator'},
    {'NAME': f'{PASSWORD_VALIDATOR}NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = []

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAdminUser'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {'type': 'basic'},
        'bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'},
    },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'SHOW_URL_CODE_SAMPLES': True,
}

IPSTACK_ACCESS_KEY = os.environ.get("IPSTACK_ACCESS_KEY")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("CONFIG_EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("CONFIG_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("CONFIG_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_PORT = 587

CORS_ALLOW_ALL_ORIGINS = True

# تنظیمات امن فقط برای پروداکشن
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 259200
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = bool(int(os.environ.get("CONFIG_SECURE_SSL_REDIRECT", 1)))

    secure_proxy = os.environ.get("CONFIG_SECURE_PROXY_SSL_HEADER", "")
    if secure_proxy:
        parts = [p.strip() for p in secure_proxy.split(",") if p.strip()]
        if len(parts) == 2:
            SECURE_PROXY_SSL_HEADER = (parts[0], parts[1])

# تنظیمات لوکال برای جلوگیری از ریدایرکت HTTPS
if DEBUG:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False

JAZZMIN_SETTINGS = {
    "site_title": "Movie Admin",
    "site_header": "Movie Admin",
    "site_brand": "Movie Admin",
    "welcome_sign": "Welcome to Movie Admin",
    "copyright": "Movie Project",
    "topmenu_links": [],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
