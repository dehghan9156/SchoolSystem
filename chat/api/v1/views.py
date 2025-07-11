from http.client import responses
from django.conf import settings
from django.core.serializers import serialize
from django.db.models.fields import return_None
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import CreateAPIView,GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from ...models import *
from school.api.v1.permissions import *
from .serialization import *
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from rest_framework import filters


class GetMessageApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,room_id):
        messages = Message.objects.filter(chatroom_id=room_id)
        data = [{'sender': msg.sender.username, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]
        return Response(data)

class GetMessageTeacherApiView(generics.ListAPIView):
    permission_classes =[IsTeacherUser]
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_fields = ["sender","reciver","chatroom","chatroom"]
    search_fields = ["sender__username","reciver__username","chatroom__name","timestamp"]
    ordering_fields = ["sender__username","reciver__username","chatroom__name","timestamp"]
        
    def get_queryset(self):
        user = self.request.user
        messages = Message.objects.filter(Q(sender=user) | Q(reciver=user))
        return messages


   