from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer,
    )
from .models import (
    OrderItem,
    Order,
)
from apps.ecommerce.serializers import ProductSerializer



class FullOrderItemSerializer(HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = "__all__"


class FullOrderSerializer(HyperlinkedModelSerializer):
    items = FullOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = "__all__"