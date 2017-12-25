'''Test for Users App'''
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .views import bookmarkHandler
import json


class LoginAcceptanceTest(StaticLiveServerTestCase):

    # fixtures = ['data.json']
    @classmethod
    def setUpClass(cls):
        super(LoginAcceptanceTest, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)
        User.objects.create_user(username='test10', password='asdasd12')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(LoginAcceptanceTest, cls).tearDownClass()

    def test_login(self):
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_name('login-nav').click()
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test10')
        password_input = self.selenium.find_element_by_id("password")
        password_input.click()
        password_input.clear()
        password_input.send_keys('asdasd12')
        self.selenium.find_element_by_name('loginbtn').click()
        try:
            logged_in = self.selenium.find_element_by_class_name("loggedin")
        except NoSuchElementException:
            logged_in = False
        self.assertTrue(logged_in)


class SignupAcceptanceTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(SignupAcceptanceTest, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)
        cls.new_user = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'janedoe@aol.com',
            'username': 'janedoe101',
            'password':'p@$$w0rd',
            'confirm_password':'p@$$w0rd',
        }

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SignupAcceptanceTest, cls).tearDownClass()

    def test_signup(self):
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_name('signup-nav').click()

        for k,v in self.new_user.items():
            input_field = self.selenium.find_element_by_name(k)
            input_field.click()
            input_field.clear()
            input_field.send_keys(v)

        self.selenium.find_element_by_class_name('signupbtn').click()
        WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "success")))

        try:
            reg_success = self.selenium.find_element_by_class_name("success")
        except NoSuchElementException:
            reg_success = False
        self.assertTrue(reg_success)
        self.assertEqual(reg_success.text, 'HELLO JANE!')



class RegisterationIntegrationTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(RegisterationIntegrationTest, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)
        cls.new_user = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'janedoe@aol.com',
            'username': 'janedoe101',
            'password':'p@$$w0rd',
            'confirm_password':'p@$$w0rd',
        }

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(RegisterationIntegrationTest, cls).tearDownClass()

    def test_integration(self):
        self.Register_new_user()
        self.Login_new_user()

    def Register_new_user(self):
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_name('signup-nav').click()

        for k,v in self.new_user.items():
            input_field = self.selenium.find_element_by_name(k)
            input_field.click()
            input_field.clear()
            input_field.send_keys(v)

        self.selenium.find_element_by_class_name('signupbtn').click()
        WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "success")))

        try:
            reg_success = self.selenium.find_element_by_class_name("success")
        except NoSuchElementException:
            reg_success = False
        self.assertTrue(reg_success)
        self.assertEqual(reg_success.text, 'HELLO JANE!')

    def Login_new_user(self):
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_name('login-nav').click()
        username_input = self.selenium.find_element_by_name("username")
        username_input.click(); username_input.clear()
        username_input.send_keys(self.new_user['username'])
        password_input = self.selenium.find_element_by_id("password")
        password_input.click(); password_input.clear()
        password_input.send_keys(self.new_user['password'])
        self.selenium.find_element_by_name('loginbtn').click()
        try:
            logged_in = self.selenium.find_element_by_class_name("loggedin")
        except NoSuchElementException:
            logged_in = False
        self.assertTrue(logged_in)



class BookmarksViewTest(TestCase):
    fixtures = ['centers.json']

    def setUp(self):
        # self.rf = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@aol.com', password='testpwd')

    def test_bookmarks_view(self):
        self.client.login(username='test', password='testpwd')
        params= json.dumps({"param": "add", "idc":5})
        response = self.client.post('/bookmarks', data= params, content_type='application/json',
                                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                                {'result':'success'})
        new_params = json.dumps({"param": "remove", "idc":5})
        response = self.client.post('/bookmarks', data= new_params, content_type='application/json',
                                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                                {'result':'success'})



class LoginTest(TestCase):
    '''LoginTest for User App'''
    def setUp(self):
        '''Method setup that sets the user credentials'''
        user = User.objects.create_user(username='test', password='password')
        user.save()

    def test_login(self):
        '''Method test_Login that logs in'''
        self.client.login(username='test', password='password')
        response = self.client.get('/')

        self.assertEqual(str(response.context['user']), 'test')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        '''Method test_logout that verifies the logout'''
        self.client.login(username='test', password='password')
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
        self.client.login(username='garbage', password='password')
        response = self.client.get('/')

        self.assertEqual(str(response.context['user']), 'AnonymousUser')


class UserProfileViewTest(TestCase):
    '''Test for User Profile View'''
    def setUp(self):
        '''Method setup that sets the user credentials'''
        user = User.objects.create_user(username='test', password='password')
        user.save()

    def test_profile_page_view(self):
        '''Method to test the profile page views is being rendered after login'''
        self.client.login(username='test', password='password')
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)

    def test_home_template_use(self):
        '''Method to test if the correct profile template was used'''
        self.client.login(username='test', password='password')
        response = self.client.get('/profile')
        self.assertTemplateUsed(response, 'users/profile.djhtml')

    def test_redirect_if_user_not_logged_in(self):
        '''Test redirect to login page when unauthenticated user requests /profile'''
        response = self.client.get('/profile', follow=True)
        self.assertRedirects(response, '/login?next=/profile')


# Create your tests here.
class UsersViewTest(TestCase):
    '''Class to test the Users views'''

    def setUp(self):
        '''Method setup that sets the user credentials'''
        user = User.objects.create_user(username='test', password='password')
        user.save()

    def test_index_from_url(self):
        '''Test returns true when index is redered properly with URL'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_from_url(self):
        '''Test returns true when login is redered properly with URL'''
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_user_logout_view(self):
        '''Test returns true when user is logged out and redirected to home page'''
        self.client.login(username='test', password='password')
        self.client.get(reverse('users:logout'))
        response = self.client.get('/')
        self.assertEqual(str(response.context['user']), 'AnonymousUser')
        self.assertEqual(response.status_code, 200)

    def test_signup_from_name(self):
        '''Test returns true when signup index is redered properly with name'''
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_profile_from_name(self):
        '''Test returns true when profile index is redered properly with name'''
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
