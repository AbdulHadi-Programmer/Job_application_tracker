"""
Django settings for job_application_tracker project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# LOGIN_URL = 'login'

# LOGIN_URL = '/auth/login/'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/auth/login/'

LOGIN_URL = '/login/'


SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default session engine
SESSION_COOKIE_AGE = 1209600  # Two weeks (in seconds)

# AUTH_USER_MODEL = 'tracker.User'  # Adjust according to your app name and model name
# AUTH_USER_MODEL = 'tracker.CustomUser'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*zy$9ahx^-q$fp9fb#m-_%g0fozpv(f(r1u!#n-9h7j-*=b-wa'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# settings.py

# Static Files Configuration for Deployment
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']  # If you have a 'static' folder in your project

# ALLOWED_HOSTS = ['careertraces.pythonanywhere.com', 'www.careertraces.com']
ALLOWED_HOSTS = ["*"] 

# X_FRAME_OPTIONS = 'ALLOWALL'


INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'tracker', 
    'corsheaders', 
    'authentication', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line here
]

# Static Files Caching
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'job_application_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # This is written to set the template folder
        # 'DIRS': [BASE_DIR / 'templates'], # This is written to set the template folder
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

WSGI_APPLICATION = 'job_application_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        # 'NAME': BASE_DIR / '/job_application_tracker/db.sqlite3',
        'OPTIONS': {
            'timeout': 20,  # Increase timeout to 20 seconds
        },
    }
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

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_TZ = True


# python decouple library is perfectly working and it is used to get and store .env var so we can keep our api aur secret key even more secure
# from decouple import config
from dotenv import load_dotenv
import os

load_dotenv()
# load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'reamde/.env'))  # Adjust path as needed
# print(os.path.join(BASE_DIR, 'readme/.env'))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')