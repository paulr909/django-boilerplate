from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Item
from ..views import AboutView


class AboutTests(TestCase):
    def setUp(self):
        self.items = Item.objects.create(name='About View', description='Testing About View.',
                                         link='http://google.com')
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_about_url_resloves_about_view(self):
        view = resolve('/about/')
        self.assertEquals(view.func.view_class, AboutView)
