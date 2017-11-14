'''Test for Users App'''
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from catalog.forms import SignupForm

class LoginTest(TestCase):
    '''LoginTest for User App'''
    def setUp(self):
        '''Method setup that sets the user credentials'''
        user = User.objects.create_user(username='test', password='password')
        user.save()            

    def test_login(self):
        '''Method test_Login that logs in'''
        login = self.client.login(username='test', password='password')
        response = self.client.get('/')

        self.assertEqual(str(response.context['user']), 'test')
        self.assertEqual(response.status_code, 200)

	def test_logout(self):
		'''Method test_logout that verifies the logout'''       