from django.test import TestCase
from django.contrib.messages import get_messages
from .models import NewDjUser

# defining user model


class TestViews(TestCase):
    """Dockstring"""
    
    def setUp(self):

        self.djuser = NewDjUser.objects.create_user(
            'test@email.com',
            'testdj',
            'testpassword'
            )

    def tearDown(self):
        del self.djuser

    def test_login_display_view(self):
        """Test for login view"""
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    def test_registration(self):
        """
        Test the template of registration
        """

        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('register.html')

    def test_login_sucess(self):
        """
        Testing if a success on login
        display the right template
        """
        # dj_user = NewDjUser.objects.filter(user_name='djtest')[0]
        credentials = {'email': 'test@email.com', 'password': 'testpassword'}
        response = self.client.post(
            '/accounts/login',
            credentials,
            follow=True
            )

        # testing status code and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # testing django messages
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            f"Welcome back {self.djuser.user_name}"
            )
        
    def test_error_on_login(self):
        """ If somethin is worng if login"""

        response = self.client.post('/accounts/login', data={
            'email': 'wrong_email',
            'password': self.djuser.password
        })

        self.assertEqual(response.status_code, 200)

        # testing django messages
        all_messages = list(get_messages(response.wsgi_request))

        self.assertEqual(
            all_messages[0].message,
            "An error ocurred with the login, please try again."
            )

        # testing if the login template will be displayed
        self.assertTemplateUsed('login.html')

    def test_logut_view(self):
        """Test for logout"""

        response = self.client.get('/accounts/logout')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    
