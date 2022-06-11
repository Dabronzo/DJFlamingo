from django.test import TestCase
from .forms import GigCreationForm, VenueCreationForm


class TestGigCreationForm(TestCase):
    """Test for the gig creation form"""

    def test_gig_name_required(self):
        form = GigCreationForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_in_meta_class(self):
        form = GigCreationForm()
        self.assertEqual(
            form.Meta.fields, (
                'name',
                'date',
                'time_start',
                'time_duration',
                'dj',
                'venue',
                'fees',
                'agency_tax',
                'is_payed',
                'status',
                'notes'
            ))


class TestVenueCreationForm(TestCase):
    """Class test for venue form"""

    def test_name_required(self):
        form = VenueCreationForm({'name': ''})
        self.assertFalse(form.is_valid())

    def test_not_required_fields(self):
        form = VenueCreationForm(
            {
                'name': 'Test Venue',
                'address': 'Test address',
                'city': 'Test city',
                'website': '',
                'contact': 'Test contact',
                'additional_info': ''
            }
        )
        self.assertTrue(form.is_valid())

    def test_forms_fields_meta(self):
        form = VenueCreationForm()
        self.assertEqual(
            form.Meta.fields, (
                'name',
                'address',
                'city',
                'website',
                'contact',
                'additional_info'
            ))

