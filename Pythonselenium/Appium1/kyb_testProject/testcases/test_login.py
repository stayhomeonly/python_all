"""
#@Time：2022/5/16-16:56
#@file：test_login
#@Project:Pythonselenium
#@Content:

"""
import logging
import unittest

from Appium1.kyb_testProject.buisnessView.loginView import LoginView
from Appium1.kyb_testProject.common.myunit import StartEnd


class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    def test_login_zxw2018(self):
        logging.info('=======test_login_zxw2018=========')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())


if __name__ == '__main__':
    unittest.main()
