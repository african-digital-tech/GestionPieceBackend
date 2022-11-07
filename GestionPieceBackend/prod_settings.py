from .settings import *
import dj_database_url


DEBUG = False
DEBUG_TEMPLATE = False

ALLOWED_HOSTS = ['backend-piece.herokuapp.com']

SECRET_KEY = 'yl$&cyx^ogn7e+1l0n8dh!9nd&wpyuw_l8t_^d!138we87u3o7'

DATABASES = dj_database_url.config()
