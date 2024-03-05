from django.urls import path
from .views import (
    PostDetailAPIView,
    PostListAPIView,
    LikeListAPIView,
    DislikeListAPIView
    )
urlpatterns = [
    path("", PostListAPIView.as_view(), name="post-list"),
    path("<uuid:id>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("<uuid:id>/likes/", LikeListAPIView.as_view(), name="likes-list"),
    path("<uuid:id>/dislikes/", DislikeListAPIView.as_view(), name="dislikes-list"),
]
