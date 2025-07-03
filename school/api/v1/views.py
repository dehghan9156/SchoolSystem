from http.client import responses
from django.conf import settings
from django.core.serializers import serialize
from django.db.models.fields import return_None
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import CreateAPIView,GenericAPIView
from .serialization import *
from ...models import *
from drf_yasg.utils import swagger_auto_schema

class AddSchoolApiView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(request_body=ScoolSerializer)
    def post(self,request):
        serializer = ScoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New School Add Successfully."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AddClassRoomApiView(generics.GenericAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages":"classroom add successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)