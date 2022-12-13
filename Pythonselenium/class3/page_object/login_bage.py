"""
#@Time：2022/5/22-18:02
#@file：login_bage
#@Project:python_basic05.py
#@Content:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from class3.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 核心元素
    user = (By.XPATH, '//input[@name="accounts"]')
    password = (By.XPATH, '//input[@name="pwd"]')
    login_button = (By.XPATH, '//button[text()="登录"]')

    def login(self, username, pwd):
        self.visit(self.url)
        self.input_(self.user, username)
        self.input_(self.password, pwd)
        self.click(self.login_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = 'xuzhu666'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(username, password)
