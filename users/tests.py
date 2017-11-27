'''Test for Users App'''
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from users.forms import SignupForm

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
        login = self.client.login(username='test', password='password')
        response = self.client.get('/')
        
        # Verify first that the user has logged in with the accurate response code
        self.assertEqual(str(response.context['user']), 'test')
        self.assertEqual(response.status_code, 200)

        self.client.logout();
        response = self.client.get('/')

        # self.assertFalse(str(response.context['user'] == "test"))
        self.assertEqual(response.status_code, 200)

    def invalid_user_login_test(self):
        '''Method for testing the rendered message for invalid users'''
        login = self.client.login(username='garbage', password='password')
        response = self.client.get('/')

        self.assertEqual(str(response), "Invalid Login")
        self.assertEqual(response.status_code, 200)


class UserProfileViewTest(TestCase):
    '''Test for User Profile View'''
    def setUp(self):
        '''Method setup that sets the user credentials'''
        user = User.objects.create_user(username='test', password='password')
        user.save()  

    def test_profile_page_view(self):
        '''Method to test the profile page views is being rendered after login'''
        login = self.client.login(username='test', password='password')
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)

    def test_home_template_use(self):
        '''Method to test if the correct profile template was used'''
        login = self.client.login(username='test', password='password')
        response = self.client.get('/profile')
        self.assertTemplateUsed(response, 'users/profile.djhtml') 


class SignupFormTest(TestCase):
    '''Signup Form Test Class for users app'''

    def test_singupForm_password_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['password'].label== 'Password')

# Create your tests here.
class UsersViewTest(TestCase):

    def test_index_from_url(self):
        '''Test returns true when user account index is redered properly with URL'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_from_url(self):
        response = self.client.get('login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_from_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signup_from_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_profile_from_name(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
