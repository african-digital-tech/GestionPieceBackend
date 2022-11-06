"""
ASGI config for GestionPieceBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestionPieceBackend.settings")

application = get_asgi_application()


ALLOWED_HOSTS = ['*']

SECRET_KEY = '3k2b)luux#bt=bd4g=$6num(qqp@%x$wiv#w8o44e9nm%5rrsr'