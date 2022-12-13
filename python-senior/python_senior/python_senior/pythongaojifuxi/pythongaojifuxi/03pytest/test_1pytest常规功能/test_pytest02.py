# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
=============================
"""

'''
断言分两种：一种是python自带的断言方式,另外一种是多重断言。
1、assert断言：是python自带的断言方式：多个assert断言在执行时，一个失败，后面的断言将不再执行
    assert A == B
    assert 3>4
    assert a in b
2、多重断言：
    使用前提：需要安装 pytest-check 插件
    pip install pytest-check 特点：也可以写多个断言，但一个失败，后面的断言将**继续**执行
3、选择：一个函数中有多个断言，并且我们希望断言失败后执行其他内容那么我们使用 多重断言
'''

import pytest


class TestAssume1:

    # def testAssert1(self):
    #     assert 1 + 4 == 5
    #
    # def testAssert2(self):
    #     assert "y" in "python"
    #     assert 8 + 5 > 9
    #
    # def testAssert3(self):
    #     assert 8 + 5 > 9

    # def testAssert3(self):
    #     """用例1"""
    #     print('执行test_01断言1')
    #     assert 0 == 1
    #     print('执行test_01断言2')
    #     assert 1 == 2

    def testAssert4(self):
        # print('执行test_01断言1')
        pytest.assume(0 == 1)
        print('执行test_01断言2')
        pytest.assume(2 == 2)
        print('执行test_01断言2完成')


if __name__ == "__main__":
    # 知识点1: 运行该模块下的所有测试用例  -s -v -q
    # pytest.main(['-vs', './test_pytest02.py'])  # 运行指定模块
    # 报错需要忽略报错信息
    pytest.main(['-vs', './test_pytest02.py'])
