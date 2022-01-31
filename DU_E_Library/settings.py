"""
Django settings for DU_E_Library project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['libread.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Blog',
    'Library',
    'rest_framework',
    'cloudinary',
    'widget_tweaks',
    'whitenoise.runserver_nostatic',
    'compressor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'DU_E_Library.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'DU_E_Library.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True

# Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME'),
    'API_KEY': os.getenv('API_KEY'),
    'API_SECRET': os.getenv('API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static')
]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_FINDERS = ['compressor.finders.CompressorFinder']

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

MEDIA_URL = "/media/"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Security
# TODO - SET TO True FOR DEPLOYMENT
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False

# Whitenoise cache policy
WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0

# Django compressor settings
# COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
# COMPRESS_ROOT = os.path.abspath(STATIC_ROOT)
# COMPRESS_ENABLED = os.getenv('COMPRESS_ENABLED')
# COMPRESS_OFFLINE = os.getenv('COMPRESS_OFFLINE')
# COMPRESS_PRECOMPILERS = (
#     ("text/x-sass", "django_libsass.SassCompiler"),
#     ("text/x-scss", "django_libsass.SassCompiler"),
# )
# COMPRESS_FILTERS = {
#     "css": [
#         "compressor.filters.css_default.CssAbsoluteFilter",
#         "compressor.filters.cssmin.rCSSMinFilter",
#     ],
#     "js": ["compressor.filters.jsmin.JSMinFilter"],
# }
# DEBUG_TEMPLATE = False

# Upload size
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100MB
