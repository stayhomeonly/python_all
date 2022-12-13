"""
#@Time：2022/6/1-21:41
#@file：123
#@Project:Pythonselenium
#@Content:

"""
import pytest


import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
CASE_DIR = os.path.join(BASE_DIR, 'test_cases')
# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'report')
REPORT_JSON = os.path.join(REPORT_DIR, 'allure_json')
REPORT_HTML = os.path.join(REPORT_DIR, 'allure_html')

if __name__ == '__main__':
    # 执行测试用例获得测试数据  数据的目录
    pytest.main(['-s','--alluredir','../allure-result'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system('allure generate ./allure-results -o ./reports')
# if __name__ == '__main__':
#     pytest.main(['-vs', '--alluredir', REPORT_JSON, CASE_DIR])
#     os.system('allure generate %s -o %s --clean' % (REPORT_JSON, REPORT_HTML))