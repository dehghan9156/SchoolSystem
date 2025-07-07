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
 

class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField()
    teacher_id = serializers.IntegerField()
    school_id = serializers.IntegerField()
    
    def validate_teacher_id(self, value):
        teacher_id = User.objects.filter(pk=value,role="teacher")
        if not teacher_id.exists():
            raise serializers.ValidationError("teacher not found")
        return value
    
    def validate_school_id(self,value):
        school_id = School.objects.filter(pk=value)
        if not school_id.exists():
            raise serializers.ValidationError("school not found")
        return value
    
    def create(self, validated_data):
        teacher_id = validated_data.pop("teacher_id")
        school_id = validated_data.pop("school_id")
        teacher = User.objects.get(pk=teacher_id)
        school = School.objects.get(pk=school_id)
        classroom=ClassRoom.objects.create(teacher=teacher,school=school,**validated_data)
        return classroom

class AddStudendtSerializer(serializers.Serializer):
    codemeli = serializers.CharField()
    classroom_id = serializers.IntegerField()
    lesson_id = serializers.IntegerField()

    def create(self, validated_data):
        classroom_id = validated_data.pop("classroom_id")
        lesson_id = validated_data.pop("lesson_id")
        
        classroom = ClassRoom.objects.get(pk=classroom_id)
        lesson = Lesson.objects.get(pk=lesson_id)
        
        codemeli=validated_data['codemeli']
        
        user = User.objects.create_user(username=codemeli,codemeli=codemeli,role="student")

        student_lesson = Studen_Lesson.objects.create(student=user,lesson=lesson)
        classroom_student = ClassRoom_Student.objects.create(student=user,classroom=classroom)
        
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
