import os
import dj_database_url

from APIMatriculas.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG',False)
ALLOWED_HOSTS = ['apimatriculas.herokuapp.com','https://apimatriculas.herokuapp.com/', 'localhost', '127.0.0.1']

DATABASES={}

DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))


