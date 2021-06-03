from django.test import TestCase
from django.contrib.auth import get_user_model


class Modeltests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@idkwhatis.domain'
        password = 'P@$$W0rD'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for an new user is normalized"""
        email = 'test@IdkWhatIs.domain'
        user = get_user_model().objects.create_user(email, 'p@$$w0rd')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'p@$$w0rd')

    def test_create_new_superuser(self):
        """Testing creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@IdkWhatIs.domain',
            'P@$$W0rD'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
