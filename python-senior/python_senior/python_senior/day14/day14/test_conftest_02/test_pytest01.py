"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-11:23
知识点: 
---------------------------------
"""
import pytest

"""
测试固件(测试夹具)
使用固件的四种方式：
            1.@pytest.fixture(autouse=True) :声明固件时设置autouse=True会自动使用固件
            2.在需要使用固件的case参数传入固件函数名即可
            3.在需要使用固件的case上使用装饰器@pytest.mark.usefixtures('固件名')
            4.conftest.py 配置固件
"""


# 1.@pytest.fixture(autouse=True) :声明固件时设置autouse=True会自动使用固件
# @pytest.fixture(scope='function', autouse=True)  # 默认使用的就是基于方法的夹具，可以定义一个scope用来规定作用域
# def function():
#     print("\r---------------------自动执行之前---------------------")
#     yield
#     print("\r---------------------自动执行之后---------------------")
#
#
# class TestFixture:
#     def test_fixture01(self):
#         print("\t执行test01测试用例")
#
#     def test_fixture02(self):
#         print("\t执行test02测试用例")
#
#     def test_fixture03(self):
#         print("\t执行test03测试用例")

# 2.在需要使用固件的case参数传入固件函数名即可
# @pytest.fixture()
# def function():
#     print("\r---------------------自动执行之前---------------------")
#     yield
#     print("\r---------------------自动执行之后---------------------")
#
#
# class TestFixture:
#     def test_fixture01(self, function):
#         print("\t执行test01测试用例")
#
#     def test_fixture02(self, function):
#         print("\t执行test02测试用例")
#
#     def test_fixture03(self, function):
#         print("\t执行test03测试用例")

# 3.在需要使用固件的case上使用装饰器@pytest.mark.usefixtures('固件名')
# @pytest.fixture()
# def function():
#     print("\r---------------------自动执行之前---------------------")
#     yield
#     print("\r---------------------自动执行之后---------------------")
#
#
# class TestFixture:
#     @pytest.mark.usefixtures('function')
#     def test_fixture01(self):
#         print("\t执行test01测试用例")
#
#     @pytest.mark.usefixtures('function')
#     def test_fixture02(self):
#         print("\t执行test02测试用例")
#
#     @pytest.mark.usefixtures('function')
#     def test_fixture03(self):
#         print("\t执行test03测试用例")
# 4.conftest.py
class TestFixture01:
    def test_fixture01(self):
        print("\t执行test01测试用例")

    def test_fixture02(self):
        print("\t执行test02测试用例")

    def test_fixture03(self):
        print("\t执行test03测试用例")


class TestFixture02:
    def test_fixture01(self):
        print("\t执行test01测试用例")

    def test_fixture02(self):
        print("\t执行test02测试用例")

    def test_fixture03(self):
        print("\t执行test03测试用例")


if __name__ == '__main__':
    pytest.main(["-vs", 'test_pytest01.py'])
