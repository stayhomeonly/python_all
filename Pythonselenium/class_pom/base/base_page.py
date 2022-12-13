"""
#@Time：2022/5/16-20:20
#@file：base_page
#@Project:Pythonselenium
#@Content:

"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
基类，提供所有的常用函数，进行二次封装，便于页面对象的调用
"""
from selenium import webdriver


class BasePage:

    # 提供一个构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def loctor(self, loc):  # loc元组
        return self.driver.find_element(*loc)

    # 显示等待
    def wait_(self,driver,loc):# 不确定对错
        self.driver = driver
        WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(*loc))


    # def loctor(self, ele, loc):
    #     return self.driver.find_element(ele, loc)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 输入
    def input(self,  loc, txt):
        self.loctor(loc).send_keys(txt)

    # 点击
    def click(self,  loc):
        self.loctor( loc).click()

    # 等待
    def sleep(self, time_):
        sleep(time_)

    # 定位frame
    def frame_(self,  loc):
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
    url ="http://www.baidu.com"
    a=BasePage(driver)
    a.open(url)
    a.wait_(driver,(By.ID,'kw'))
