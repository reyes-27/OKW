from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import MembershipSerializer
from .models import Membership
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class MembershipDetailAPIView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        membership = Membership.objects.get(slug=self.kwargs['slug'])
        serializer = MembershipSerializer(membership, context={"request":request}, read_only=True)
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
    
class MembershipListAPIView(APIView):
    #SINCE I DON'T HAVE THAT MANY PRODUCTS I'LL SHOW EVERY SINGLE PRODUCTS, THE BEST CASE WOULD BE TO FILTER FOR TREND PRODUCTS
    permission_classes = [AllowAny, ]
    def get(self, request, *args, **kwargs):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, context={'request':request}, many=True, read_only=True)
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)