from .base import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = dict() #Heroku config

#DATABASES['default'] = dj_database_url.config() #Heroku config

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https') #Heroku config

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': os.getenv("DB_NAME"),
       'USER': os.getenv("DB_USER"),
       'PASSWORD': os.getenv("DB_PASSWORD"),
       'HOST': 'localhost',
       'PORT': '5432'
   }
}

STATIC_ROOT = os.path.join(os.getcwd(), 'static')