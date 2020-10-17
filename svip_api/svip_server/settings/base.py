"""
Django settings for svip_server project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ceqqi+r54k4btz4v_3#kl3_%xpbxopm9fag@vq-6q72-v!^lg$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1', '0.0.0.0',
    'svip-dev.nexus.ethz.ch',
    'svip-test.nexus.ethz.ch',
    'svip.nexus.ethz.ch',
    'svip.ch', 'www.svip.ch',
    'svip.sib.swiss', 'svip-public.sib.swiss'
]

CSRF_TRUSTED_ORIGINS = [
    'localhost:8080',
    'svip-dev.nexus.ethz.ch',
    'svip-test.nexus.ethz.ch',
    'svip.ch', 'www.svip.ch',
    'svip.sib.swiss', 'svip-public.sib.swiss'
]

# allows django to detect that we're running behind a secure proxy (e.g., nginx)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# allows django to use nginx's x-forwarded-host field to set its hostname
USE_X_FORWARDED_HOST = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'corsheaders',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'simple_history',

    # FIXME: enable when we get around to blacklisting tokens correctly
    # 'rest_framework_simplejwt.token_blacklist',

    # # Django Elasticsearch integration
    # 'django_elasticsearch_dsl',
    # # Django REST framework ES integration
    # 'django_elasticsearch_dsl_drf',

    # local apps
    'svip_server',
    'api'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'svip_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'svip_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django_db_cascade.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        # below is the db cache backend, currently commented out in favor of redis
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'LOCATION': 'default_cache_tbl',
        # 'TIMEOUT': 60*60*24*15,  # 15 days
        # 'MAX_ENTRIES': 5000,

        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        'TIMEOUT': 60*60*24*15,  # 15 days
        'MAX_ENTRIES': 5000,
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

DB_CONNECTION_URL = ("postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s" % DATABASES['default'])

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTH_USER_MODEL = 'auth.User'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/api/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# colorizes test output
TEST_RUNNER="redgreenunittest.django.runner.RedGreenDiscoverRunner"


# django-rest-framework config
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'api.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'svip_server.utils.BrowsableAPIRendererWithoutForms',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
        'rest_framework_simplejwt.tokens.SlidingToken'
    ),

    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'JWT_AUTH_COOKIE': None  # 'jwt-cookie'
}

# CORS config (https://github.com/ottoyiu/django-cors-headers/)
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:8080',
    'svip-dev.nexus.ethz.ch',
    'svip-test.nexus.ethz.ch'
)
CORS_ALLOW_CREDENTIALS = True

# Elasticsearch configuration
# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': 'elasticsearch:9200'
#     },
# }

SOCIBP_BASE_URL = os.environ['SOCIBP_BASE_URL']
SOCIBP_API_URL = SOCIBP_BASE_URL + '/api'
