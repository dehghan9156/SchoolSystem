from rest_framework import serializers
from school.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['pk','name','longitude','latitude']

class ClassRoomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role="teacher"),
    )
    teacher_name = serializers.SerializerMethodField()
    class Meta:
        model = ClassRoom
        fields = ["pk","name","teacher","teacher_name"]
    
    def get_teacher_name(self,obj):
        return f"{obj.teacher.name}-{obj.teacher.family}"
    
class AddStudendtSerializer(serializers.Serializer):
    codemeli = serializers.CharField()

    def create(self, validated_data):
        codemeli=validated_data['codemeli']
        user = User.objects.create_user(username=codemeli)
        return user