from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer
    )
from apps.items.models import (
    Product,
    ProductImage,
    )

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "product-detail",
        lookup_field = "slug",
        lookup_url_kwarg = "slug",
        )
    image_set = ProductImageSerializer(many=True)
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

