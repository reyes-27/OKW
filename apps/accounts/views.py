from django.shortcuts import render
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from typing import TypeVar
from django.contrib.auth import get_user_model
from .models import TokenUser

# Create your views here.


