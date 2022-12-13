"""
==================================
文件名: python_basic73
作者:    Liu
时间:   2022/5/29-14:14
==================================
"""
"""
函数参数的类型 
1.必须参数（位置参数）2.默认参数 3.不定长参数（可变参数） 4.关键字参数
"""


# 1.必须参数 入参按照位置传递 再调用函数时 入参的元素个数必须相同
def add1(a, b):
    c = a + b
    return c


add1(1, 10)
add1(a=1, b=10)
print(add1(1, 10))  # 11
print(add1(a=1, b=10))  # 11


# 2 默认参数  我们可在定义函数的时候 给入参设置默认值 如过只传一个值 b就用默认值  如果传2个值  b就使用传入的值
def add2(a, b=10):
    c = a + b
    return c


print(add2(9))
print(add2(11, 2))


# 3.不定长参数 (可变参数)  可以保存0-N个入参  一般使用*args表示  调用该方法时如果传入多个入参 会自动组包成一个元组
def add3(*args):
    print(args)
    print(type(args))


add3(1, 2, 3, 5, 7)  # (1, 2, 3, 5, 7)  <class 'tuple'>
add3()  # () <class 'tuple'>


# 4. 关键字参数 一般用来接收key—value入参 而且会保存成一个字典 一般用**kwargs
def add4(**kwargs):
    print(kwargs)
    print(type(kwargs))


add4(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}  <class 'dict'>


# 多种参数混合使用的实例1
def add5(x, y=2, z=6, *args, **kwargs):
    print(x, end=' ')
    print(y, end=' ')
    print(z, end=' ')
    print(args, end=' ')
    print(kwargs, end=' ')
    print()


add5(1)  # 1 2 6 () {}
add5(1, 5)  # 1 5 6 () {}
add5([1, 2])  # [1, 2] 2 6 () {}
add5(5, 6, 7, 8, 9)  # 5 6 7 (8, 9) {}
add5(7, 8, 9, 10, a=5, b=8)  # 7 8 9 (10,) {'a': 5, 'b': 8}
add5(999, z=100)  # 999 2 100 () {}


# 多种参数混合使用实例2
def add6(*args, **kwargs):
    print(args, end=' ')
    print(kwargs)


add6()  # () {}
add6(1, 5, 8, 9, 10, 9, 12, 55, 4)  # (1, 5, 8, 9, 10, 9, 12, 55, 4) {}
add6(a=1, b=2)  # () {'a': 1, 'b': 2}
add6(1, '325a', [1, 9], (45, 56), {'a': 56}, a=5)  # (1, '325a', [1, 9], (45, 56), {'a': 56}) {'a': 5}
