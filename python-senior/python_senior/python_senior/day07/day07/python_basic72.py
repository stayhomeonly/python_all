"""
==================================
文件名: python_basic72
作者:    Liu
时间:   2022/5/29-11:02
==================================
"""
"""
函数  就是可以重复使用的一段代码  print() type() input() id()
方法  定义在类里面的叫方法  定义在类外面的叫函数
自定义函数
def 函数名([参数1，参数2......]):
    函数体(实现具体的功能)
    [return] 改函数返回的值

"""


def add():
    print('我是一个自定义的函数add')


add()  # 根据函数名来调用


def add1(a, b):
    c = a + b
    return c



# print(add1(1, 5))
d = add1(2, 8)
print(d)
print(add1(3, 11))


# 让你设计一个函数 接收长方形的 长和宽  返回它的面积
def area(length, wid):
    # a = length * wid
    # return a
    return length * wid


a1 = area(100, 33)
print(a1)


def add2(a, b):
    c = a + b
    c2 = a - b
    c3 = a * b
    return c, c2, c3


print(add2(1, 6))  # (7, -5, 6)
a2 = add2(1, 6)
print(type(a2))  # <class 'tuple'>


# 定义一个函数 接收一个整数的入参  判断它是奇数还是偶数 并返回 该数据是奇数/偶数
def p(v):
    if v % 2 == 0:
        return '该数据是偶数'
    elif v % 2 == 1:
        return '该数据是奇数'


print(p(5))
