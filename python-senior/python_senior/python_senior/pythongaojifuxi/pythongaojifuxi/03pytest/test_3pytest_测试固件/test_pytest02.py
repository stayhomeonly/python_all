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


@pytest.fixture(scope='class', autouse=True)  # 如果声明了autouse=True参数就会在当前模块每个类执行前后自动使用
def class_scope():
    print('-----------class前执行-----------')
    yield
    print('-----------class后执行-----------')


# @pytest.mark.usefixtures("class_scope")
class TestFixture:
    def test_case01(self):
        print('开始执行case1!')

    def test_case02(self):
        print('开始执行case2!')

    def test_case03(self):
        print('开始执行case3!')


def test_case04():
    print('开始执行case4!')


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest02.py'])
