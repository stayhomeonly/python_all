"""
#@Time：2022/6/20-17:04
#@file：python_basic_14
#@Project:Pythonselenium
#@Content:

"""
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBasePage(unittest.TestCase):
    url = "http://www.baidu.com"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def test_search_selenium(self):
        input_box = self.driver.find_element(By.XPATH, '//input[@id="kw"]')
        input_box.send_keys("selenium")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()