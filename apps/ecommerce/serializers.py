from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer,
    )
from apps.items.models import (
    Product,
    ProductImage,
    )
from apps.accounts.serializers import ShortCustomerSerializer
class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            "image",
            "level",
        ]

class ProductSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "product-detail",
        lookup_field = "slug",
        lookup_url_kwarg = "slug",
        )
    image_set = ProductImageSerializer(many=True)
    seller = ShortCustomerSerializer()

    class Meta:
        model = Product
        fields = "__all__"
        # fields = [
        #     "url",
        #     "name",
        #     "description",
        #     "stock",
        #     "rate",
        # ]

