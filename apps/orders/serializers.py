from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer,
    )
from .models import (
    CartItem,
    Order,
)
from apps.ecommerce.serializers import ProductSerializer



class FullCartItemSerializer(HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = "__all__"


class FullOrderSerializer(HyperlinkedModelSerializer):
    items = FullCartItemSerializer(many=True)
    class Meta:
        model = Order
        fields = "__all__"