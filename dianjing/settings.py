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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, 'upload')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rgmth63^*at+bt=xh9uqtu9ndv@s*0z54-990yg3-!v8$m0t-1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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

    'anymail',
    'duckadmin',
    'apps.helper',
    'apps.server',
    'apps.account',
    'apps.character',
    'apps.config',
    'apps.statistics',
    'apps.history_record',
    'apps.purchase',
    'apps.game',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'dianjing.middleware.LazyMiddleware',
    'dianjing.middleware.RequestMiddleware',
    'dianjing.middleware.LoginIDMiddleware',
    'dianjing.middleware.ResponseMiddleware',
    'dianjing.middleware.ExceptionMiddleware',
]

ROOT_URLCONF = 'dianjing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

LANGUAGE_CODE = 'zh-hans'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = UPLOAD_DIR

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
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
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
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
}


TIME_ZONE = doc.find('timezone').text

DUTY_SERVER_MIN = int( doc.find('duty-server/min').text )
DUTY_SERVER_MAX = int( doc.find('duty-server/max').text )

SOCKET_SERVERS = []
for _s in doc.find('sockets').getchildren():
    attrib = _s.attrib
    attrib['http'] = int(attrib['http'])
    attrib['tcp'] = int(attrib['tcp'])
    SOCKET_SERVERS.append(attrib)

AES_KEY = doc.find('crypto/key').text
AES_CBC_IV = doc.find('crypto/iv').text

REDIS_HOST = doc.find('redis/host').text
REDIS_PORT = int( doc.find('redis/port').text )

MONGODB = []
for _m in doc.find('mongodb').getchildren():
    attrib = _m.attrib
    attrib['port'] = int(attrib['port'])
    attrib['sid-min'] = int(attrib['sid-min'])
    attrib['sid-max'] = int(attrib['sid-max'])
    MONGODB.append(attrib)

# MAILGUN
ANYMAIL = {
    'MAILGUN_API_KEY': doc.find('mailgun/key').text
}
SERVER_EMAIL = "{0} <{0}@{1}>".format(doc.find('mailgun/sender').text, doc.find('mailgun/domain').text)
EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
EMAIL_SUBJECT_PREFIX = "[DianJing]"

_config_admins = doc.find('admins')
ADMINS = ()
for _admin in _config_admins.getchildren():
    ADMINS += ((_admin.attrib['name'], _admin.attrib['email']), )

del _config_admins
del doc
del tree
del et
