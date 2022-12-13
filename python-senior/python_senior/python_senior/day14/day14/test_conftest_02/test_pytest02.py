"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-11:53
知识点: 
---------------------------------
"""
import pytest

"""
测试固件的范围
scope：
        function(default)、class、module、session(package)
"""


@pytest.fixture(scope='class', autouse=True)
def class_scope():
    print("\r---------------------类自动执行之前---------------------")
    yield
    print("\r---------------------类自动执行之后---------------------")


class TestA:
    def test01(self):
        print("执行test01测试用例")

    def test02(self):
        print("执行test02测试用例")

    def test03(self):
        print("执行test03测试用例")


class TestB:
    def test01(self):
        print("执行test01测试用例")

    def test02(self):
        print("执行test02测试用例")


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest02.py'])
