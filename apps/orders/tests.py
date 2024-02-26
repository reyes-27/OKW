from django.test import TestCase
from rest_framework.test import (
    APITestCase,
    APIRequestFactory,
    )
from .models import *
# Create your tests here.

class OrdersTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.order = Order.objects.create()