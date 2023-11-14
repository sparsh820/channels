"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from home.consumers import TestConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Original Django application
django_application = get_asgi_application()

# WebSocket patterns
ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi()),
]

# Combine the Django application and WebSocket patterns
application = ProtocolTypeRouter({
    'http': django_application,
    'websocket': URLRouter(ws_patterns),
})
