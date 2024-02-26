from rest_framework.test import (
    APITestCase,
    APIClient,
    )
from apps.accounts.models import CustomUser
# Create your tests here.

class ItemsTest(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = CustomUser.objects.get(username="Admin")
        
        cls.client = APIClient()
        cls.client.force_authenticate(user=cls.user)



