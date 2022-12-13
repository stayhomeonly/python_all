"""
--------------------------------
@Time  : 2022/2/24-------19:33
@author  :  ztt
@File  :  python_basic02 
--------------------------------
"""
"""
测试固件(测试夹具)
使用固件的三种方式
1,@pytest.fixture(autouse=True):声明固件时会设置autouse=True会自动使用固件
2,在需要使用固件的case参数传入固件函数名即可
3,使用pytest.mark.usefixture('固件名')装饰器装饰需要使用固件地的case
"""
import pytest

#在类前使用固件，夹具
class TestFixture:
    @pytest.fixture(scope='class', autouse=True)
    def func_scope(self):
        print('--在class前使用--')
        yield  # 暂停的意思
        print('--在class后使用--')

    def test_01(self):
        print('开始执行case01--')

    def test_02(self):
        print('开始执行case02--')


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest_02.py'])
