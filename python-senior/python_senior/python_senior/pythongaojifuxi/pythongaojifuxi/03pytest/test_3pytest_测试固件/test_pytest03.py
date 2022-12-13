"""
================================
  Author   :  Lee
  FileName :  test_pytest01
  Date     :  2022/8/8 - 11:46
================================
"""
import pytest

"""
测试固件(测试夹具)的作用，能够在测试方法、测试类、测试模块、测试包、测试会话 前或者后 做一些事情。
测试固件的声明: @pytest.fixture(scope='作用域') 如果声明固件时设置autouse=True会自动使用固件
测试固件的使用: 
        1、手动添加：固件不使用autouse=True，并且在需要的地方添加: @pytest.mark.usefixtures("固件名1")
        2、自动添加：固件使用autouse=True，会根据固件作用域自动添加。
"""


@pytest.fixture(scope='module', autouse=True)  # 如果声明了autouse=True参数就会在当前模块执行前后自动使用
def module_scope():
    print('-----------module前执行-----------')
    yield
    print('-----------module后执行-----------')

#
# @pytest.fixture(scope='package', autouse=True)  # 如果声明了autouse=True参数就会在当前包执行前后自动使用
# def package_scope():
#     print('++++++package前执行++++++')
#     yield
#     print('++++++package后执行++++++')


# @pytest.fixture(scope='session', autouse=True)  # 如果声明了autouse=True参数就会在整个会话执行前后自动使用
# def session_scope():
#     print('***session前执行***')
#     yield
#     print('***session后执行***')


class TestFixture1:

    def test_case01(self):
        print('开始执行case1!')

    def test_case02(self):
        print('开始执行case2!')


class TestFixture2:

    def test_case03(self):
        print('开始执行case1!')

    def test_case04(self):
        print('开始执行case2!')


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest03.py'])
