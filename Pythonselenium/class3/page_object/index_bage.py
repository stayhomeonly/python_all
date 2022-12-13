"""
#@Time：2022/5/24-18:16
#@file：index_bage
#@Project:python_basic05.py
#@Content:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from class3.base.base_page import BasePage


class IndexPage(BasePage):
    url = 'http://39.98.138.157/shopxo/'
    # 核心元素
    search_input = (By.XPATH, '//input[@id="search-input"]')
    search_button = (By.XPATH, '//input[@id="ai-topsearch"]')

    def search(self, txt):
        self.visit(self.url)
        self.input_(self.search_input, txt)
        self.click(self.search_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    IndexPage(driver).search(txt='手机')
