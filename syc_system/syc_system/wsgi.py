"""
WSGI config for syc_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from syc_system.settings.base import PROJECT_PROFILE
from django.core.wsgi import get_wsgi_application

profile = PROJECT_PROFILE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'syc_system.settings.%s' % profile)

application = get_wsgi_application()
