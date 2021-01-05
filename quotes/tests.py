from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
import unittest

class ModelTests(unittest.TestCase):

    def TestUser(self):
        """ Testing if there are users in db  """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@hotmail.com', 
            password='password123'

        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_superuser(
            email='test@hotmail.com',
            password='password123',
            name="Test User Full Name"
        )

    def test_users_listed(self):
        """ Test that users are listed """
        url = reverse('admin:core_user_changeList')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

