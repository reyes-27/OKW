from rest_framework.test import APITestCase
from apps.accounts.models import CustomUser, Customer

from ..models import CustomerMembership, Membership
from datetime import timedelta, datetime


# Create your tests here.

class MembershipTestCase(APITestCase):
    fixtures = ['permissions', 'groups', 'accounts']
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

        membership = Membership.objects.create(
            name="Premium",
            unit_price = 3,
            discount = 0,
            level=1,
            duration=timedelta(days=30)
        )

        self.user.membership.sample = membership
        self.user.membership.save()


    def test_expiration(self):
        self.assertEqual(self.user.membership.status, "ACTIVE")
        self.user.membership.test_set_status(self.user.membership.end_date)
        self.assertEqual(self.user.membership.status, "SUSPENDED")

