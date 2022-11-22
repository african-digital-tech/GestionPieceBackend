from .settings import *
import dj_database_url


DEBUG = False
DEBUG_TEMPLATE = False

ALLOWED_HOSTS = ['backend-piece.herokuapp.com']


DATABASES['default'] = dj_database_url.config()

SECRET_KEY = "yl$&cyx^ogn7e+1l0n8dh!9nd&wpyuw_l8t_^d!138we87u3o7"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware"
]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
