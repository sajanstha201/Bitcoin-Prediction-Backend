from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
class Register_serializers(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    firstname=serializers.CharField()
    lastname=serializers.CharField()
    def validate(self, obj):
        if (User.objects.all().filter(username=obj['username'])).exists():
            raise ValidationError("User Already Exit")
        if (User.objects.all().filter(email=obj['email']).exists()):
            raise ValidationError("Email Already Exist")
        return obj
    def create(self,obj):
        instance=User.objects.create_user(username=obj['username'],email=obj['email'],password=obj['password'],first_name=obj['firstname'],last_name=obj['lastname'])
        Token.objects.create(user=instance)
        return instance
        
class Login_serializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class User_serializer(serializers.Serializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
            