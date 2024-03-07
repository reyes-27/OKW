from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Post,
    Like,
    Dislike,
    Comment,
    )
from .serializers import (
    PostSerializer,
    LikeSerializer,
    DislikeSerializer,
    CommentSerializer,
    )

# Create your views here.

class PostListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
class PostDetailAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get_object(self, post_id):
        obj = Post.objects.get(id=post_id)
        return obj
    
    def get(self, request, *args, **kwargs):
        post = self.get_object(kwargs["id"])
        serializer = PostSerializer(post, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)

class LikeListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        likes = Like.objects.filter(post=kwargs["id"])
        serializer = LikeSerializer(likes, many=True)
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    
class DislikeListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        dislikes = Dislike.objects.filter(post=kwargs["id"])
        serializer = DislikeSerializer(dislikes, many=True)
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    
class CommentListAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(post=kwargs["id"])
        serializer = CommentSerializer(comments, many=True)
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)