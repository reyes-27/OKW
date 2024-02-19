from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    )
from .models import (
    OrderItem,
    Order,
)

class OrderItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem