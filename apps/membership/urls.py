from  django.urls import path
from .views import (
    MembershipDetailAPIView,
    MembershipListAPIView,
    )
urlpatterns = [
    path('<slug:slug>/', view=MembershipDetailAPIView.as_view(), name="membership-detail"),
    path('', view=MembershipListAPIView.as_view(), name='membership-list'),
]
