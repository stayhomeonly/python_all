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


@pytest.fixture(scope='function', params=['xiaohua', 'xiaoli', 'xiaohei'],
                ids=[1, 2, 3])  # 如果声明了autouse=True参数就会在当前模块每个case执行前后自动使用
def func_scope(request):
    print('-----------function前执行-----------')
    yield request.param
    print('-----------function后执行-----------')


class TestFixture:
    @pytest.mark.usefixtures("func_scope")
    def test_case01(self):  # 使用func_scope固件,会在case前执行固件和case后执行固件
        print('开始执行case1!')
        print(func_scope)

    def test_case02(self, func_scope):
        print('开始执行case2!')
        print(func_scope)


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest01.py'])
