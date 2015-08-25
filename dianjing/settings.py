"""
Django settings for dianjing project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
TEST = os.environ.get('DIANJING_TEST', '0') == '1'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rgmth63^*at+bt=xh9uqtu9ndv@s*0z54-990yg3-!v8$m0t-1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = '*'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.helper',
    'apps.server',
    'apps.account',
    'apps.character',
    'background',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dianjing.middleware.GameRequestMiddleware',
    'dianjing.middleware.GameResponseMiddleware',
    'dianjing.middleware.GameExceptionMiddleware',
)

ROOT_URLCONF = 'dianjing.urls'

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

WSGI_APPLICATION = 'dianjing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': [],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


if not DEBUG:
    LOGGING['loggers']['django.request']['handlers'].extend(['console', 'mail_admins'])

LOG_PATH = os.path.join(BASE_DIR, 'logs')

DATETIME_FORMAT = "Y-m-d H:i:s"


# project config
import xml.etree.ElementTree as et
tree = et.ElementTree(file=os.path.join(BASE_DIR, 'settings.xml'))
doc = tree.getroot()

MYSQL_HOST = doc.find('mysql/host').text
MYSQL_PORT = int( doc.find('mysql/port').text )
MYSQL_DATABASE = doc.find('mysql/database').text
MYSQL_USER = doc.find('mysql/user').text
MYSQL_PASSWORD = doc.find('mysql/password').text


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  MYSQL_DATABASE,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
        'CONN_MAX_AGE': 0,
    },
}


TIME_ZONE = doc.find('timezone').text


AES_KEY = doc.find('crypto/key').text
AES_CBC_IV = doc.find('crypto/iv').text

REDIS_HOST = doc.find('redis/host').text
REDIS_PORT = int( doc.find('redis/port').text )
REDIS_CACHE_SECONDS = int( doc.find('redis/cache-seconds').text )

del doc
del tree
del et
