from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='patelbhumi3696@gmail.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'patelbhumi3696@gmail.com'
        password = "patelbhumi3696"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'patelbhumi3696@gmail.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'patelbhumi3696')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'patelbhumi3696@gmail.com',
            'patelbhumi3696'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
