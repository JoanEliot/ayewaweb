from .base import *

DEBUG = False

# load heroku settings
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

try:
    from .local import *
except ImportError:
    pass
