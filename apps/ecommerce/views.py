from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )
from rest_framework.response import Response
from rest_framework import status
from apps.items.models import Product
from apps.categories.models import Category
from .serializers import ProductSerializer
from .permissions import IsSellerOrReadOnly
from django.http import Http404

# Create your views here.

class ProductListAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, format=None):
        cat = request.query_params.get("cat")
        if not cat:
            products = Product.objects.select_related("seller").filter(visibility="pu")
        else:
            category = Category.objects.prefetch_related("children").get(name=cat)
            if category.children.all().exists():
                sub_categories = category.children.all()
                categories = [category, *[sub_cat for sub_cat in sub_categories]]
                categories=tuple(categories)
                products = Product.objects.select_related("seller").filter(categories__in=categories, visibility="pu")
            else:
                products = Product.objects.select_related("seller").filter(categories=category, visibility="pu")
                
        serializer = ProductSerializer(products, many=True, read_only=True, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save(seller=request.user.customer)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    permission_classes = [IsSellerOrReadOnly, ]
    def get_object(self, slug:str):
        try:
            obj = Product.objects.get(slug=slug)
            self.check_object_permissions(self.request, obj)
            return obj
        except:
            raise Http404("You are not allowed modify this product")
        
    def get(self, request, format=None, *args, **kwargs):
        product = self.get_object(kwargs["slug"])
        if not product.visibility == 'pr' or request.user.customer == product.seller or request.user.is_superuser:
            serializer = ProductSerializer(instance=product, context={"request":request})
            return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={"error":"You are not authorized to see this article"}, status=status.HTTP_401_UNAUTHORIZED)


    
    def patch(self, request, format=None, *args, **kwargs):
        product = self.get_object(kwargs["slug"])
        serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data={"product":serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
    def delete(self, request, format=None, *args, **kwargs):
        product = self.get_object(kwargs["slug"])
        product.delete()
        return Response(data={"data":"deleted"}, status=status.HTTP_200_OK)
