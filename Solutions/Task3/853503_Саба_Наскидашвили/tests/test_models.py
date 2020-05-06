from django.test import TestCase
from wines.models import Wine, GrapeSort, Category, Food, Reviews, Rating, RatingStar

class TestModels(TestCase):

    def setUp(self):
        self.project1 = Wine.objects.create(
            name='wine',
            description='test',
            year=2001,
            country='Italy',
        )

    def test_wine_is_assigned_slug_on_getting(self):
        self.assertEquals(self.project1.url, self.project1.url)

