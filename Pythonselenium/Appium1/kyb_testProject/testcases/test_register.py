import sys

path = 'D:\FENG1234\Pythonselenium\Appium1\kyb_testProject'
sys.path.append(path)
from Appium1.kyb_testProject.common.myunit import StartEnd
from Appium1.kyb_testProject.buisnessView.registerView import RegisterView
import logging
import random
import unittest


class RegisterTest(StartEnd):

    def test_user_register(self):
        logging.info('=========test_user_register======')
        r = RegisterView(self.driver)

        username = 'zxw2020' + 'FLY' + str(random.randint(1000, 9000))
        password = 'zxw1' + str(random.randint(1000, 9000))
        email = '51z11' + str(random.randint(1000, 9000)) + '@163.com'

        self.assertTrue(r.register_action(username, password, email))


if __name__ == '__main__':
    unittest.main()
