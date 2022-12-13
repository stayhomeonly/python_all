import pytest,allure, os


@allure.epic('[epic] 淘宝电商系统测试')
# feature 模块名称
@allure.feature('[feature] 淘宝电商系统登录模块测试')
class TestLogin:
    # 用例
    @allure.story('[story] 登录用例01')
    def test_login01(self):
        # 用例步骤 写法二 用例步骤可写在方法内部
        with allure.step('步骤一：第一步:读取execl数据'):
            pass

        with allure.step('步骤二：第二步:调用登录接口'):
            pass

        with allure.step('步骤三：验证响应结果'):
            pass
        assert True

    @allure.story('[story] 登录用例02')
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
    pytest.main(['--alluredir', './reports/allure_json', '--clean-alluredir', r'./test_allure01.py'])
    os.system('allure generate ./reports/allure_json -o ./reports/allure_report --clean')
