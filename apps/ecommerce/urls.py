from django.urls import path
from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    )

urlpatterns = [
    path(route="products/", view=ProductListAPIView.as_view(), name="product-list"),
    path(route="products/<slug:slug>/", view=ProductDetailAPIView.as_view(), name="product-detail"),
]
