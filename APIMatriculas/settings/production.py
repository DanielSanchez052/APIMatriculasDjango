import os
import dj_database_url

from APIMatriculas.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://apimatriculas.herokuapp.com/']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES={}
DATABASES['default']= dj_database_url.config(default=os.environ.get('DATABASE_URL'))


