"""
--------------------------------
@Time    :  2022/1/24 - 17:37 
@Author  :  Lee
@File    :  constants 
--------------------------------
"""
import os

"""
使用常量对路径进行管理
好处: 代码使用非绝对路径,可移植性高
"""

# 获取项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(os.path.dirname(__file__))
# print(BASE_DIR)  # D:/PythonWorkSpace/autotest

# 测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')
# print(CASE_DIR)  # D:/PythonWorkSpace/autotest\testcases

# 测试数据所在路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
print(DATA_DIR)
DATA_FILE = os.path.join(DATA_DIR, 'cases.xlsx')
# print(DATA_FILE)  # D:/PythonWorkSpace/autotest\datas\cases.xlsx


