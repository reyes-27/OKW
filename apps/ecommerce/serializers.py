from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer,
    )
from apps.items.models import (
    Product,
    ProductImage,
    )
from apps.categories.serializers import CategorySerializer
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
    image_set = ProductImageSerializer(many=True, read_only=True)
    seller = ShortCustomerSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)

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

