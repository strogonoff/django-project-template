"""Local settings specific to particular environment. Not version-controlled."""

from settings_base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ()

ALLOWED_HOSTS = [
    '{{ project_name }}.com.',
    'www.{{ project_name }}.com.',
]

ADMINS = (
    # ("your name", "your email"),
)
MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DISABLED_APPS = [
    # Each app name listed here will be excluded from INSTALLED_APPS
    # 'debug_toolbar',
]

DISABLED_MIDDLEWARE = [
    # If a string listed here is encountered in middleware class path,
    # that entry will be excluded from MIDDLEWARE_CLASSES
    # 'debug_toolbar',
]

SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = [
    app for app in INSTALLED_APPS
    if app not in DISABLED_APPS]

MIDDLEWARE_CLASSES = [
    cls for cls in MIDDLEWARE_CLASSES
    if all([_dm not in cls for _dm in DISABLED_MIDDLEWARE])]
