from django.test import TestCase
from .models import NewDjUser


class TestModel(TestCase):
    """
    Class test for the custom user
    model
    """

    def setUp(self):
        self.djuser = NewDjUser.objects.create_user(
            'test@email.com',
            'testdj',
            'testpassword'
            )
        self.super_user = NewDjUser.objects.create_superuser(
            'super@email.com',
            'super',
            'superpassword'
            )

    def tearDown(self):
        del self.djuser
        del self.super_user

    def test_creation_user(self):
        """ Test to the creation of users"""
        users = NewDjUser.objects.all()
        self.assertEqual(len(users), 2)

    def test_super_user_creation(self):

        self.assertTrue(self.super_user.is_superuser)
        self.assertTrue(self.super_user.is_staff)

        # test default values not matching
        self.assertRaises(
            ValueError,
            NewDjUser.objects.create_superuser,
            email='superwrond@email.com',
            user_name='superWrong',
            password='wrongpassword',
            is_staff=False
            )

    def test_email_not_passed_user(self):
        """
        Testing the raise for an
        user creation without an email
        """

        self.assertRaises(
            ValueError,
            NewDjUser.objects.create_user,
            email="",
            user_name="testdj2",
            password="testpassword2"
            )

    def test_if_superuser_fails(self):
        """
        Testing if during the superuser creation
        the supeuser is set as false
        expect raise error
        """

        self.assertRaises(
            ValueError,
            NewDjUser.objects.create_superuser,
            email="failadim@email.com",
            user_name='adminfail',
            password='testfailpassword',
            is_superuser=False
            )
