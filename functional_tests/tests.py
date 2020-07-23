from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
from django.contrib.auth.models import User

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		#self.client.force_login(User.objects.get_or_create(username="marycoldicott"))
		User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )

		self.browser = webdriver.Firefox()
		# to access the base url in tests
		self.browser.get(
			'%s%s' % (self.live_server_url,  "/admin/")
		)

        # Fill login information of admin
		username = self.browser.find_element_by_id("id_username")
		username.send_keys("admin")
		password = self.browser.find_element_by_id("id_password")
		password.send_keys("admin")

        # Locate Login button and click it
		self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
		self.browser.get(
			'%s%s' % (self.live_server_url, "/admin/auth/user/add/")
		)		

	def tearDown(self):
		self.browser.quit()

	def test_can_add_photo_to_cv(self):
		# Mary logs onto her CV on the web
		self.browser.get(self.live_server_url)
		cv_header = self.browser.find_element_by_id('cv-link')
		self.assertIn('CV', cv_header.text)
		cv_header.click()

		# She sees a blank space where her photo should be and the title Photo
		header_text = self.browser.find_element_by_id('photo-header')
		self.assertIn('Photo', header_text.text)

		# She clicks on the photo header to add a photo
		header_text.click()

		# She enters a URL on the add photo to cv form and clicks submit
		createbox = self.browser.find_element_by_id('create-button')
		createbox.click()

		header_text = self.browser.find_element_by_id('photo-header')
		header_text.click()

		inputbox = self.browser.find_element_by_id('url-input')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a photo URL'
		)

		inputbox.send_keys('https://image.shutterstock.com/image-photo/isolated-portrait-smiling-business-woman-260nw-684509272.jpg')

		submitbutton = self.browser.find_element_by_id('submit-button')
		submitbutton.click()

		# The photo is now displayed as part of her CV - redirected to full CV
		currenturl = self.browser.current_url
		self.assertIn(f'/cv/', currenturl)

		# Check photo exists on page
		photo = self.browser.find_element_by_id('cv-photo')
		self.assertEqual(photo.get_attribute('src'), 'https://image.shutterstock.com/image-photo/isolated-portrait-smiling-business-woman-260nw-684509272.jpg')


	def test_can_add_personal_detail_to_cv(self):
		# Mary logs onto her CV on the web
		self.browser.get(self.live_server_url)
		cv_header = self.browser.find_element_by_id('cv-link')
		self.assertIn('CV', cv_header.text)
		cv_header.click()

		# She sees a header that says "Personal"
		header_text = self.browser.find_element_by_id('personal-header')
		self.assertEqual('Personal', header_text.text)

		# She clicks this header and is redirected to a new page
		header_text.click()

		# She creates a new personal detail of Name, with the name Mary
		createbox = self.browser.find_element_by_id('create-button')
		createbox.click()

		header_text = self.browser.find_element_by_id('personal-header')
		header_text.click()

		selection = self.browser.find_element_by_id('personal-type')
		selection.send_keys('Name')

		inputbox = self.browser.find_element_by_id('personal-input')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a personal detail'
		)

		inputbox.send_keys('Mary')

		# She clicks submit
		submitbutton = self.browser.find_element_by_id('submit-button')
		submitbutton.click()

		# She sees the new detail added to her CV
		currenturl = self.browser.current_url
		self.assertIn(f'/cv/', currenturl)

		personal = self.browser.find_element_by_id('personal-all')
		self.assertIn("Mary", personal.text)


	def test_can_add_education_to_cv(self):
		# Mary logs onto her CV on the web
		self.browser.get(self.live_server_url)
		cv_header = self.browser.find_element_by_id('cv-link')
		self.assertIn('CV', cv_header.text)
		cv_header.click()

		# She sees a header that says "Education"
		header_text = self.browser.find_element_by_id('education-header')
		self.assertEqual('Education', header_text.text)

		# She clicks this header and is redirected to a new page
		header_text.click()

		# She creates a new education
		createbox = self.browser.find_element_by_id('create-button')
		createbox.click()

		header_text = self.browser.find_element_by_id('education-header')
		header_text.click()

		selection = self.browser.find_element_by_id('education-type')
		selection.send_keys('University')

		years = self.browser.find_element_by_id('years-input')
		years.send_keys('2018 - 2022')

		name = self.browser.find_element_by_id('institution-input')
		name.send_keys('University of Birmingham')

		qualifications = self.browser.find_element_by_id('qualifications-input')
		qualifications.send_keys('Degree of Bachelor of Science in Computer Science')

		other = self.browser.find_element_by_id('other-input')
		other.send_keys('First Year average of 80%')

		# She clicks submit
		submitbutton = self.browser.find_element_by_id('submit-button')
		submitbutton.click()

		# She sees the new detail added to her CV
		currenturl = self.browser.current_url
		self.assertIn(f'/cv/', currenturl)

		education = self.browser.find_element_by_id('education-all')
		self.assertIn("University of Birmingham", education.text)


	def test_can_add_experience_to_cv(self):
		# Mary logs onto her CV on the web
		self.browser.get(self.live_server_url)
		cv_header = self.browser.find_element_by_id('cv-link')
		self.assertIn('CV', cv_header.text)
		cv_header.click()

		# She sees a header that says "Work Experience"
		header_text = self.browser.find_element_by_id('experience-header')
		self.assertEqual('Work Experience', header_text.text)

		# She clicks this header and is redirected to a new page
		header_text.click()

		# She creates a new experience
		createbox = self.browser.find_element_by_id('create-button')
		createbox.click()

		header_text = self.browser.find_element_by_id('experience-header')
		header_text.click()

		selection = self.browser.find_element_by_id('experience-type')
		selection.send_keys('Current')

		role = self.browser.find_element_by_id('role-input')
		role.send_keys('Tech Degree Apprentice')

		dates = self.browser.find_element_by_id('dates-input')
		dates.send_keys('Summer 2019')

		employer = self.browser.find_element_by_id('employer-input')
		employer.send_keys('PwC')

		responsibilities = self.browser.find_element_by_id('responsibilities-input')
		responsibilities.send_keys('This is where I enter responsibilities')

		# She clicks submit
		submitbutton = self.browser.find_element_by_id('submit-button')
		submitbutton.click()

		# She sees the new detail added to her CV
		currenturl = self.browser.current_url
		self.assertIn(f'/cv/', currenturl)

		experience = self.browser.find_element_by_id('experience-all')
		self.assertIn("Tech Degree Apprentice", experience.text)


	def test_can_add_skill_to_cv(self):
		# Mary logs onto her CV on the web
		self.browser.get(self.live_server_url)
		cv_header = self.browser.find_element_by_id('cv-link')
		self.assertIn('CV', cv_header.text)
		cv_header.click()

		# She sees a header that says "Work Experience"
		header_text = self.browser.find_element_by_id('skills-header')
		self.assertEqual('Skills', header_text.text)

		# She clicks this header and is redirected to a new page
		header_text.click()

		# She creates a new experience
		createbox = self.browser.find_element_by_id('create-button')
		createbox.click()

		header_text = self.browser.find_element_by_id('skills-header')
		header_text.click()

		selection = self.browser.find_element_by_id('skill-type')
		selection.send_keys('Personal')

		skill = self.browser.find_element_by_id('skill-input')
		skill.send_keys('Microsoft Office')

		# She clicks submit
		submitbutton = self.browser.find_element_by_id('submit-button')
		submitbutton.click()

		# She sees the new detail added to her CV
		currenturl = self.browser.current_url
		self.assertIn(f'/cv/', currenturl)

		skills = self.browser.find_element_by_id('skills-all')
		self.assertIn("Personal", skills.text)


if __name__ == '__main__':  
    unittest.main(warnings='ignore')