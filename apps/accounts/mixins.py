from apps.accounts.models import CustomUser, Customer
from django.test import TestCase
class UserTestDataMixin(TestCase):
    user = CustomUser.objects.create(username="test", email="test@email.com", password="penedemono12")
    customer = Customer.objects.create(
            user = user,
            phone = 2223334445,
            first_name = "TestName",
            last_name = "Test",
            country = "Nigeria",
            is_seller = True
            )
    