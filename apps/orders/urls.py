from django.urls import path
from .views import CustomerOrderListAPIView
urlpatterns = [
    path("", view=CustomerOrderListAPIView.as_view(), name="orders-list"),
]
