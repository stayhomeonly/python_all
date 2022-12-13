"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-10:50
知识点: 
---------------------------------
"""
"""
对注册接口进行参数化，并且运行测试用例成功
"""
import pytest, requests


class TestRegister:
    cases = [{
        "case_data": "{'username':'xiaoliu','pwd':'a123456','re_pwd':'a123456',"
                     "'phone':'13487280000','email':'123@qq.com'}",
        "exp": '{"code": 1000, "msg": "注册成功"}'},{
        "case_data": "{'username':'xiaoliu1','pwd':'a123456','re_pwd':'123456',"
                     "'phone':'13487280001','email':'124@qq.com'}",
        "exp": '{"code": 1003, "msg": "两次密码输入不一致"}'},{
        "case_data": "{'username':'xiaoliu2','pwd':'a2345','re_pwd':'a2345',"
                     "'phone':'13487280002','email':'125@qq.com'}",
        "exp": '{"code": 1006, "msg": "用户名和密码必须在6-18位之间"}'},{
        "case_data": "{'username':'xiaoliu3','pwd':'a123456','re_pwd':'a123456',"
                     "'phone':'13487280003','email':'126@'}",
        "exp": '{"code": 1008, "msg": "邮箱格式错误"}'},]

    @pytest.mark.parametrize("case", cases)
    def test_register(self, case):
        response = requests.post(url="http://127.0.0.1:5000/register", data=eval(case["case_data"]))
        res = response.json()
        assert eval(case["exp"]) == res


if __name__ == '__main__':
    pytest.main(['./test_Parameter03.py'])