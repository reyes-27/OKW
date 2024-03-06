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
from django.urls import reverse

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="post-detail",
        lookup_field="id",
        lookup_url_kwarg="id"
        )
    def get_user_dislikes(self, instance):
        is_list_view = self.context["request"].path == "/api/posts/"
        if is_list_view:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}/{self.context["request"].path}{instance.id}/dislikes/'
        else:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}/{self.context["request"].path}dislikes/'
        return absolute_url
    
    def get_user_likes(self, instance):
        is_list_view = self.context["request"].path == "/api/posts/"
        if is_list_view:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}/{self.context["request"].path}{instance.id}likes/'
        else:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}/{self.context["request"].path}likes/'

        return absolute_url
    
    user = ShortCustomerSerializer()
    category = CategorySerializer(many=True)
    user_dislikes = serializers.SerializerMethodField()
    user_likes = serializers.SerializerMethodField()
    # user_dislikes = DislikeSerializer(source="posts_dislikes", many=True, read_only=True)
    # user_likes = LikeSerializer(source="posts_likes", many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        # exclude = [
        #     # "user_dislikes",
        #     "user_likes",
        #     ]