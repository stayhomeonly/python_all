"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-15:38
知识点: 
---------------------------------
"""
# pytest 发现测试用例的默认规则  1.文件名（模块名）test_开头或者以_test 结尾 2.类名 Test 3.方法名 test开头

import pytest, requests


class TestLogin():
    datas = [{'case_data': {'username': 'xiaozhen', 'password': 'a123456', 'typeId': '101'}, 'exp': '登录成功'},
             {'case_data': {'username': '', 'password': 'a123456', 'typeId': '101'}, 'exp': '用户名不能为空'},
             {'case_data': {'username': 'xiaozhen', 'password': '', 'typeId': '101'}, 'exp': '密码不能为空'}
             ]

    @pytest.mark.parametrize('data', datas)  # 第一个入参 str  变量 用来接收数据源的数据   2.数据源要求失list或者tuple类型
    def test_login(self, data):  # 我们要讲变量作为入参传到测试方法里面才能参数化 测试用例
        res = requests.get(url='http://127.0.0.1:6666/business/token_login', params=data['case_data'])
        res = res.json()
        print(res)
        # assert data['exp'] == res['msg']
        assert data['exp'] in str(res)


if __name__ == '__main__':
    pytest.main(['-vs', './test_login'])

