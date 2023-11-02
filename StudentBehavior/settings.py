"""
Django settings for StudentBehavior project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5d+1@_ij+qvu3mf0wsaq&@8b223^(rf&246tdecw_vcj&yhnj)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'StudentBehavior',
    'students',
    'records'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",

    # 异常处理
    # "EXCEPTION_HANDLER": "utils.exceptions.exception_handler",

    # 统一响应JSON内容
    "DEFAULT_RENDERER_CLASSES": [
        'rest_framework.renderers.JSONRenderer',
    ],

    # 指定用于支持 coreapi 的 Schema
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",

    # 认证
    # "DEFAULT_AUTHENTICATION_CLASSES": (
        # "apps.common.jwt_auth.UapAuthentication",
        # "apps.common.jwt_auth.Authentication",
        # "rest_framework.authentication.TokenAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
    # ),

    "DEFAULT_PERMISSION_CLASSES": (
        # "common.permission.PrecisionMarketingPermission",
    ),

    "UNAUTHENTICATED_USER": None,  # 用户未登录，request.user返回的值
    "UNAUTHENTICATED_TOKEN": None,  # 用户未登录，request.auth返回的值
    # "DEFAULT_PAGINATION_CLASS": "utils.pagination.Pagination",
    "PAGE_SIZE": 10,
    # 设置全局过滤引擎
    "DEFAULT_FILTER_BACKENDS": [
        # 设置排序过滤引擎
        "rest_framework.filters.OrderingFilter",
        # 设置查询过滤引擎
        "django_filters.rest_framework.backends.DjangoFilterBackend"
    ],
}


ROOT_URLCONF = 'StudentBehavior.urls'

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

WSGI_APPLICATION = 'StudentBehavior.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ly",
        "USER": "root",
        "PASSWORD": "aBc_123456",
        "HOST": "206.233.133.31",
        "PORT": "3306",
        "POOL_OPTIONS": {
            "POOL_SIZE": 25,
            "MAX_OVERFLOW": 10
        },
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET foreign_key_checks = 0;",
        },
        "TEST": {
            "CHARSET": "utf8mb4"
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 跨域配置: 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "VIEW",
)

CORS_ALLOW_HEADERS = (
    "XMLHttpRequest",
    "X_FILENAME",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Pragma",
)