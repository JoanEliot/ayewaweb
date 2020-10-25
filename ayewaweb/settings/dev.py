from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# load heroku settings
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


try:
    from .local import *
except ImportError:
    pass

