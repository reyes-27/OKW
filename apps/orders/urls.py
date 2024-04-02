from django.urls import path
from .views import (
    CustomerCartAPIView,
    CustomerOrderDetailAPIView,
    CustomerOrderListAPIView,
    )
urlpatterns = [
    path("", CustomerOrderListAPIView.as_view(), name="orders-list"),
    path("<uuid:id>/", CustomerOrderDetailAPIView.as_view(), name="order-detail"),
    path("cart/<uuid:id>/", view=CustomerCartAPIView.as_view(), name="cart-detail"),
]
