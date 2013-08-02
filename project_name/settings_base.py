"""Settings common for all environments."""

from os import path

PROJECT_ROOT = path.normpath(path.dirname(__file__))
REPO_ROOT = path.join(PROJECT_ROOT, '..')


#==============================================================================
# Django settings

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = path.join(REPO_ROOT, '..', 'public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = path.join(REPO_ROOT, '..', 'public', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    'django.contrib.admindocs',

    'django_extensions',
    'south',
    'debug_toolbar',
    'pipeline',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DATETIME_FORMAT = 'd.m.y H:i'
DATE_FORMAT = 'd.m.y'


#==============================================================================
# django-autoslug

AUTOSLUG_SLUGIFY_FUNCTION = '{{ project_name }}.slughifi.slughifi'


#==============================================================================
# django-pipeline static compressor

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'lib/pure-base-min.css',
            'lib/pure-buttons-min.css',
            'lib/pure-tables-min.css',
            'lib/pure-menus-min.css',
            'lib/messenger.css',
            'lib/messenger-theme-future.css',
            'lib/ladda.css',

            'css/base.css',
            'css/layout.css',
            'css/components.css',
        ),
        'output_filename': 'css/main.css',
    },
}

PIPELINE_JS = {
    'main': {
        'source_filenames': (
            'lib/underscore.js',
            'lib/yui.js',
            'lib/jquery.js',
            'lib/sprintf.js',
            'lib/ladda.js',
            'lib/messenger.js',
            'lib/messenger-theme-future.js',
            'lib/angular/angular.js',

            'js/app.js',
            'js/config.js',
            'js/utility.js',
            'js/controllers.js',
        ),
        'output_filename': 'js/main.js',
    },
}

# Yuglify can be used, but it requires installation of an npm module
# (see django-pipeline docs)
PIPELINE_JS_COMPRESSOR = None
PIPELINE_CSS_COMPRESSOR = None
