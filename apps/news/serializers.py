from rest_framework import serializers
from .models import (
    Like,
    Dislike,
    Post,
    PostImage,
    Comment,
)
from apps.accounts.serializers import ShortCustomerSerializer, CustomerSerializer
from apps.categories.serializers import CategorySerializer

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post-detail",
        lookup_field="id",
        lookup_url_kwarg="id"
        )
    user = ShortCustomerSerializer()
    category = CategorySerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"