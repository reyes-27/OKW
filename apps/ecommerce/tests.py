from rest_framework.test import (
    APITestCase,
    APIClient,
    )
from apps.accounts.models import CustomUser
from django.urls import reverse
from rest_framework import status
from apps.items.models import Product
from apps.categories.models import Category
import json
# Create your tests here.

class EcommerceTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="test", email="test@email.com", password="penedemono12")
        # cat = Category.objects.create(name="Test", desc="pene de mono")
        self.product1 = Product.objects.create(name="waos", description="pene de mono", stock=10, unit_price=100)
        self.product2 = Product.objects.create(name="waos se no fué", description="pene de mono", stock=70, unit_price=199)
        # self.product.category.add(cat)
        self.client.force_authenticate(user=self.user)
        
    
    def test_product_detail_view(self):
        url = reverse(viewname="product-detail", kwargs={"slug":self.product1.slug})
        response = self.client.get(path=url)
        parsed_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(parsed_data["data"]["name"], "waos")
    
    def test_product_list_view(self):
        url = reverse(viewname="product-list")
        response = self.client.get(path=url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(parsed_response["data"]), 2)
        # self.assertContains(parsed_response["data"][0]["description"], "pene")