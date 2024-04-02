from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import FullCartItemSerializer, FullCartSerializer
from apps.items.models import Product
from .models import (
    Order,
    CartItem,
    Cart,
    )
from rest_framework.response import Response

# Create your views here.
#ASYNC
class CustomerCartAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(customer = request.user.customer).first()
        serializer = FullCartSerializer(instance=cart, context={"request":request})
        return Response(data={"cart":serializer.data})
    
#ASYNC
class CustomerOrderListAPIView(APIView):
    pass

class CustomerOrderDetailAPIView(APIView):
    pass