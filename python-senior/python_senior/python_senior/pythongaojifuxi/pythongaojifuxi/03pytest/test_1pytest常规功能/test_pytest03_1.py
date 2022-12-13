# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
=============================
"""

'''
分级运行：我们有的时候，在运行测试用例的过程中，想要运行部分测试用例，可以用 mark进行分级
工作中的使用场景：冒烟测试，分模块执行测试用例。
比如：现在自动化代码运行过程中，1000条测试用例，有200条报错，我们需要先跑主干流程，也就是核心测试用例。
'''

import pytest


class TestLogin:
    # 登录成功
    @pytest.mark.P1
    def test_login01(self):
        assert 1 == 1

    # 用户名错误
    @pytest.mark.P0
    def test_login02(self):
        assert "H" in "Hello World"

    @pytest.mark.P2
    @pytest.mark.P0
    def test_login03(self):
        assert 3 == 3


if __name__ == "__main__":
    # 知识点1: 运行该模块下的所有测试用例  -s -v -q
    # pytest.main(['-vs','./test_pytest03_1.py'])  # 运行指定模块
    pytest.main(['-vs', "-m P0 or P2", './test_pytest03_1.py'])  # 运行指定模块
