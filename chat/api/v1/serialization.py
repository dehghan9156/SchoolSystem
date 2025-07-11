from rest_framework import serializers
from chat.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields =["pk","sender","reciver","content","chatroom","timestamp"]