from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Contact
from ..views import contact


class ContactTests(TestCase):
    def setUp(self):
        self.items = Contact.objects.create(name='Contact View', email='tester@mail.com',
                                            message='New Project Form', budget=4500, industry='Film')
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_contact_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_contact_url_resloves_contact_view(self):
        view = resolve('/contact/')
        self.assertEquals(view.func, contact)
