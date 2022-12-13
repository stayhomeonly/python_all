"""
#@Time：2022/4/26-16:54
#@file：kyb_register
#@Project:python_basic05.py
#@Content:

"""
import random
from time import sleep

from Appium1.find_element.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
sleep(3)

# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

username = 'zxw2018' + 'Fly' + str(random.randint(1000, 9999))
print('username:%s' % username)
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').click()
sleep(3)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
password = 'zxw2018' + str(random.randint(1000, 9999))
print('password:%s' % password)
#一定要先点击，在输入密码，才有效
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

email = '51zxw' + str(random.randint(1000, 9000)) + '@163.com'
print('email:%s' % email)
#一定要先点击，在输入邮箱，才有效
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').click()
sleep(3)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
sleep(3)
# 院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
sleep(3)
# 选择省份
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
sleep(3)
# 选择具体院校--同济大学
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()
sleep(3)

# 专业选择


driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
sleep(3)
# 选择经济学类-统计学-经济统计学
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
sleep(3)
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
sleep(3)
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()
sleep(3)

# 点击“进入考研帮”按钮

driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
'''
	
T886232rv
email='51zxw'+str（random.randint（1000,9000））+'@163.com' print（'email: %s' %email） 
driver.find_element_by_id（'com.tal.kaoyan:id/activity_register_email_edittext'）.click（） 
#加在这里解决了 driver.find_element_by_id（'com.tal.kaoyan:id/activity_register_email_edittext'）.send_keys（email） 
#driver.keyevent（61） #加在这里也可以解决 牛！ 感觉抱上大腿了。
'''