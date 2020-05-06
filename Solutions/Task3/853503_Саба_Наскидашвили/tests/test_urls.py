from django.test import SimpleTestCase
from django.urls import reverse, resolve
from wines.views import WinesView, FilterWinesView, GrapeView, AddReview, WineDetailView, Search, AddStarRating


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse("wine_list")
        self.assertEquals(resolve(url).func.view_class, WinesView)

    def test_filter_url_resolves(self):
        url = reverse("filter")
        self.assertEquals(resolve(url).func.view_class, FilterWinesView)

    def test_search_url_resolves(self):
        url = reverse("search")
        self.assertEquals(resolve(url).func.view_class, Search)

    def test_add_star_rating_url_resolves(self):
        url = reverse("add_rating")
        self.assertEquals(resolve(url).func.view_class, AddStarRating)

    def test_detail_url_resolves(self):
        url = reverse("wine_detail", args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, WineDetailView)

    def test_grape_sort_url_resolves(self):
        url = reverse("grape_sort_detail", args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, GrapeView)
