from django.test import TestCase
from django.contrib.messages import get_messages
from datetime import date, datetime,timedelta
from accounts.models import NewDjUser
from .models import Gig, Venue

# getting a current time for gig creation
current_time = datetime.now().strftime('%H:%M:%S')
# get yesterday to test history
yesterday = datetime.now() - timedelta(1)

class TestViews(TestCase):
    """
    Test class for views in agenda. This class
    will only test if the user is not registered the site
    shall display a landing page
    """

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
            name='Test',
            slug='test',
            date=date.today(),
            time_start=current_time,
            time_duration='test',
            dj=self.djuser,
            venue=self.venue,
            fees=100,
            agency_tax=5,
            is_payed=False,
            status=0,
            notes=''
        )

        self.gig_yesterday = Gig.objects.create(
            name='yesterdayTest',
            slug='yesterdaytest',
            date=yesterday,
            time_start=current_time,
            time_duration='test',
            dj=self.djuser,
            venue=self.venue,
            fees=100,
            agency_tax=5,
            is_payed=False,
            status=0,
            notes=''
        )

    def tearDown(self):
        del self.djuser
        del self.admin_user
        del self.gig
        del self.venue

    def test_landing_page_anonymous_user(self):
        """
        Test for the anonymous user
        displaying the landing page template
        """

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')
    
    def test_all_gigs_history(self):
        """
        Test if the view is working
        for superuser
        """

        # login superuser
        self.client.login(
            email='admin@email.com',
            password='adminpassword'
        )
        response = self.client.get('/gigs_history')

        # test status code and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gigs_history.html')
    
    def test_gigs_history_no_admin(self):
        """ Testing if normar user
        redirects to home"""

        # login as normal user
        self.client.login(email='test@email.com', password='testpassword')
        response = self.client.get('/gigs_history')

        # test redirect
        self.assertRedirects(response, '/')

    def test_my_history_view(self):
        """
        Testing the my gigs view
        for normal user
        """

        # login as normal user
        self.client.login(email='test@email.com', password='testpassword')
        response = self.client.get('/history')

        # test status code and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history.html')

    def test_create_gig_view(self):
        """
        Testing the creation of a post get
        method
        """

        # login superuser
        self.client.login(
            email='admin@email.com',
            password='adminpassword'
        )
        response_get = self.client.get('/create_gig')
        
        # testing code and template
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'create_gig.html')

        # testing for post method
        response_post = self.client.post('/create_gig', data=dict(
            name='Another',
            slug='another',
            date=date.today(),
            time_start=current_time,
            time_duration='test',
            dj=self.djuser.pk,
            venue=self.venue.pk,
            fees=100,
            agency_tax=5,
            is_payed=False,
            status=0,
            notes=''
        ))

        # testing creation and redirect
        gig_created = Gig.objects.filter(name='Another')
        self.assertEqual(gig_created[0].name, 'Another')
        self.assertRedirects(response_post, '/')

        # testing django messages
        all_messages = list(get_messages(response_post.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
             "New gig created!"
            )

    def test_create_gig_failure_user(self):
        """ test if only admin can access view"""

        # login as normal user
        self.client.login(email='test@email.com', password='testpassword')
        response = self.client.get('/create_gig')

        # testing redirect
        self.assertRedirects(response, '/')

    def test_create_gig_failure_form(self):
        """
        test if an error messaga and the correct
        template are being displayed in case
        form is not valid
        """

        # login as admin
        self.client.login(email='admin@email.com', password='adminpassword')

        response = self.client.post('/create_gig', data=dict(
            name='wrong'
        ))

        self.assertEqual(response.status_code, 200)

        # testing error message
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Oops something went wrong, try it again."
            )

        self.assertTemplateUsed(response, 'create_gig.html')

    def test_delete_gig(self):
        """
        Test for the delete gig funcionality
        """

        # login as admin
        self.client.login(email='admin@email.com', password='adminpassword')

        response = self.client.post(f'/delete_gig/{self.gig.slug}')

        # testing django messages
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
             "Gig deleted!"
            )

        
        # testing redirect
        self.assertRedirects(response, '/')
    
    def test_create_venue(self):
        """
        Testing the create venue view
        """

        # login as superuser
        self.client.login(email='admin@email.com', password='adminpassword')

        # testing get response
        response_get = self.client.get('/create_venue')

        # testing status code and template
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'create_venue.html')

        # testing post response
        response_post = self.client.post('/create_venue', data=dict(
            name='venuetest',
            address='venueaddress',
            city='testcity',
            website='',
            contact='testcontact',
            additional_info=''
        ))

        # testing resdirect
        self.assertRedirects(response_post, '/')

        # testing success messages
        all_messages = list(get_messages(response_post.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "New venue created!"
            )

        # testing if the form is not valid
        response_failed = self.client.post('/create_venue', data=dict(
            name='',
            address='venueaddress',
            city='testcity',
            website='',
            contact='testcontact',
            additional_info=''
        ))

        self.assertTemplateUsed(response_failed, 'create_venue.html')

        # testing for error message
        all_messages = list(get_messages(response_failed.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Somthing went wrong, please try again"
            )
        
    def test_create_venue_failure(self):
        """
        Test if only the admin can access the 
        create venue
        """

        # login as normal user
        self.client.login(email='test@email.com', password='testpassword')
        response = self.client.get('/create_venue')

        self.assertRedirects(response, '/')

    def test_gig_details_view(self):
        """
        Test for the right template and 
        user permissions
        """

        self.client.login(email='test@email.com', password='testpassword')

        # response for a specific gig
        response = self.client.get(f'/details/{self.gig.slug}')

        self.assertEqual(response.status_code, 200)

    def test_accept_gig(self):
        """ Test if a gig can be accepted"""

        self.client.login(email='admin@email.com', password='adminpassword')
        # accepting a proposal gig
        response = self.client.post(f'/accept/{self.gig.slug}')
        gig = Gig.objects.filter(name=self.gig.name)[0]

        self.assertEqual(gig.status, 1)
        self.assertTemplateUsed(response, 'gig_details.html')
        
        # testing message
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Gig proposal accepted!"
            )

    def test_refuse_gig(self):
        """
        Testing reject a proposal gig
        """
        self.client.login(email='admin@email.com', password='adminpassword')
        response = self.client.post(f'/refuse/{self.gig.slug}')
        gig = Gig.objects.filter(name=self.gig.name)[0]

        self.assertEqual(gig.status, 2)
        self.assertRedirects(response, '/')

        # testing message
        all_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Gig refused!"
            )
    
    def test_udpate_gig(self):
        """
        Test for the update gig
        """

        # login as admin    
        self.client.login(email='admin@email.com', password='adminpassword')

        # testing get method
        response_get = self.client.get(f'/update/{self.gig.slug}')

        # testing status code and template
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'edit_gig.html')

        # testing post method
        response_post = self.client.post(f'/update/{self.gig.slug}', data=dict(
            name='Test',
            date=date.today(),
            time_start=current_time,
            time_duration='updated',
            dj=self.djuser.pk,
            venue=self.venue.pk,
            fees=100,
            agency_tax=5,
            is_payed=False,
            status=0,
            notes=''
            ))
        
        self.assertEqual(response_post.status_code, 302)
        self.assertRedirects(response_post, '/')

        # testing for sucess message
        all_messages = list(get_messages(response_post.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Gig updated!"
            )

        # testing for form invalid
        response_fail = self.client.post(f'/update/{self.gig.slug}', data=dict(
            name='',
            date=date.today(),
            time_start=current_time,
            time_duration='updated',
            dj=self.djuser.pk,
            venue=self.venue.pk,
            fees=100,
            agency_tax=5,
            is_payed=False,
            status=0,
            notes=''
            ))
        
        self.assertTemplateUsed(response_fail, 'edit_gig.html')
        # testing for sucess message
        all_messages = list(get_messages(response_fail.wsgi_request))
        self.assertEqual(
            all_messages[0].message,
            "Oops, something went worng."
            )

    def test_update_gig_fail(self):
        """
        Testing if only admin can updade gigs
        """

        self.client.login(email='test@email.com', password='testpassword')

        response = self.client.get(f'/update/{self.gig.slug}')

        self.assertRedirects(response, "/")
