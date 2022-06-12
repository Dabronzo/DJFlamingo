from django.test import TestCase
from .forms import RegistrationForm


class TestAccountForms(TestCase):
    """
    Class to test the user registration form
    """

    def test_if_name_is_passed(self):
        """
        Expected false if a name is not passed
        """

        form = RegistrationForm(
            {
                'email': 'testemail',
                'user_name': '',
                'password1': 'testpassword',
                'password2': 'testpassword',
            }
        )

        self.assertFalse(form.is_valid())

    def test_fields_in_meta_class(self):
        """
        Test to make sure that the correct
        fields are being displayed on the form
        """

        form = RegistrationForm()
        self.assertEqual(
            form.Meta.fields,
            (
                'email',
                'user_name',
                'password1',
                'password2',
            )
        )
