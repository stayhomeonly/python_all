"""
作者：Liucl
创建时间：2022/5/3 10:37

"""
"""
skip:
@pytest.mark.skip(reason="bug未修复") 跳过标记的测试用例，()中填写跳过的原因，当然可以省略
什么时候跳过? 如果该测试用例不需要执行，可以跳过。还有该测试用例有bug,并且未修复，我们也可以选择跳过。

pytest额外插件1: pytest-ordering: 可以对需要运行的测试用例的顺序进行排序
1、安装相关库：pip install pytest-ordering  安装后 order排序才能起作用
2、在需要排序的测试用例上边添加装饰器：@pytest.mark.run(order=2)
3、order =1 =2 =3 代表运行顺序，1先执行 2再执行... 注意 order也可以为负值，比如 -1 代表 倒数第一执行。
"""

import pytest

age = 21


class TestLogin:
    # 登录成功
    @pytest.mark.skip(reason="开发接口更新，暂未维护")
    @pytest.mark.run(order=-1)
    def test_login01(self):
        assert 1 == 1

    # 用户名错误
    @pytest.mark.skipif(age > 18, reason="根据年龄跳过")
    @pytest.mark.run(order=-1)
    def test_login02(self):
        assert "H" in "Hello World"

    def test_login03(self):
        assert 3 == 3


if __name__ == "__main__":
    # 知识点1:运行当前模块的下的内容
    pytest.main(['-vs', './test_pytest03.py'])  # 运行标记test03
