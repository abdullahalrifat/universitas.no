# -*- coding: utf-8 -*-
"""
Django settings for universitas_no project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: path.join(SITE_ROOT, ...)
from os import environ
from os.path import abspath, dirname, join, normpath
import django.conf.global_settings as DEFAULT_SETTINGS

# PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
BASE_DIR = environ["DJANGO_SOURCE_FOLDER"]

# Absolute filesystem path to the top-level project folder:
PROJECT_ROOT_FOLDER = dirname(BASE_DIR)
# These values are set in the virtualenv postactivate bash file

SECRET_KEY = environ["DJANGO_SECRET_KEY"]
SITE_URL = environ["DJANGO_SITE_URL"]

# Prodsys for universitas.
PRODSYS_USER = environ["DJANGO_PRODSYS_USER"]
PRODSYS_PASSWORD = environ["DJANGO_PRODSYS_PASSWORD"]
PRODSYS_URL = environ["DJANGO_PRODSYS_URL"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# CUSTOM APPS
INSTALLED_APPS = (
    'apps.issues',
    'apps.stories',
    'apps.core',
    'apps.photo',
    'apps.frontpage',
    'apps.contributors',
    'apps.markup',
    'apps.legacy_db',
    'functional_tests',
    )

# THIRD PARTY APPS
INSTALLED_APPS = (
    # 'django_nose',
    'autocomplete_light',
    'django_extensions',
    'compressor',
    'sekizai',
    'sorl.thumbnail',
    ) + INSTALLED_APPS

# CORE APPS
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ) + INSTALLED_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'universitas_no.urls'
WSGI_APPLICATION = 'universitas_no.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ["DJANGO_DB_NAME"],
        'USER': environ["DJANGO_DB_USER"],
        'PASSWORD': environ["DJANGO_DB_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '',       # Set to empty string for default.
    },
    'prodsys': {
        'ENGINE': 'mysql.connector.django',
        'NAME': environ["DJANGO_PRODSYS_DB_NAME"],
        'USER': environ["DJANGO_PRODSYS_DB_USER"],
        'PASSWORD': environ["DJANGO_PRODSYS_DB_PASSWORD"],
        # 'HOST': environ["DJANGO_PRODSYS_DB_HOST"],
        'HOST': 'localhost', # TODO: Endre dette tilbake det er bare et eksperiment.
        'PORT': '',       # Set to empty string for default.
    }
}
DATABASE_ROUTERS = ['apps.legacy_db.router.ProdsysRouter']

#SORL
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 0,
            # 'PASSWORD': 'yadayada',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            }
        },
    },
}


# # When using unix domain sockets with Redis
# # Note: ``LOCATION`` needs to be the same as the ``unixsocket`` setting
# # in your redis.conf
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '/path/to/socket/file',
#         'OPTIONS': {
#             'DB': 1,
#             'PASSWORD': 'yadayada',
#             'PARSER_CLASS': 'redis.connection.HiredisParser'
#         },
#     },

###############   MEMCACHED (Bruker redis i stedet)
# }
# CACHES = {
#     'default': {
#         # TODO: PyLibMCCache er visst rasker, men ikke ennå klar for python 3.
#         'BACKEND': 'djpymemcache.backend.PyMemcacheCache',
#         # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         # 'LOCATION': 'unix:/tmp/memcached.sock',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# When using TCP connections

# INTERNATIONALIZATION
LANGUAGE_CODE = 'no'
TIME_ZONE = 'Europe/Oslo'
USE_I18N = True  # Internationalisation (string translation)
USE_L10N = True  # Localisation (numbers and stuff)
USE_TZ = True  # Use timezone

# STATIC FILE CONFIGURATION
STATIC_ROOT = normpath(join(PROJECT_ROOT_FOLDER, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    normpath(join(BASE_DIR, 'assets')),
)

# MEDIA_ROOT = normpath(join(PHOTO_ARCHIVE, 'upload'))
MEDIA_ROOT = '/srv/fotoarkiv_universitas'
MEDIA_URL = '/foto/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
# END STATIC FILE CONFIGURATION

# TEMPLATES AND FIXTURES CONFIGURATION
FIXTURE_DIRS = (
    normpath(join(BASE_DIR, 'fixtures')),
)
TEMPLATE_DIRS = (
    normpath(join(BASE_DIR, 'templates')),
)
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.request',
)
# END TEMPLATES AND FIXTURES CONFIGURATION

LOG_FOLDER = normpath(join(PROJECT_ROOT_FOLDER, 'logs'))
