"""
=========================
File Name:constants
Author:冯鑫
Date:2021/12/9-11:16
==========================
"""
import os

# 获取项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # __file__当前文件名,全部大写代表常量
# print(BASE_DIR)  # D:/PythonWorkSpace/autotest02


# 配置文件所在路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')
CONF_FILE = os.path.join(CONF_DIR, 'config.ini')
