from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
import json
from .models import ChatGroup, GroupMessage
from django.contrib.auth.models import User

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']  
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)

        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name, self.channel_name
        )

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            author_username = text_data_json.get('author')

            if not author_username:
                raise ValueError("Missing 'author' in received data.")

            user = User.objects.get(username=author_username)

            if 'file_url' in text_data_json:
                file_url = text_data_json['file_url']

                # Only send the file URL to the group once
                async_to_sync(self.channel_layer.group_send)(
                    self.chatroom_name,
                    {
                        'type': 'message_handler',
                        'file_url': file_url,
                        'author': user.username,
                    }
                )
            
            elif 'body' in text_data_json:
                body = text_data_json['body']
                message = GroupMessage.objects.create(
                    body=body,
                    author=user,
                    group=self.chatroom
                )
                async_to_sync(self.channel_layer.group_send)(
                    self.chatroom_name,
                    {
                        'type': 'message_handler',
                        'body': message.body,
                        'author': message.author.username,
                    }
                )
        except Exception as e:
            self.send(text_data=json.dumps({'error': str(e)}))

    def message_handler(self, event):
        response_data = {}

        if 'file_url' in event:
            response_data['file_url'] = event['file_url']
        
        if 'body' in event:
            response_data['body'] = event['body']

        response_data['author'] = event.get('author')

        self.send(text_data=json.dumps(response_data))
