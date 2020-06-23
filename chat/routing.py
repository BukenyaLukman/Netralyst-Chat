from django.urls import re_path,path
from django.conf.urls import url
from .consumers import ChatConsumer
from .import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/',ChatConsumer),
    ##path('ws/chat/<str:room_name>/', consumers.ChatConsumer),
]