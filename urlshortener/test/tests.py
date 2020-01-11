import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

class MySeleniumTests(unittest.TestCase):

	def setUp(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--incognito")
		self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'D:\Projects\chromedriver.exe')
		self.custom_short_url = "test18"

	def tearDown(self):
		self.driver.quit()

	def create_url(self):
		self.driver.get('http://localhost:8000/')
		url_input = self.driver.find_element_by_name("url")
		url_input.send_keys('https://www.python.org/')
		short_url_input = self.driver.find_element_by_name("short")
		short_url_input.send_keys(self.custom_short_url)
		self.driver.find_element_by_xpath('//input[@value="Go!"]').click()
		time.sleep(5)

	def test_url_creation_flow(self):
		self.create_url()
		self.assertTrue('http://localhost:8000/short/'+self.custom_short_url in self.driver.find_element_by_id("short_url").get_attribute('innerHTML'))
		self.create_url()
		self.assertFalse('http://localhost:8000/short/'+self.custom_short_url in self.driver.find_element_by_id("short_url").get_attribute('innerHTML'))
		self.assertTrue('already exists!' in self.driver.page_source)
		self.driver.get('http://localhost:8000/short/'+self.custom_short_url)
		self.assertTrue("Python" in self.driver.title)


if __name__ == "__main__":
    unittest.main()