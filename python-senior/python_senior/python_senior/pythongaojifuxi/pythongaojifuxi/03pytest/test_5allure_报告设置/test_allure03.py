"""
•	allure.dynamic.feature
•	allure.dynamic.link
•	allure.dynamic.issue
•	allure.dynamic.testcase
•	allure.dynamic.story
•	allure.dynamic.title
•	allure.dynamic.description

"""
import allure, os

# epic 项目名称描述
import pytest


@allure.epic('[epic] 淘宝电商系统测试')
# feature 模块名称
class TestLogin:
    allure.dynamic.feature('[feature] 淘宝电商系统登录模块测试')

    def test_login01(self):
        allure.dynamic.story("[story] 登录用例01")  # 测试用例
        allure.dynamic.title('[Title] 验证正确的用户名和密码能否成功登录')
        assert False

    # @allure.story('[story] 登录用例02')
    # @allure.title('[Title] 验证错误的用户名和密码能否正确处理')
    def test_login02(self):
        allure.dynamic.story("[story] 登录用例02")  # 测试用例
        allure.dynamic.title('[Title] 验证错误的用户名和密码能否正确处理')
        assert True


if __name__ == '__main__':
    # # 冒烟情况下，只运行主流程
    pytest.main(['--alluredir', './reports/allure_json', '--clean-alluredir', r'./test_allure03.py'])
    # 把json格式的结果，转换为html格式  --clean 新生成的报告会每次覆盖老的报告
    # os.system('allure generate ./reports/allure_json -o ./reports/allure_report --clean')
    os.system('allure generate ./reports/allure_json -o ./reports/allure_report --clean')
