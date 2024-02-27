from django.test import TestCase
from rest_framework.test import (
    APITestCase,
    APIRequestFactory,
    )
from .models import *
# Create your tests here.

class OrdersTestCase(APITestCase):
    def setUp(self):
        self.order = Order.objects.create()