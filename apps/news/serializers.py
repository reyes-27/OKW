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

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = [
            "id",
            "image",
            "level",
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = [
            "user_likes"
        ]
class PostSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="post-detail",
        lookup_field="id",
        lookup_url_kwarg="id"
        )
    def get_user_dislikes(self, instance):
        is_list_view = self.context["request"].path == "/api/posts/"
        if is_list_view:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}{self.context["request"].path}{instance.id}/dislikes/'
        else:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}{self.context["request"].path}dislikes/'
        return absolute_url
    
    def get_user_likes(self, instance):
        is_list_view = self.context["request"].path == "/api/posts/"
        if is_list_view:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}{self.context["request"].path}{instance.id}/likes/'
        else:
            absolute_url = f'{self.context["request"].build_absolute_uri('/')[:-1]}{self.context["request"].path}likes/'

        return absolute_url
    
    def get_comments(self, instance):
        is_list_view = self.context["request"].path == "/api/posts/"
        if is_list_view:
            #If is list view, only the three most liked comments will be shown
            comments = instance.comments.filter(parent=None)[:3]
            return CommentSerializer(comments, many=True).data
        else:
            #Otherwise paginated comments
            comments = f'{self.context["request"].build_absolute_uri('/')[:-1]}{self.context["request"].path}comments/'
            return comments

    user = ShortCustomerSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    user_dislikes = serializers.SerializerMethodField(read_only=True)
    user_likes = serializers.SerializerMethodField(read_only=True)
    image_set = PostImageSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
