from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import FullOrderItemSerializer, FullOrderSerializer
from apps.items.models import Product
from .models import (
    Order,
    OrderItem,
    )
from rest_framework.response import Response

# Create your views here.

class CustomerOrderListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(customer = request.user.customer)
        serializer = FullOrderSerializer(data=orders)
        return Response(data={"orders":serializer.data})
    

