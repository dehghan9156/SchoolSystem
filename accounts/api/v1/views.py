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
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView,GenericAPIView
from .serialization import *
from ...models import *
from drf_yasg.utils import swagger_auto_schema


class UserRegisterApiView(APIView):
    # @swagger_auto_schema(request_body=TeacherSerializer)
    def post(self,request,role):
        if role == "teacher":
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.create_user(
                    name = serializer.validated_data['name'],
                    family = serializer.validated_data['family'],
                    codemeli = serializer.validated_data['codemeli'],
                    username = serializer.validated_data['username'],
                    password = serializer.validated_data['password'],
                    role = role
                )
                return Response({"message":"user register successfully."},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        if role == 'student':
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.create_user(
                    name = serializer.validated_data['name'],
                    family = serializer.validated_data['family'],
                    codemeli = serializer.validated_data['codemeli'],
                    password = serializer.validated_data['password'],
                    role = role
                )
                return Response({"message":"user register successfully."},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
