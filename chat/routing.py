# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]
""" 
#burada web socket olarak tanımladık
#maksat mesajlar HTTP olarak değilde
#Direkt karşıya gitsin için.
"""