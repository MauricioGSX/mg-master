import os
import sys
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from base.consumers import AppointmentConsumer,AppointmentDetailConsumer

# Add the parent directory to the python path to ensure project modules can be imported correctly 
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

#Set the default django settings module for the ASGI application 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scr.settings')

def get_application():
    """
    Create and return the ASGI application configured with routing for HTTP and WebSocket protocols.

    HTTP:
        - Uses Django's ASGI application wrapped with ASGIStaticFilesHandler to serve static files in development.

    WebSocket:
        - Routes WebSocket connections to consumers with authentication support via AuthMiddlewareStack.
    """
    return ProtocolTypeRouter({
        "http": ASGIStaticFilesHandler(get_asgi_application()), 
        "websocket": AuthMiddlewareStack(
            URLRouter([
                path('ws/appointments/<int:vehicle_id>/', AppointmentConsumer.as_asgi()),
                path('ws/appointment_details/<int:appointment_id>/', AppointmentDetailConsumer.as_asgi()), 
            ])
        ),
    })

application = get_application()