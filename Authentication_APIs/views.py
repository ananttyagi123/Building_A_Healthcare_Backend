from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from rest_framework import permissions

class RegisterView(generics.CreateAPIView):

    "1. this is my registed customised view API to create register user"
    "2. allow user to register with only unique email "
    "3. no duplicates allowed "
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# auth_api/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomLoginView(TokenObtainPairView):
   # "1. Login using email password and get JWT access token"
   # "2. Allow user to login with only email and password"
   #"3. After Login get Access Token for Authorisation of API like Patient , Doctor to access their data"
    #"   and perform CRUD operations "
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

