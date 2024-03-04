from django.shortcuts import render
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from typing import TypeVar
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.http import Http404

# Create your views here.

class CustomerProfileDetailView(APIView):
    permission_classes = [AllowAny,]
    def get_object(self, customer_id):
        try:
            obj = Customer.objects.get(id=customer_id)
            return obj
        except:
            raise Http404("Customer does not exist")
    def get(self, request, *args, **kwargs):
        customer = self.get_object(kwargs["id"])
        serializer = CustomerSerializer(customer, context = {'request':request})
        return Response(data={"customer":serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        customer = self.get_object(kwargs["id"])
        serializer = CustomerSerializer(customer, partial=True, data={request.data}, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




