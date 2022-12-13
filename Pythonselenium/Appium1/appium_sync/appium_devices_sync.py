"""
#@Time：2022/6/13-20:57
#@file：appium_devices_sync
#@Project:Pythonselenium
#@Content:

"""
import multiprocessing
from time import sleep

from Appium1.appium_sync.check_port import *
from Appium1.appium_sync.multi_appium import appium_start
from Appium1.appium_sync.multi_devices import appium_desired

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def start_appium_action(host, port):
    '''检测端口是否被占用，如果没有被占用则启动appium服务'''
    if check_port(host, port):
        appium_start(host, port)
        return True
    else:
        print('appium %s start fail' % port)


def start_devices_action(udid, port):
    '''先检测appium服务是否启动成功，启动成功则再启动App,否则释放端口'''
    host = '127.0.0.1'
    if start_appium_action(host, port):
        appium_desired(udid, port)
    else:
        release_port(port)


def appium_start_sync():
    print('========appium_start_sync======')
    # 构建appium进程组
    appium_process = []

    # 加载appium进程

    for i in range(len(devices_list)):
        host = '127.0.0.1'
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        appium_process.append(appium)

    # 启动appium服务
    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    sleep(5)


def devices_star_sync():
    '''并发启动设备'''
    print('===devices_start_sync===')

    # 定义desired进程组
    desired_process = []

    # 加载desired进程
    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        desired = multiprocessing.Process(target=start_devices_action, args=(devices_list[i], port))
        desired_process.append(desired)

    # 并发启动App
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


if __name__ == '__main__':
    appium_start_sync()
    devices_star_sync()
