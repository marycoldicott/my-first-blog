from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_add_photo_to_current_cv(self):
		# Mary logs onto her CV on the web
		# She sees a blank space where her photo should be and the title Photo
		# She clicks on the photo header to add a photo
		# She enters a URL on the add photo to cv form and clicks submit
		# The photo is now displayed as part of her CV - redirected to full CV
		time.sleep(1)
		self.fail('Finish the test!')

	def test_edit_photo_in_current_cv(self):
		# Mary logs onto her CV on the web
		# She decides she needs to update her current photo
		# She clicks on the photo header and see's her current photo displayed
		# She enters a new URL on the add photo to cv form and clicks submit
		# She is redirected to her CV page
		self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')