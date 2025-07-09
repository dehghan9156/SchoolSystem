from rest_framework import serializers
from accounts.models import User
from django.urls import reverse

class TeacherSerializer(serializers.ModelSerializer):
    # role = serializers.ChoiceField(choices=User.Roel_User)
    password_confirm = serializers.CharField()
    class Meta:
        model = User
        fields = ['pk','username','name','family','codemeli','password','password_confirm']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm') # Remove confirmation field
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate_codemeli(self,value):
        print(value)
        if len(value) != 10:
            raise serializers.ValidationError({"detail":"codemeli lenght must 10"})
        return value
    
class StudentSerializer(serializers.ModelSerializer):    
    password_confirm = serializers.CharField()
    class Meta:
        model = User
        fields = ['pk','name','family','codemeli','password','password_confirm']
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm') # Remove confirmation field
        validated_data['codemeli']=validated_data['username']
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate_codemeli(self,value):
        print(value)
        if len(value) != 10:
            raise serializers.ValidationError({"detail":"codemeli lenght must 10"})
        return value

class TeacherLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class StudentLoginSerializer(serializers.Serializer):
    codemeli = serializers.CharField()
    password = serializers.CharField(write_only = True)

class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    confirm_url = serializers.SerializerMethodField(source="get_confirm_url")
    class Meta:
        model = User
        fields = ["pk","username","name","family","codemeli","biography","longitude","latitude","role","confirmation","confirm_url"]
        read_only_fields =["role","confirmation","confirm_url"]

    def get_confirm_url(self,obj):
        return reverse("accounts:api-v1:user-confirm",args=[obj.pk])