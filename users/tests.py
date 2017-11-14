'''Test for Users App'''
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase

class LoginTest(TestCase):
    '''LoginTest for User App'''
    def setUp(self):
        '''Method setup that sets the user credentials'''
        user = User.objects.create_user(username='test', password: 'password')
        user.save()            

    def test_login(self):
        '''Method test_Login that logs in'''
        response = self.client.login('/login/', self.credentials)


