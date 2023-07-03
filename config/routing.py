from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from app.consumers import TaxiConsumer
from config.middleware import TokenAuthMiddlewareStack


application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('config/',TaxiConsumer),
        ])
    )
})
