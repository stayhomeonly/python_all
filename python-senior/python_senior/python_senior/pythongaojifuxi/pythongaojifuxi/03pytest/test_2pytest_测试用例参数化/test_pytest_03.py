import requests, pytest

'''
使用 pytest.mark.parametrize(argnames, argvalues) 参数化测试,减少代码量
'''


class TestLogin(object):
    cases = [{"case_data": '{"username": "xiaohua", "password": "a123456"}', "exp": "{'code': '1000', 'msg': '登录成功'}"},
             {"case_data": '{"username": "xiaoniu1", "password": "a123456"}',"exp": "{'code': '1005', 'msg': '用户名或密码错误！'}"},
             {"case_data": '{"username": "", "password": "a123456"}', "exp": "{'code': '1003', 'msg': '用户名不能为空！'}"},
             {"case_data": '{"username": "xiaoniu", "password": "a1234567"}',"exp": "{'code': '1005', 'msg': '用户名或密码错误！'}"},
             {"case_data": '{"username": "xiaoniu", "password": ""}', "exp": "{'code': '1004', 'msg': '密码不能为空！'}"}]

    @pytest.mark.parametrize('case', cases)
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data=eval(case['case_data']))
        res = response.json()
        print(res)
        assert eval(case['exp']) == res


if __name__ == '__main__':
    pytest.main(['-v', '-s', './test_pytest_03.py'])
