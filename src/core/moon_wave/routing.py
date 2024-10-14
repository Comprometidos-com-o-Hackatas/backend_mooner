from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/moon_wave/(?P<room_name>\w+)/$", consumers.MoonWaveConsumer.as_asgi()),
]