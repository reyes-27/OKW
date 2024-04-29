from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer,
    )
from .models import (
    CartItem,
    Order,
    Cart,
)
from apps.ecommerce.serializers import ProductSerializer
from apps.accounts.serializers import CustomerSerializer

class FullCartItemSerializer(ModelSerializer):

    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = "__all__"


class FullCartSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "cart-detail",
        lookup_field = "id",
        lookup_url_kwarg = "id",
        )
    customer = CustomerSerializer()
    items = FullCartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = "__all__"

class ShortCartSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "cart-detail",
        lookup_field = "id",
        lookup_url_kwarg = "id",
        )
    class Meta:
        model = Cart
        exclude = ["customer"]

# class ShortCartSerializer()

class OrderSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="order-detail",
        lookup_field="id",
        lookup_url_kwarg="id"
        )
    customer = CustomerSerializer()
    cart = ShortCartSerializer(read_only=True)
    class Meta:
        model = Order 
        fields = "__all__"