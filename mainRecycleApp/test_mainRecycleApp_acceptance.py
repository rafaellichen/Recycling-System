# import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class VisitorSearchTest(StaticLiveServerTestCase):

	fixtures = ['centers.json']
	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		self.driver.quit()

	def test_integration_facility_lookup(self):
		'''Test facility lookup form'''

		self.driver.get(self.live_server_url)
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

		# zipcode_text_field.send_keys('11104')

		type_button.click();

		zipcode_submit.click();

		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, "card-block"))
		)

		try:
			results_exist = self.driver.find_element_by_id("result-ok")
		except NoSuchElementException:
			results_exist = False

		self.assertTrue(results_exist)
