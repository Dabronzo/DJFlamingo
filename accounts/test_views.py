from django.test import TestCase
from agenda.models import Gig, Venue
from django.contrib.messages import get_messages
from .models import NewDjUser
from datetime import date, datetime


# defining user model


class TestViews(TestCase):
    """Dockstring"""

    def setUp(self):

        self.djuser = NewDjUser.objects.create_user(
            'test@email.com',
            'testdj',
            'testpassword'
            )

        self.admin_user = NewDjUser.objects.create_superuser(
            'admin@email.com',
            'testadmin',
            'adminpassword'
            )

        self.venue = Venue.objects.create(
            name='testvenue',
            address='testaddress',
            city='testcity',
            website='',
            contact='testcontact',
            additional_info=''
        )

        self.gig = Gig.objects.create(
            date=date.today(),
            name='Test',
            status=0,
            created_on=datetime.now(),
            updated_on=datetime.now(),
            time_start=datetime.now(),
            time_duration='test',
            dj=self.djuser,
            venue=self.venue,
            fees=100,
            agency_tax=5,
            is_payed=False,
            notes=''
        )

    def tearDown(self):
        del self.djuser
        del self.admin_user
        del self.gig
        del self.venue

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

    def test_registration_post(self):
        """
        If the registration process
        works with success
        """

        response = self.client.post('/accounts/register', data=dict(
            email='another@email.com',
            user_name='anothertestdj',
            password1='anotherpassword',
            password2='anotherpassword'
        ))

        # tesing response and urls
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

        # testing django messages
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Success! You are registered on Flamingo"
            )

    def test_registration_failure_post(self):
        """
        Test if the right template and message
        are displayed if registration fails
        """

        response = self.client.post('/accounts/register', data=dict(
            # email missing with make the form fail
            email='',
            user_name='anothertestdj',
            password1='anotherpassword',
            password2='anotherpassword'
        ))

        # testing template used
        self.assertTemplateUsed(response, 'register.html')

        # testing django messages
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Something went wrong, please try it again."
            )

    def test_login_sucess(self):
        """
        Testing if a success on login
        display the right template
        """
        response = self.client.post('/accounts/login', data=dict(
            email='test@email.com',
            password='testpassword'
        ))

        # testing status code and template
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

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

    def test_all_users_view(self):
        """
        Testing if the all gigs admin
        view is working properly
        """
        # login with admin credentials
        self.client.login(email='admin@email.com', password='adminpassword')
        response = self.client.get('/accounts/all_users')

        # testing response code and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_users.html')

    def test_all_users_failure(self):
        """
        Testing if the user admin
        is the only type that can access
        this page
        """

        # login wiht a normal user
        self.client.login(email='test@email.com', passowrd='testpassword')
        response = self.client.get('/accounts/all_users')

        # testing redirecting
        self.assertRedirects(response, '/')

    def test_dj_details_view(self):
        """
        Testing the view to display dj
        details to admin
        """

        # login with admin
        self.client.login(email='admin@email.com', password='adminpassword')
        response = self.client.get(
            f'/accounts/user_details/{self.djuser.user_name}'
            )

        # testing if the correct queryset is used
        dj_gigs = Gig.objects.filter(dj=self.djuser.pk)
        # print(dj_gigs)
        self.assertQuerysetEqual(
            dj_gigs,
            ['<Gig: Gig on 2022-06-11 at testvenue assined to testdj>']
            )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_details.html')

    def test_dj_details_failure(self):
        """
        Testing if the view redirect to home
        in case the user is not admin status
        """

        # login with normal user
        self.client.login(email='test@email.com', passowrd='testpassword')
        response = self.client.get(
            f'/accounts/user_details/{self.djuser.user_name}'
        )

        self.assertRedirects(response, '/')

    def test_delete_dj_view(self):
        """
        Testing deleting functionality
        """

        # login as admin
        self.client.login(email='admin@email.com', password='adminpassword')
        response = self.client.post(
            f'/accounts/delete_user/{self.djuser.user_name}'
            )

        # testing django messages
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            f"User {self.djuser.user_name} was deleted!"
            )

        # testing redirect
        self.assertRedirects(response, '/')
