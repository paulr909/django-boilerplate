from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Post
from ..views import BlogView


class BlogTests(TestCase):
    def setUp(self):
        self.items = Post.objects.create(name='Blog View', post='Testing Blog View.',
                                         link='http://google.com')
        url = reverse('blog')
        self.response = self.client.get(url)

    def test_blog_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_blog_url_resloves_blog_view(self):
        view = resolve('/blog/')
        self.assertEquals(view.func.view_class, BlogView)
