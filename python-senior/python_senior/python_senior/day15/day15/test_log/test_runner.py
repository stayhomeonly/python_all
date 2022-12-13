"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-14:03
知识点: 
---------------------------------
"""
import pytest
import os

"""
使用allure生成测试报告
        1.https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/ 官网下载allure的zip压缩包
        2.解压到tools目录下，如：D:/tools/allure-2.17.0/bin
        3.添加allure的bin目录到环境变量path当中
        4.在cmd命令行数allure --version 回车，验证是否安装成功
        5.在cmd命令行输入pip install allure-pytest 安装pytest框架的allure插件
"""

if __name__ == '__main__':
    pytest.main(["--alluredir", './report/allure_json', '--clean-alluredir', './'])
    os.system('allure generate report/allure_json -o report/allure_report --clean')
