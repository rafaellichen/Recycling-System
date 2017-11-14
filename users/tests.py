'''Test for Users App'''
from django.contrib.auth.models import User
from django.test import TestCase

class LoginTest(TestCase):
    '''LoginTest for User App'''
    def setUp(self):
        '''Method setup that sets the user credentials'''
        self.credentials = {
            'username': 'test',
            'password': 'password'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        '''Method test_Login that logs in'''
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
