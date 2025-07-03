from rest_framework import serializers
from school.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class ScoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['pk','name','longitude','latitude']

class ClassRoomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role="teacher")
    )
    teacher_name = serializers.SerializerMethodField()
    class Meta:
        model = ClassRoom
        fields = ["pk","name","teacher","teacher_name"]
    
