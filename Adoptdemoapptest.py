from selenium import webdriver
import unittest
import os
import HtmlTestRunner

class Adoptdemoapptest(unittest.TestCase):
	def setUp(self):
		remote_url='http://localhost:4444/wd/hub'
		self.driver = webdriver.Remote(command_executor=remote_url,desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	def test_demo(self):
		driver = self.driver
		driver.get('http://localhost:9005/')
		self.assertIn("localhost", driver.title)

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))