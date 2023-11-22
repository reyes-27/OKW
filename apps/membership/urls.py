from  django.urls import path
from .views import (
    MembershipDetailAPIVIEW,
    MembershipListAPIVIEW,
    )
urlpatterns = [
    path('memberships/<slug:slug>/', view=MembershipDetailAPIVIEW.as_view(), name="membership-detail"),
    path('memberships/', view=MembershipListAPIVIEW.as_view(), name='membership-list'),
]
