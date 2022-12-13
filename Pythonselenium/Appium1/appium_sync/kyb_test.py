"""
#@Time：2022/6/14-21:06
#@file：kyb_test
#@Project:Pythonselenium
#@Content:

"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class KybTest(object):
    def __init__(self,driver):
        self.driver = driver

    def check_cacelBtn(self):
        print('check cacelBtn')
        try:
            cacelBtn = self.driver.find_element(By.ID, 'android:id/button2')
        except NoSuchElementException:
            print("no cacelBtn")
        else:
            cacelBtn.click()

    check_cacelBtn()


    def check_skipBtn(self):
        print('check skipBtn')

        try:
            skipBtn = self.driver.find_element(By.ID, 'com.tal.kaoyan:id/tv_skip')
        except NoSuchElementException:
            print("no skipBtn")
        else:
            skipBtn.click()


    def skip_update_guide(self):
        self.check_cacelBtn()
        self.check_skipBtn()