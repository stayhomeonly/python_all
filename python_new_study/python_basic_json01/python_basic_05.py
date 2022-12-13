"""
#@Time：2022/6/20-16:31
#@file：python_basic-05
#@Project:python_new_study
#@Content:

"""

import unittest
from time import sleep

from selenium import webdriver


class TestBaidu(unittest.TestCase):
    base_url = "http://www.baidu.com"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        print("窗口打开成功")

    def test_search_key_selenium(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "selenium_百度搜索")
        print("窗口打开成功")

    def test_search_key_unttest(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "unittest_百度搜索")
        print("窗口打开成功")

    def tearDown(self):
        self.driver.quit()
        print("窗口退出成功")


if __name__ == '__main__':
    unittest.main()
