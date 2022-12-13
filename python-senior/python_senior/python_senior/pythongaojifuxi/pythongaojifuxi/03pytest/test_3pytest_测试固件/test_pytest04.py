"""
================================
  Author   :  Lee
  FileName :  test_pytest04
  Date     :  2022/8/8 - 16:34
================================
"""
import pytest

"""

测试固件(测试夹具)的作用，能够在测试方法、测试类、测试模块、测试包、测试会话 前或者后 做一些事情。
测试固件的声明: @pytest.fixture(scope='作用域') 如果声明固件时设置autouse=True会自动使用固件
测试固件的使用: 
        1、手动添加：固件不使用autouse=True，并且在需要的地方添加: @pytest.mark.usefixtures("固件名1")
        2、自动添加：固件使用autouse=True，会根据固件作用域自动添加。

# 固件配置文件:
    python会自动加载当前目录下的conftest.py文件里的自定义的测试固件,一般可以在根目录里定义通用的自定义测试固件
    注意: conftest.py和pytest.ini文件一样都是系统规定的名字
"""


class TestFixture:

    def test_case01(self):
        print('开始执行case1!')

    def test_case02(self):
        print('开始执行case2!')


class TestFixture02:

    def test_case03(self):
        print('开始执行case3!')

    def test_case04(self):
        print('开始执行case4!')


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest04.py'])
