# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2022/5/13-22:12
   contents:添加标签
=============================
"""
import allure, os

# epic 项目名称描述
import pytest


@allure.epic('[epic] 淘宝电商系统测试')
# feature 模块名称
@allure.feature('[feature] 淘宝电商系统登录模块测试')
class TestLogin:
    # 用例
    @allure.story('[story] 登录用例01')
    # 用例标题
    @allure.title('[Title] 验证正确的用户名和密码能否成功登录')
    # 管理测试用例的链接地址
    @allure.testcase(url='http://127.0.0.1/zentao/www/index.php?m=testcase&f=view&caseID=17&version=1', name='用例连接')
    # 管理缺陷的链接地址
    @allure.issue(url='http://127.0.0.1/zentao/www/index.php?m=bug&f=browse&productID=4', name='缺陷地址')
    # 用例描述
    @allure.description('登录测试用例 执行人：老王')
    # 定义一个链接
    @allure.link(url='https://www.baidu.com/', name='百度搜索')
    def test_login01(self):
        # 用例步骤 写法二 用例步骤可写在方法内部
        with allure.step('步骤二：第一步:读取execl数据'):
            pass

        with allure.step('步骤二：第二步:调用登录接口'):
            pass

        with allure.step('步骤二：验证响应结果'):
            pass
        assert True

    @allure.story('[story] 登录用例02')
    @allure.title('[Title] 验证错误的用户名和密码能否正确处理')
    def test_login02(self):
        assert True

        with allure.step('步骤一：第一步:读取execl数据'):
            pass

        with allure.step('步骤二：第二步:调用登录接口'):
            pass

        with allure.step('步骤三：验证响应结果'):
            pass
        assert True


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports/allure_json', '--clean-alluredir', r'./test_allure02.py'])
    os.system('allure generate ./reports/allure_json -o ./reports/allure_report --clean')
