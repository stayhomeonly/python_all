"""
#@Time：2022/7/14-17:34
#@file：456
#@Project:python_new_study
#@Content:

"""

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    # 提供一个构造函数
    def __init__(self, driver):
        self.driver = driver

    # 显示等待定位元素点击
    def webdriver_wait_click(self, *loc):

        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(*loc)).click()  # 不确定对错

    # 显示等待定位元素输入
    def webdriver_wait_input(self,txt, *loc):
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(*loc)).send_keys(txt)

    # 元素定位
    def loctor(self, loc):  # loc元组
        return self.driver.find_element(*loc)

    # def loctor(self, ele, loc):
    #     return self.driver.find_element(ele, loc)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 输入
    def input(self, loc, txt):
        self.loctor(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.loctor(loc).click()

    # 等待
    def sleep(self, time_):
        sleep(time_)

    # 定位frame
    def frame_(self, loc):
        """
        :return: 切入frame
        """
        sleep(1)
        self.driver.switch_to.frame(self.loctor(loc))

    def parent_frame(self):
        """
        :return: 切出frame
        """

        self.driver.switch_to.parent_frame()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # url = "https://www.126.com/"
    # t = BasePage(driver)
    # t.open(url)
    #
    # # iframe1 = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
    # t.frame_((By.XPATH, '//*[@id="loginDiv"]/iframe'))
    # t.input((By.XPATH, '//input[@name="email"]'), "m15161039042")
    # t.input((By.XPATH, '//input[@name="password"]'), "FENG1234.")
    # t.click((By.XPATH, '//a[@id="dologin"]'))
    url = "http://www.baidu.com"
    a = BasePage(driver)
    a.open(url)
    a.webdriver_wait_input("selenium",(By.ID, 'kw'))
