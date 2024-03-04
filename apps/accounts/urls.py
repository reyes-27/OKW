from django.urls import path
from .views import CustomerProfileDetailView
urlpatterns = [
    path("customers/<uuid:id>/", view=CustomerProfileDetailView.as_view(), name="customer-detail"),
]