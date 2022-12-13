"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-10:31
知识点: 
---------------------------------
"""
import requests

"""
使用pytest参数化数据，让测试数据和测试逻辑分离
"""
import pytest


class TestLogin:
    cases = [{"case_data": "{'username':'xiaohua','pwd':'a123456'}", "exp": '{"code": 1000, "msg": "登录成功"}'},
             {"case_data": "{'username':'','pwd':'a123456'}", "exp": '{"code": 1001, "msg": "用户名不能为空"}'},
             {"case_data": "{'username':'xiaohua','pwd':''}", "exp": '{"code": 1002, "msg": "密码不能为空"}'},
             {"case_data": "{'username':'xiaohua','pwd':'a1234'}", "exp": "{'code': 1007, 'msg': '用户名或者密码错误'}"},
             {"case_data": "{'username':'xiaohua1','pwd':'a123456'}", "exp": "{'code': 1007, 'msg': '用户名或者密码错误'}"}]

    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        response = requests.post(url="http://127.0.0.1:5000/login", data=eval(case["case_data"]))
        res = response.json()
        assert eval(case["exp"]) == res


if __name__ == '__main__':
    pytest.main(["-vs", "./"])