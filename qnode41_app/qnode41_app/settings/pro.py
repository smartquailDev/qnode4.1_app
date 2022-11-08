from .base import *

DEBUG=  str(os.environ.get('DEBUG')) 



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3')
    }
}

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVIAL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

POSTGRES_READY=str(os.environ.get('POSTGRES_READY_ENV'))=="0"
if DB_IS_AVIAL and POSTGRES_READY:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_DATABASE,
        "USER": DB_USERNAME,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

#Static files DevMod

MEDIA_URL = "/media/"
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
#STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  
#STATIC_ROOT = STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 #Deploy Project- Don`t touch 
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

from .cdn.conf import * #noqa