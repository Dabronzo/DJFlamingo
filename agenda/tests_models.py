from django.test import TestCase
from datetime import date, datetime
from .models import Gig, Venue
from accounts.models import NewDjUser


class TestModels(TestCase):
    """
    Class to test the models of agenda app. It will
    create a Gig, Venue and a User for test the 
    properties fo the Gig Model class
    """

    def setUp(self):

        self.djuser = NewDjUser.objects.create(
            user_name='djtest',
            is_superuser=False,
            email='testemail',
            is_staff=False,
            password='testpassword'
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
        del self.venue
        del self.gig

    def test_if_gig_created(self):
        """Check if the gig was created correctly"""

        newgig = Gig.objects.filter(name='Test')
        self.assertEqual(newgig[0].name, 'Test')

    def test_days_to_property(self):
        """Test for the days_to property"""

        self.assertEqual(self.gig.days_to, 0)

    def test_if_cash_is_calculated(self):
        """
        Test for the property that calculates
        the cash for the dj of each gig
        """
        self.assertEqual(self.gig.calculated_fees, 95)

    def test_if_agency_cahs_is_calculated(self):
        """
        Test for the property that calculates the
        agency cash for the gig
        """

        self.assertEqual(self.gig.calc_agency_cash, 5)
