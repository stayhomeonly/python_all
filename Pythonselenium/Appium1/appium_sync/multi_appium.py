"""
#@Time：2022/6/4-16:13
#@file：multi_appium
#@Project:Pythonselenium
#@Content:

"""
import subprocess
from time import ctime


def appium_start(host, port):
    '''启动appium服务'''
    bootstrap_port = str(port + 1)
    cmd = 'start -b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    # cmd = 'start  appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    print('%s at  %s' % (cmd, ctime()))
    '''去掉 -b 可以显示cmd窗口'''


    subprocess.Popen(cmd, shell=True, stdout=open('./appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4728
    appium_start(host, port)
