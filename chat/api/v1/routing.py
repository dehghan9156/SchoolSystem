# chat/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^chat/api/v1/ws/chat/(?P<room_name>\w+)/$', consumers.WebsocketConsumer.as_asgi()),
]