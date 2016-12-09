"""
WSGI config for aroomie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aroomie.settings")

application = get_wsgi_application()

# Use whitenoise package to serve static files on Heroku
# pass the application to the DjangoWhiteNoise
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
