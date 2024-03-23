from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Register_serializers,Login_serializer,User_serializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
class Register(APIView):
    def post(self,request):
        register_serializer=Register_serializers(data=request.data)
        if(register_serializer.is_valid()):
            register_serializer.create(register_serializer.data)
            return Response({'detail':'success'})
        else:
            return Response({'detail':'fail','error':register_serializer.errors})
        
          
class Login(APIView):
    def post(self,request):
        data=request.data
        login_serializer=Login_serializer(data=request.data)
        if not login_serializer.is_valid():
            return Response({'detail':'fail','message':'Invalid Input'})
        user=authenticate(username=login_serializer.validated_data['username'],
                          password=login_serializer.validated_data['password'])
        if(not user):
            return Response({'detail':'fail','message':'Wrong Password or Username'})
        token,created=Token.objects.get_or_create(user=user)
        obj=User.objects.get(username=data['username'])
        serialized_data=User_serializer(obj)
        return Response({'detail':'success','token':str(token),'user_data':serialized_data.data})
    
    
    
    
    
    
class getUserDetail(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            print("sajan shrestha")
            print(request.user)
            if not request.user.is_authenticated:
                return Response({'detail':'fail','message':'authentication fail'})
            user=request.user
            print(user)
            return Response({'detail':'success','message':'authentication successful','name':user.username})
        except AuthenticationFailed as e:
            return Response({'detail':'fail','message':'authentication fail','error':str(e)})
        
        
