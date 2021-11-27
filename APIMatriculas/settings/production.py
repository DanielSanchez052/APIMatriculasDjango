import os
import dj_database_url

from APIMatriculas.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['apimatriculas.herokuapp.com']

DATABASES={}

DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))


