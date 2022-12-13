"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-15:38
知识点: 
---------------------------------
"""
# pytest 发现测试用例的默认规则  1.文件名（模块名）test_开头或者以_test 结尾 2.类名 Test 3.方法名 test开头

import pytest, requests
import allure


@allure.epic("星光项目接口")
@allure.feature("登录接口")
@pytest.mark.P0
class TestLogin:
    datas = [{'case_data': {'username': 'xiaozhen', 'password': 'a123456', 'typeId': '101'}, 'exp': '登录成功'},
             {'case_data': {'username': '', 'password': 'a123456', 'typeId': '101'}, 'exp': '用户名不能为空'},
             {'case_data': {'username': 'xiaozhen', 'password': '', 'typeId': '101'}, 'exp': '密码不能为空'}
             ]

    @allure.description("星光项目接口自动化-登录接口")
    @allure.severity("critical")
    @allure.title("星光项目_token_login")
    @pytest.mark.parametrize('data', datas)  # 第一个入参 str  变量 用来接收数据源的数据   2.数据源要求失list或者tuple类型
    def test_login(self, data):  # 我们要讲变量作为入参传到测试方法里面才能参数化 测试用例
        allure.attach(body=str(data["case_data"]), name="请求参数")

        with allure.step("发起请求:"):
            res = requests.get(url='http://127.0.0.1:6666/business/token_login', params=data['case_data'])
            res = res.json()

        allure.attach(body=data["exp"], name='预期结果')
        assert data['exp'] in str(res)
