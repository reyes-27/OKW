from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )
from rest_framework.response import Response
from rest_framework import status
from apps.items.models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, read_only=True, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
class ProductDetailAPIView(APIView):
    permission_classes=[AllowAny, ]
    def get(self, request, format=None, *args, **kwargs):
        product = Product.objects.get(slug=kwargs["slug"])
        serializer = ProductSerializer(instance=product, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)