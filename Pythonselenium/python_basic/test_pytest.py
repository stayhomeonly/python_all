"""
#@Time：2022/5/29-20:07
#@file：python_basic_11
#@Project:Pythonselenium
#@Content:

"""
import pytest


# pytest中执行顺序,可用pytest.mark.run(order=1),order是几就是第几个执行
class Testcase():
    @pytest.mark.run(order=1)
    def test_01(self):
        print('这是第一条案例')

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_02(self):
        print('这是第二条案例')

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.skip(reason='无条件跳过')
    def test_03(self):
        print('这是第三条案例')


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-k','smoke','test_pytest.py'])

    # 上面就是指定smoke运行，一定加上-m,@pytest.mark加上名字，名字随意取 在pytest.ini文件配置下
    # 跳过@pytest.mark.skip(resson=)
    # 跳过@pytest.mark.skipif(resson=) 条件成立就跳过