"""


# 设置allure结果报告
# 1、解压 allure-2.17.1.zip
# 2、然后配置环境变量： 在系统变量path中添加 ....\bin，然后确定保存。

# 下载 allure-pytest 插件，用来生成 Allure 测试报告所需要的数据。
# pip3 install allure-pytest

第一步：将测试数据打包
pytest 脚本目录 --alluredir 存放报告目录
第二步：生成测试报告
allure generate -o 运行结果目录 存放报告目录 --clean # 清空
# 第三步：pyChram要重新启动 加载 否则报： 找不到 allure

问题：
控制台乱码 改为 gbk或者utf8: https://www.jb51.net/article/154697.htm
报告生成为空问题：重新启动 pycharm
=============================
"""

import pytest, os

if __name__ == '__main__':
    pytest.main(['--alluredir', './report/allure_json', '--clean-alluredir',
                 r'C:\Users\XG\Desktop\pythongaojifuxi\03pytest\test_3pytest_测试固件'])
    os.system('allure generate report/allure_json -o report/allure_report --clean')
