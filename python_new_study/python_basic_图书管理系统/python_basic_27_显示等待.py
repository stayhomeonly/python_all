"""
#@Time：2022/7/14-16:46
#@file：234
#@Project:python_new_study
#@Content:

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://10.1.140.22:8080/gims/login/")
driver.maximize_window()
# 定位登录名
longin1=driver.find_element(By.XPATH,'//input[@id="_easyui_textbox_input1"]').send_keys("sob5187")
sleep(5)
#点击登录
driver.find_element(By.XPATH,'//a[@id="btnLogin"]').click()

# 定位公开市场投资

# 显示等待
ele2 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/aside/section/main/div/div[1]/div/ul/li[6]/div"))).click()
sleep(3)
ele2 =driver.find_element(By.XPATH,'/html/body/section/aside/section/main/div/div[1]/div/ul/li[6]/div/span').click()


sleep(5)

