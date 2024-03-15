import json
from rest_framework.test import APITestCase
from apps.categories.models import Category
from apps.news.models import Post, PostImage
from django.urls import reverse
from apps.accounts.models import CustomUser, Customer
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.

class NewsAPITestCase(APITestCase):
    fixtures = ['news_post', 'accounts']
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

        self.sukuna_img = SimpleUploadedFile("sukuna.png", content=open(r"C:\Users\dani2\Documents\Backend-projects\OKW\testing-assets\sukuna.png", "rb").read(), content_type="image/png")
        self.waos_img = SimpleUploadedFile("waos.png", content=open(r"C:\Users\dani2\Documents\Backend-projects\OKW\testing-assets\waos.png", "rb").read(), content_type="image/png")
        category=Category.objects.create(name="TestCategory", desc="WAos")
        self.post = Post.objects.create(
                                        user=self.customer,
                                        header="Test header",
                                        description="Test description",
                                        )
        self.sukuna = PostImage.objects.create(post=self.post, image=self.sukuna_img, level=0)
        self.waos = PostImage.objects.create(post=self.post, image=self.waos_img, level=1)

        self.client.force_authenticate(user=self.user)


    def test_post_list_view_POST(self):
        url = reverse("post-list")
        data = {
                    # "category": [
                    #     {
                    #         "id": 1,
                    #         "name": "Tech",
                    #         "desc": "waos",
                    #         "parent": None
                    #     }
                    # ],
                    "header": "Test header",
                    "description": "WAos",
                    # "image_set": [
                    #     {
                    #         "image":self.sukuna_img.read(),
                    #         "level": 0
                    #     },
                    #     {
                    #         "image":self.waos_img.read(),
                    #         "level":1
                    #     }
                    # ]
                }
        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["data"]["header"], "Test header")

    def test_post_list_view_GET(self):
        url = reverse(viewname="post-list")
        response = self.client.get(path=url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        print(response.data)
        # self.assertEqual(len(parsed_response["data"][0]["image_set"]), 2)
        self.assertEqual(len(parsed_response["data"]), 1)