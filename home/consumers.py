from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from django channels'})) #when we need to send data from backend to frontend

    #when we need data from frontened
    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status':'connected from django channels'}))
        pass

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.room_group_name
        )
    
    def send_notification(self,event):
        print('send notification')
        # print(event)
        print(event.get("value"))
        data=json.loads(event.get("value"))
        self.send(text_data=json.dumps({'payload':data}))
        print('send notification')
