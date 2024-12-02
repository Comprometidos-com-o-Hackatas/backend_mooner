import json
import re

from channels.generic.websocket import AsyncWebsocketConsumer

class MoonWaveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        original_room_name = self.scope["url_route"]["kwargs"]["room_name"]

        self.room_group_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", original_room_name)

        print(original_room_name, self.room_group_name)
         # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            data_json = json.loads(text_data)
            song = data_json.get('song', None)
            action = data_json.get('action', None)
            timestamp = data_json.get('timestamp', None)
            queue = data_json.get('queue', None)

            await self.channel_layer.group_send(
                self.room_group_name, {"type": "moon_wave_message", "action": action, "timestamp": timestamp, "song": song, "queue": queue}
            )

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")

    async def moon_wave_message(self, event):
        action = event["action"]
        timestamp = event["timestamp"]
        song = event["song"]
        queue = event["queue"]


        await self.send(text_data=json.dumps({'action': action, 'timestamp': timestamp, 'song': song, 'queue': queue}))
