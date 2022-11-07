from .settings import *
import dj_database_url


DEBUG = False
DEBUG_TEMPLATE = False

ALLOWED_HOSTS = ['backend-piece.herokuapp.com']


DATABASES['default'] = dj_database_url.config()

MIDDLEWARE = [
   
    "whitenoise.middleware.WhiteNoiseMiddleware"
]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
