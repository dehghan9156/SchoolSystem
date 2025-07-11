from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from chat.models import *


class WebsocketConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print("recive message")
        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        print(user,room_name)
        await self.save_message(user,room_name,message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user' :user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
        })) 

    @database_sync_to_async
    def save_message(self, sender, room_name, msg):
        chatroom, _ = Chatroom.objects.get_or_create(name=room_name)
        Message.objects.create(sender=sender, content=msg, chatroom=chatroom)
