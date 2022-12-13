"""
#@Time：2022/7/14-15:50
#@file：123
#@Project:python_new_study
#@Content:

"""
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://10.1.140.22:8080/gims/login/")
driver.maximize_window()
# 定位登录名
ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "_easyui_textbox_input1"))).send_keys("sob5187")
# 定位点击登录
ele1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnLogin"))).click()
# 定位公开市场投资
ele2 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/aside/section/main/div/div[1]/div/ul/li[6]/div")))


# ele3 = driver.find_element(By.XPATH,"/html/body/section/aside/section/main/div/div[1]/div/ul/li[6]/div")
# sleep(5)
# ele4 = driver.find_element_by_class_name("el-aside")
# sleep(3)
# action = ActionChains(driver)#实例化鼠标
# sleep(5)
# action.move_to_element(ele4)
# action.perform()