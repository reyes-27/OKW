from django.urls import path
from .views import (
    PostDetailAPIView,
    PostListCreateAPIView,
    LikeListAPIView,
    DislikeListAPIView,
    CommentListAPIView,
    )
urlpatterns = [
    path("", PostListCreateAPIView.as_view(), name="post-list"),
    path("<uuid:id>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("<uuid:id>/likes/", LikeListAPIView.as_view(), name="likes-list"),
    path("<uuid:id>/dislikes/", DislikeListAPIView.as_view(), name="dislikes-list"),
    path("<uuid:id>/comments/", CommentListAPIView.as_view(), name="comments-list"),
]
