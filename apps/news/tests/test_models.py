from django.test import TestCase
from ..models import Post, PostImage
from apps.categories.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.accounts.models import CustomUser, Customer

class NewsModelsTestCase(TestCase):
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

        self.sukuna_img = SimpleUploadedFile("sukuna.png", content=open(r"./testing-assets/sukuna.png", "rb").read(), content_type="image/png")
        self.waos_img = SimpleUploadedFile("waos.png", content=open(r"./testing-assets/waos.png", "rb").read(), content_type="image/png")
        category=Category.objects.create(name="TestCategory", desc="WAos")
        self.post = Post.objects.create(
                                        user=self.customer,
                                        header="Test header",
                                        description="Test description",
                                        )
        self.post.categories.add(category)
        

    def test_post_data(self):
        self.assertEqual(self.post.header, "Test header")
        self.assertGreaterEqual(len(self.post.categories.all()), 1)
        