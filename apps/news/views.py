from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import AnonymousUser
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
from .paginators import StandardResultsSetPagination

# Create your views here.

# class PostListAPIView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [AllowAny, ]


class PostListAPIView(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={"request":request})
        return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, context={"request":request})
        if self.request and hasattr(self.request, "user") and not isinstance(self.request.user, AnonymousUser):
            serializer.initial_data["user"] = self.request.user
        if serializer.is_valid():
            serializer.save(user=request.user.customer)
            return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={"error":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        

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
        paginator = StandardResultsSetPagination()
        comments = Comment.objects.order_by("-likes").filter(post=kwargs["id"])
        serializer = CommentSerializer(comments, many=True)
        paginator.paginate_queryset(queryset=serializer.data, request=request)
        return paginator.get_paginated_response(data={"data":serializer.data})