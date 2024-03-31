from rest_framework.test import (
    APITestCase,
    APIClient,
    )
from apps.accounts.models import CustomUser, Customer
from django.urls import reverse

from rest_framework import status
from apps.items.models import Product
from apps.categories.models import Category
import json

# Create your tests here.

class EcommerceTestCase(APITestCase):
    fixtures = ['permissions', 'groups', 'accounts', 'categories', 'products',]

    def setUp(self):
        self.user = CustomUser.objects.create(username="test", email="test@email.com", password="penedemono12")
        self.customer = Customer.objects.create(
            user = self.user,
            phone = 2223334445,
            first_name = "TestName",
            last_name = "Test",
            country = "Nigeria",
            is_seller = True
        )
        # cat = Category.objects.create(name="Test", desc="pene de mono")
        self.product1 = Product.objects.create(name="waos", description="pene de mono", stock=10, unit_price=100, seller=self.customer)
        self.product2 = Product.objects.create(name="waos se no fué", description="pene de mono", stock=70, unit_price=199, seller=self.customer)
        # self.product.categories.add(cat)
        self.client.force_authenticate(user=self.user)
        # self.product3 = Product.objects.get(id='a000f987-f734-437f-9d35-a41974a0a37e')

    
    def test_product_detail_view(self):
        url = reverse(viewname="product-detail", kwargs={"slug":self.product1.slug})
        response = self.client.get(path=url)
        parsed_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(parsed_data["data"]["name"], "waos")

    # def test_product_detail_view_PATCH(self):
    #     #I have to write permissions before.
    #     pass

    # def test_product_detail_view_DELETE(self):
    #     pass
        
    def test_visibility(self):
        url = reverse(viewname="product-detail", kwargs={"slug":"waos_f734"})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 401)

    def test_product_list_view_GET(self):
        #Testing GET method
        url = reverse(viewname="product-list")
        response = self.client.get(path=url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(parsed_response["data"]), 3)
        data = {
                "name":"test product",
                "description":"Test description", 
                "stock":70,
                "unit_price":199
                }
        response = self.client.post(path=url, data=data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "test product")

