"""
#@Time：2022/5/20-21:00
#@file：registerView
#@Project:python_basic05.py
#@Content:

"""
import logging
import random
from time import sleep

from Appium1.kyb_testProject.common.comm_fun import Common, By, NoSuchElementException
from Appium1.kyb_testProject.common.desired_caps import appium_desired


class RegisterView(Common):
    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')
    save = (By.ID, 'com.tal.kaoyan:id/save')

    # 用户名密码邮箱相关元素
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    # 完善资料界面元素
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    # 院校相关元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    # 专业相关元素
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    # 用户中心相关元素
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self, register_username, register_password, register_email):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('======register_action======')
        sleep(3)
        self.driver.find_element(*self.register_text).click()

        logging.info('set userhead')
        sleep(2)
        self.driver.find_element(*self.userheader).click()
        sleep(2)
        self.driver.find_elements(*self.item_image)[1].click()
        sleep(2)
        self.driver.find_element(*self.save).click()
        sleep(2)

        logging.info('username is %s' % register_username)

        self.driver.find_element(*self.register_username).send_keys(register_username)

        sleep(2)

        logging.info('password is %s' % register_password)
        # 一定要在输入密码之前先点击这个输入框，不然的话输入会无效
        self.driver.find_element(*self.register_password).click()
        self.driver.find_element(*self.register_password).send_keys(register_password)

        sleep(2)

        sleep(2)

        logging.info('email is %s' % register_email)
        # 一定要在输入邮箱之前先点击这个输入框，不然的话输入会无效
        self.driver.find_element(*self.register_email).click()
        self.driver.find_element(*self.register_email).send_keys(register_email)

        sleep(2)

        self.driver.find_element(*self.register_btn).click()
        sleep(2)

        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error('register fail !')
            self.getScreenShot('register fail')
            return False
        else:
            self.add_register_info()
            if self.check_register_status():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info('======add_register_info=====')

        logging.info('select school...')
        self.driver.find_element(*self.perfectinfomation_school).click()
        sleep(2)
        self.find_elements(*self.forum_title)[1].click()
        sleep(2)
        self.find_elements(*self.university)[1].click()
        sleep(2)

        logging.info('select major...')
        self.driver.find_element(*self.perfectinfomation_major).click()
        sleep(2)
        self.driver.find_elements(*self.major_subject_title)[1].click()
        sleep(2)
        self.driver.find_elements(*self.major_group_title)[2].click()
        sleep(2)
        self.driver.find_elements(*self.major_search_item_name)[1].click()
        sleep(2)

        self.driver.find_element(*self.perfectinfomation_goBtn).click()

    def check_register_status(self):
        logging.info('=====check_register_status=====')
        self.check_market_ad()
        try:
            self.driver.find_element(*self.button_mysefl).click()
            sleep(2)
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('register fail!')
            self.getScreenShot('register fail')
            return False
        else:
            logging.info('register success!')
            return True


if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)

    username = 'zxw2019' + 'FLY' + str(random.randint(1000, 9000))
    password = 'zxw12' + str(random.randint(1000, 9000))
    email = '51zxw1' + str(random.randint(1000, 9000)) + '@163.com'

    register.register_action(username, password, email)
