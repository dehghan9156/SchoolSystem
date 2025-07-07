from rest_framework import serializers
from school.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class AddSchoolSerializer(serializers.Serializer):
    name = serializers.CharField()
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    teacher_id = serializers.IntegerField()

    def validate_teacher_id(self, value):
        teacher_id = User.objects.filter(id=value,role="teacher")
        if not teacher_id.exists():
            raise serializers.ValidationError("tecaher not found")
        return value


    def create(self, validated_data):
        teacher_id = validated_data.pop("teacher_id")
        teacher = User.objects.get(pk=teacher_id)
        school = School.objects.create(**validated_data)
        teacher_school = Teacher_School.objects.create(teacher=teacher,school=school)
        return school
 

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
        user = User.objects.create_user(username=codemeli,codemeli=codemeli,role="student")
        return user

class NewsSerializer(serializers.ModelSerializer):
    lesson = serializers.SlugRelatedField(queryset=Lesson.objects.all(),slug_field="name")
    classroom = serializers.SlugRelatedField(queryset=ClassRoom.objects.all(),slug_field="name")
    class Meta:
        model = News
        fields =["pk","title","text","lesson","classroom"]
    
    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["created_by"] = user
        return super().create(validated_data)
    
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["pk","title","content","deadline","file","lesson","classroom"]
    
    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["created_by"]=user
        return super().create(validated_data)
