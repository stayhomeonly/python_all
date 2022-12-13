"""
#@Time：2022/5/31-20:33
#@file：multi_devices
#@Project:git_python
#@Content:

"""
'''
---------------------------
File Name:capability
Author:FENGXIN
date:2022/4/22-16:46

---------------------------

'''
# 启动两个服务，同步
import yaml
from time import ctime
from appium import webdriver
import multiprocessing

with open('desired_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def appium_desired(udid, port):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']

    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['automationName'] = data['automationName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid  # 用真机的时候就需要
    desired_caps['app'] = data['app']
    desired_caps['noReset'] = data['noReset']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    print('appium port :%s strat run %s at %s' % (port, udid, ctime())) # 打印启动时间

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    return driver


desired_process = []
for i in range(len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))
    desired_process.append(desired)

if __name__ == '__main__':
    for desired in desired_process:
        desired.start()  # 执行所有进程组
    for desired in desired_process:
        desired.join()
