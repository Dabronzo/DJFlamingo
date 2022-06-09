from django.test import TestCase


class TestViews(TestCase):
    """
    Test class for views in agenda. This class
    will only test if the user is not registered the site
    shall display a landing page
    """

    def test_landing_page_anonymous_user(self):
        """
        Test for the anonymous user
        displaying the landing page template
        """

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

