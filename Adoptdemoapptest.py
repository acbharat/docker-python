from selenium import webdriver
import unittest
import os

remote_url='http://localhost:4444/wd/hub'
driver = webdriver.Remote(command_executor=remote_url,desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
driver.implicitly_wait(30)
driver.maximize_window()

driver.get ('http://localhost:9005/')
print(driver.title)
driver.close()
driver.quit()