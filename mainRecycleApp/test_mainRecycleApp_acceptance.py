import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class VisitorSearchTest(StaticLiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		self.driver.quit()

	def test_user_can_enter_the_zip_code_and_view_the_result(self):
		self.driver.get('http://localhost:8000')
		self.assertIn('Home', self.driver.title)
		# Grab the zipcode text field
		zipcode_text_field = self.driver.find_element_by_name("zipcode")
		# Send a sample zipcode to the text-field
		zipcode_text_field.send_keys('11104')
		# Grab the submit button
		zipcode_submit = self.driver.find_element_by_id("submit-zip")

		# Click the button
		zipcode_submit.click();

		# expect an alert message
		self.assertEqual('Please select at least 1 type of recyclable waste', self.driver.switch_to.alert.text);

		# accept the alert
		self.driver.switch_to.alert.accept()

		type_button = self.driver.find_element_by_id("Automotive")

		zipcode_text_field.send_keys('11104')

		type_button.click();
		
		zipcode_submit.click();

		element = WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((By.ID, "result-card-block"))
		)

		self.assertEqual("Your search results:", self.driver.find_element_by_id("result-ok"))
