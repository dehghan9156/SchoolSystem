from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from chat.models import *


class WebsocketConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def create_chat(self, msg, sender,room_name):
        chatroom,_ = Chatroom.objects.get_or_create(name=room_name)
        sender = self.scope["user"]
        return Message.objects.create(sender=sender, content=msg ,chatroom=chatroom)
    
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
        data = json.loads(text_data)
        message = data['message']

        # await self.create_chat(message,self.room_name)
        # print(self.scope["user"])

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        })) 