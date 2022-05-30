from django.test import TestCase


class TestViews(TestCase):
    """Test class for views in agenda"""

    def test_landing_page_anonymous_user(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    def test_login_view(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
