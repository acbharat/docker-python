from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions


driver = webdriver.Chrome()
chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
chrome.get ('http://localhost:9005/')
print(chrome.title)
