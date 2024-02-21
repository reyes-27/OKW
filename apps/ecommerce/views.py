from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )
from rest_framework.response import Response
from rest_framework import status
from apps.items.models import Product
from .serializers import ProductSerializer
from django.http import Http404
# Create your views here.

class ProductListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, read_only=True, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProductDetailAPIView(APIView):
    permission_classes=[AllowAny, ]
    def get_object(self, slug:str):
        try:
            obj = Product.objects.get(slug=slug)
            return obj
        except:
            raise Http404("Product does not exist.")
        
    def get(self, request, format=None, *args, **kwargs):
        product = self.get_object(kwargs["slug"])
        serializer = ProductSerializer(instance=product, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, format=None, *args, **kwargs):
        product = self.get_object(kwargs["slug"])
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"product":serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
