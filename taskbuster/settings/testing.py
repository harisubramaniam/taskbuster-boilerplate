# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'tasker',
        'PASSWORD': 'task3r',
        'HOST': '',
        'PORT': '',
    }
}