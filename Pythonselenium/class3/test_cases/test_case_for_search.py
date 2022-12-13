"""
#@Time：2022/5/24-18:10
#@file：test_case
#@Project:python_basic05.py
#@Content:

"""
import unittest
# 测试用例的设计
from time import sleep

from ddt import ddt, file_data, data, unpack
from selenium import webdriver

from class3.page_object.index_bage import IndexPage
from class3.page_object.login_bage import LoginPage


@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data('../data/user.yaml')  # 要想走一个浏览器，登录的时候用一个正确的就行
    def test_1_login(self, username, password):
        self.lp.login(username, password)

        sleep(3)

    @data('衣服', '手机', '电脑')
    def test_2_search(self, txt):
        self.ip.search(txt=txt)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
