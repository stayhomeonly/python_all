"""
==================================
文件名: python03
作者:    Liu
时间:   2022/6/26-15:32
==================================
"""

"""
1.多继承: 一个子类可以继承多个父类
2.多继承的情况下,子类会先在自己类中去找需要的内容,找不到再去父类中找

"""


class Father(object):
    def test(self):
        print('这是基类01!')


class Mother:
    def test(self):
        print('这是基类02!')


class Baby(Mother, Father):
    pass


by = Baby()
by.test()  # 这是基类02!
print(Baby.__mro__)  # 查看方法解析顺序


# 菱形继承
class A:
    def test(self):
        print('from A')


class B(A):
    # def test(self):
    #     print('from B')
    pass


class C(A):
    # def test(self):
    #     print('from C')
    pass


class D(B, C):
    # def test(self):
    #     print('from D')
    pass


dd = D()
dd.test()  # D、B、C、A、O
print(D.__mro__)  # 查看方法解析顺序

print('===' * 50)


# 钻石继承
class A:
    def test(self):
        print('from A')


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


print(F.__mro__)  # F、D、B、E、C、A、O
