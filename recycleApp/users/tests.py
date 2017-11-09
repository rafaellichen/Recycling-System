from django.contrib.auth.models import User
from django.test import TestCase

class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/login/', **self.credentials)      
        self.assertTrue(response.context['user'].is_active)
