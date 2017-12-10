import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class VisitorSearchTest(StaticLiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		self.driver.quit()

	def test_user_can_enter_the_zip_code_and_view_the_result(self):
		self.driver.get('http://localhost:8000')

		self.assertIn('Home', self.driver.title)

if __name__ == '__main__':
	unittest.main()