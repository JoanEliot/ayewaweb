from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&6vr^v=yg0^$-3sts^+e26-**ae1(u@37yu@w0u%l1bco^n8d8'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dav529ipcka40a',
        'USER': 'ynowdoifamdvvj',
        'PASSWORD': 'f3cfd55e7fb521fd57e9ec7eab6f8b6e522b7ddf7809fdf7224864bd139f9071',
        'HOST': 'ec2-35-169-92-231.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
