import os
from pathlib import Path
from decouple import config
from unipath import Path as Paths
from dj_database_url import parse as db_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_DECOPLE = Paths(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_@d!&v%0o=az9v32^2ayn&29h7+1w-1pq#pqggzsh%_9hh(-mx'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=True)
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

    'widget_tweaks',
    'bootstrap4',
    'bootstrap_modal_forms',
    'bootstrapform',
    'bootstrap_datepicker_plus',
    'django_filters',
    'django_jsonform',
    'rest_framework',
    'corsheaders',
    'django_extensions',

    'apps.users',
    'apps.core',
    'apps.clientes',
    'apps.produtos',
    'apps.servicos',
    'apps.empresas',
    'apps.orcamentos',
    'apps.dashboard',
    'apps.home',
    'apps.propostas',
    'apps.pix',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vm_acessoria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'vm_acessoria.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR_DECOPLE.child('db.sqlite3'),
        cast=db_url
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

DATE_INPUT_FORMATS = '%d-%m-%Y'
TIME_INPUT_FORMATS = ['%H:%M:%S']

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = False

USE_L10N = True
THOUSAND_SEPARATOR = '.',
USE_THOUSAND_SEPARATOR = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
print(DEBUG)
if DEBUG:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "vm_acessoria/static"),
    ]
    STATIC_ROOT = '/home/ubuntu/vm_acessoria/static/'
    MEDIA_ROOT = '/home/ubuntu/vm_acessoria/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users Backend

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.users.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://localhost:8080"
]