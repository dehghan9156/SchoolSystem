from rest_framework import serializers
from accounts.models import User


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
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate_codemeli(self,value):
        print(value)
        if len(value) != 10:
            raise serializers.ValidationError({"detail":"codemeli lenght must 10"})
        return value