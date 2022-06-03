"""
WSGI config for send_message_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from threading import Thread
from send_message_app.views import send_messages


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_message_proj.settings')

application = get_wsgi_application()


thread = Thread(target=send_messages)
thread.start()




