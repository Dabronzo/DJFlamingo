from django.test import TestCase
from django.urls import reverse
from .models import NewDjUser


class TestViews(TestCase):
    """Dockstring"""

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('home')
        self.login_page_url = reverse('login')
        self.logout = reverse('logout')

        self.user = {
            'email': 'test@email.com',
            'user_name': 'testdj',
            'password': 'testpassword',
            'password2': 'testpassword'
        }

    def tearDown(self):
        del self.user
        del self.register_url
    
    def test_login_template(self):
        response = self.client.get(self.login_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
