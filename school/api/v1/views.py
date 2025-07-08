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
from .serialization import *
from ...models import *
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsStudentUser,IsTeacherUser
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from rest_framework import filters


class AddSchoolApiView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class= AddSchoolSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New School Add Successfully."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AddClassRoomApiView(generics.GenericAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes =[IsAdminUser]
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages":"classroom add successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AddStudentApiView(generics.GenericAPIView):
    permission_classes =[IsTeacherUser]
    serializer_class = AddStudendtSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"student add successfully."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AddNewsApiView(generics.ListCreateAPIView):
    permission_classes =[IsTeacherUser]
    serializer_class = NewsSerializer
    queryset = News.objects.all()

class AddExerciseApiView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    permission_classes = [IsTeacherUser]

class EditExerciseApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsTeacherUser]
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        exercise = Exercise.objects.filter(created_by=self.request.user)    
        return exercise

class EditNewsApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsTeacherUser]
    serializer_class =NewsSerializer
    def get_queryset(self):
        news = News.objects.filter(created_by=self.request.user)
        return news

class ReviewsNewsApiView(APIView):
    permission_classes = [IsStudentUser]
    
    def get(self,request):
        user = request.user
        classroom_ids = ClassRoom_Student.objects.filter(student=user).values_list("classroom_id",flat=True)
        teacher_ids = ClassRoom.objects.filter(pk__in=classroom_ids).values_list("teacher_id",flat=True)
        news = News.objects.filter(created_by__in=teacher_ids,classroom_id__in=classroom_ids)
        serializer = NewsSerializer(news,many=True)
        return Response(serializer.data)

class ReviewsExerciseApiView(APIView):
    permission_classes =[IsStudentUser]
    
    def get(self,request):
        user = request.user
        classroom_ids = ClassRoom_Student.objects.filter(student=user).values_list("classroom_id",flat=True)
        teacher_ids = ClassRoom.objects.filter(pk__in=classroom_ids).values_list("teacher_id",flat=True)
        exercise = Exercise.objects.filter(created_by__in=teacher_ids,classroom__in=classroom_ids)
        
        serializer = ExerciseSerializer(exercise,many=True)
        return Response(serializer.data)

class SendExerciseApiView(generics.GenericAPIView):
    permission_classes = [IsStudentUser]
    serializer_class = AnswerExerciseSerializer
    def post(self,request,pk):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            exercise = Exercise.objects.get(pk=pk)
            AnswerExercise.objects.create(exercise=exercise,student=request.user)
            return Response({"message":"answerexercise upload success."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EditAnswerExercise(generics.GenericAPIView):
    serializer_class = AnswerExerciseSerializer
    permission_classes=[IsStudentUser]
    def put(self,request,pk):
        answerexercise = AnswerExercise.objects.get(pk=pk)
        exercise  = answerexercise.exercise
        deadline = exercise.deadline
        current_time = timezone.now()
        if current_time>deadline:
            return Response({"message":"sorry.you can not upload you answer because the time has passed"})
        serializer = self.serializer_class(answerexercise,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"you answerexercise successfully edited."},status=status.HTTP_200_OK)

class FullAccessNewApiView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes =[IsAdminUser]
    serializer_class = NewsSerializer
    filter_backends =[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_fields = ["lesson","classroom","created_by"]
    search_fields = ["id","lesson__name","classroom__name","created_by__username"]
    ordering_fields = ["id","lessonــname","classroom__name","created_by__username"]

class FullAccessExerciseApiView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    permission_classes =[IsAdminUser]
    serializer_class =ExerciseSerializer
    filter_backends =[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_fields = ["lesson","classroom","created_by"]
    search_fields = ["id","lesson__name","classroom__name","created_by__username"]
    ordering_fields = ["id","lessonــname","classroom__name","created_by__username"]
