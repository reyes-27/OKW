from django.urls import path
from .views import (
    PostDetailAPIView,
    PostListAPIView,
    )
urlpatterns = [
    path("", PostListAPIView.as_view(), name="post-list"),
    path("<uuid:id>/", PostDetailAPIView.as_view(), name="post-detail"),
]
