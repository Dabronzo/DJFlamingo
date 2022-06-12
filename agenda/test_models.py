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

    # Set up to simulate gig, user and venue for testing
    def setUp(self):

        self.djuser = NewDjUser.objects.create_user(
            'test@email.com',
            'testdj',
            'testpassword'
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

    # Testing the models properties
    def test_days_to_property(self):
        """Test for the days_to property"""

        self.assertEqual(self.gig.days_to, 0)

    def test_if_cash_is_calculated(self):
        """
        Test for the property that calculates
        the cash for the dj of each gig
        """
        self.assertEqual(self.gig.calculated_fees, 95)

    def test_if_agency_tax_is_calculated(self):
        """
        Test for the property that calculates the
        agency cash for the gig
        """

        self.assertEqual(self.gig.calc_agency_cash, 5)

    def test_if_dj_created(self):
        """ If the Dj is created properly"""

        dj_test = NewDjUser.objects.filter(user_name='testdj')
        self.assertEqual(dj_test[0].user_name, 'testdj')

    def test_retrun_string_for_gig(self):
        """return string name"""

        newgig = Gig.objects.filter(name='Test')
        gig = newgig[0]
        self.assertEqual(
            str(this_gig),
            f"Gig on {gig.date} at {gig.venue} assined to {gig.dj}"
            )

    def test_return_string_venue(self):
        """Return string name"""
        venue = Venue.objects.filter(name='testvenue')
        this_venue = venue[0]
        self.assertEqual(str(this_venue), f"{this_venue.name}")
