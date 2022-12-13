# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
=============================
"""

'''
1、pytest作用:     用来管理和运行测试用例
2、pytest安装:     pip install  pytest
3、查看pytest版本:   pytest --version
4、测试用例编写规则:
    测试文件以test_开头（以_test结尾也行）
    测试类以Test开头，并且不能带有init方法
    测试函数以test开头
    断言使用基本的assert即可

'''

import pytest, requests


class TestLogin:
    # 1.正确流程
    def test_login01(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={"username": "xiaohua", "password": "a123456"})
        res = response.json()
        print(res)
        assert {'code': '1000', 'msg': '登录成功'} == res

    # 2.用户名错误
    def test_login02(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={"username": "xiaoniu1", "password": "a123456"})
        res = response.json()
        print(res)
        assert "用户名或密码错误" in str(res)

    # 3.用户名为空
    def test_login03(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={"username": "", "password": "a123456"})
        res = response.json()
        print(res)
        assert res["msg"] == "用户名不能为空！" and res["code"] == "1003"  # 断言响应结果中的value值是否和预期结果一致

    # 4.密码错误
    def test_login04(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={"username": "xiaoniu", "password": "a1234567"})
        res = response.json()
        print(res)
        assert {'code': '1005', 'msg': '用户名或密码错误！'} == res

    # 5.密码为空
    def test_login05(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={"username": "xiaoniu", "password": ""})
        res = response.json()
        print(res)
        assert {'code': '1004', 'msg': '密码不能为空！'} == res


if __name__ == "__main__":
    # 知识点1: 运行该模块下的所有测试用例  -s -v -q
    pytest.main(['-vs', './test_pytest01.py'])  # 运行指定模块

    # 知识点2: -s -v -q的应用
    # pytest.main(['-s', './test_pytest01.py'])  # 运行指定模块, -s: 显示程序中的打印和日志信息
    # pytest.main(['-v', './test_pytest01.py'])  # 运行指定模块, -v: 丰富信息模式, 输出更详细的用例执行信息
    # pytest.main(['-q', './test_pytest01.py'])  # 运行指定模块, -q: 静默模式,只显示运行结果

    # 知识点3: 运行模块中的某个类
    # pytest.main(['./test_pytest01.py::TestLogin'])  # 运行类中的指定用例

    # 知识点4: 运行某个测试类中的指定用例
    # pytest.main(['./test_pytest01.py::TestLogin::test_login05'])  # 运行模块中的指定用例
    # pytest.main(['-vs', './test_pytest01.py::TestLogin::test_login05'])

    # 知识点5:运行某个目录下的所有测试用例
    # pytest.main(['./'])  # 运行当前目录下所有(test_*.py  和 *_test.py)
    # pytest.main([r'D:\dev_tools\python_project\python高级复习\4pytest\test_1pytest常规功能'])  # 运行./test1_pytest_test_1pytest常规功能 目录下所有的用例
