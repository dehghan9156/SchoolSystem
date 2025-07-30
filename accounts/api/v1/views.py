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
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.exceptions import TokenError
from school.api.v1.permissions import *
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import Group



class UserRegisterApiView(generics.GenericAPIView):
    def get_serializer_class(self):
         if self.kwargs.get("role")=="teacher":
              return TeacherSerializer
         return StudentSerializer
    
    def post(self,request,role):
        serializer_class = self.get_serializer_class()
        print(serializer_class)
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            if role == "teacher":
                user = User.objects.create_user(
                    name = serializer.validated_data['name'],
                    family = serializer.validated_data['family'],
                    codemeli = serializer.validated_data['codemeli'],
                    username = serializer.validated_data['username'],
                    password = serializer.validated_data['password'],
                    role = role
                )
                group,_ = Group.objects.get_or_create(name="Teachers")
                user.groups.add(group)
                
                # assign_perm("is_teacher",group)
                print("group add")
                user.save()
                return Response({"message":"user register successfully."},status=status.HTTP_200_OK)
                    
            elif role == 'student':
                user = User.objects.create_user(
                    name = serializer.validated_data['name'],
                    family = serializer.validated_data['family'],
                    username = serializer.validated_data['codemeli'],
                    codemeli = serializer.validated_data['codemeli'],
                    password = serializer.validated_data['password'],
                    role = role
                )
                group,_ = Group.objects.get_or_create(name="Students")
                user.groups.add(group)
                # assign_perm("is_student",group)
                user.save()
                return Response({"message":"user register successfully."},status=status.HTTP_200_OK)

            else:
                return Response({"message":"can not register"})

        else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginApiView(generics.GenericAPIView):
    def get_serializer_class(self):
        role = self.kwargs.get("role")
        if role == "teacher" or role=="admin":
            return TeacherLoginSerializer
        return StudentLoginSerializer

    def post(self,request,role):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            if role=="admin" or role=="teacher":
                username = serializer.validated_data['username']
                password = serializer.validated_data['password']
            elif role=="student":
                username = serializer.validated_data["codemeli"]
                password = serializer.validated_data["password"]
            else :
                return Response({"message":"you can not login the system"},status=status.HTTP_400_BAD_REQUEST)  
    
            user = authenticate(request, username=username, password=password)
            if user :
                refresh = RefreshToken.for_user(user)
                return Response ({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username':user.username,
                    'role':user.role,
                    'message':'user login successfully.',                    
                },status=status.HTTP_200_OK)
            return Response({"message":"username or password not correct"},status=status.HTTP_400_BAD_REQUEST)
              
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLogoutApiView(APIView):
    permission_classes =[IsAuthenticated]
    @swagger_auto_schema(request_body=UserLogoutSerializer)
    def post(self,request):
        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid():     
            refresh_token = serializer.validated_data.get("refresh")
            token = RefreshToken(refresh_token)
            try:
                token.blacklist()
                return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
            except TokenError:
                return Response({"message":"token already blocked"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EditProfileApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    
    def put(self,request):
        user = self.get_object()
        serializer = self.serializer_class(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"your profile edit successfully."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GetUsersApiView(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        users = User.objects.filter(role__in=["teacher","student"])
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)


class UserConfirmApiView(APIView):
    def patch(self,request,pk):
        user = User.objects.get(pk=pk)
        user.confirmation = not user.confirmation        
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)