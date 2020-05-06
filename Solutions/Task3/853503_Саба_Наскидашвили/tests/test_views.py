from django.test import TestCase, Client
from django.urls import reverse
from wines.models import Wine, GrapeSort, Reviews, Rating, Category, RatingStar
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('wine_list')
        self.detail_url = reverse("wine_detail", args=['project1'])
        self.add_rating = reverse("add_rating")
        self.grape_detail = reverse("grape_sort_detail", args=['project1'])
        self.project1 = Wine.objects.create(
            name="project1",
            description="test",
            country="Italy",
            year=2001,
            image="grape",
            url="project1"
        )

    def test_wine_list_get(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'wines/wine_list.html')

    def test_wine_detail_get(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'wines/wine_detail.html')







