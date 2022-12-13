# coding:utf-8
"""
#@Time：2022/9/17-21:45
#@file：python_basic_60(函数)
#@Project:python_new_study
#@Content:

"""
import requests

"""
def 函数名(参数1,参数2,参数3):
    '''
    文档描述
    '''
    函数体
    return 值
    return 后面的代码不会执行
"""

# return 之后的代码不会运行,break只是结束当层循环
# def fun1():
#     return 2  # 如果return什么不写，返回就是None
#     print('a')
#
#
# print(fun1())

# 关键字参数(关键字实参),可以不按照位置来传参，按照key=value的形式
# def fun2(x, y, z):
#     print(x, y, z)


# fun2(y=2, x=1, z=3)# 位置实参和关键字实参混用的时候，位置实参必须放在关键字实参前面
# fun2(2, 1, y=3) #报错


# 如何写一个函数，需求列表正常我们只能一次添加一个元素，现在需要添加两个
# 正常思路
# x = 1
# y = 2
# l = []
# l.append(x)
# l.append(y)
# print(l)  # [1, 2]

# 写成函数
# def my_append():
#     x=1
#     y=2
#     l=[]
#     l.append(x)
#     l.append(y)
#     print(l)  # [1, 2]
#
'''
但是上面的写法写死了，我们不能写死
'''

# def my_append(x, y, l=[]):
#     l.append(x)
#     l.append(y)
#     print(l)
#
#
# my_append(1, 2)  # [1, 2]

'''
上面的写法，默认形参尽量不能写成可变类型，不然会让人不专业，但是有这个需求需要怎么写,下面就是写法
'''

# def my_append(x, y, l=None):
#     if l is None:
#         l = []
#
#     l.append(x)
#     l.append(y)
#     print(l)
#
#
# my_append(1, 2)  # [1, 2]


'''
默认参数是在定义阶段被赋值的,定义的时候是把内存地址给了y
'''
a = 3


def fun21(x, y=a):
    print(x, y)


a = 4
fun21(3)  # 3,3

'''
可变长度的参数；在调用函数的时候，传入的实参的个数不固定的
'''
'''
可变长度的位置参数：
用法：*形参名(*args)
'''

# def fun(x, y, *z): #z=(3,4,5)
#     print(x, y, z)
#
#
# fun(1, 2, 3, 4, 5)

# 求和功能
# def function(*args):  # x是元组
#     res = 0
#     for i in args:
#
#         res += i
#     return res
#
#
# print(function(1, 2, 3, 4, 5))

'''
可变长度的关键字参数
用法：**kwargs
'''

# def func(x, y, **kwargs):
#     print(x, y, kwargs)
#
#
# func(1, y=2, a=1, b=2, c=3, name="张大仙")  # 1 2 {'a': 1, 'b': 2, 'c': 3, 'name': '张大仙'}

'''
命名关键字实参(命名关键字参数表)
'''


def funx(x, y, z):
    print(x, y, z)


# funx([1,2,3]) # 如果直接运行报错，显示少了两个参数
funx(*[1, 2, 3])  # 1 2 3

l = [1, 2, 3]
funx(*l)  # 如果不加上*就会报错


#
# def funy(x, y, *args):
#     print(x, y, args)
#
#
# funy(*'愿疫情早点结束')  # 愿 疫 ('情', '早', '点', '结', '束')


def funz(x, y, z):
    print(x, y, z)


funz(**{'x': 1, 'y': 2, 'z': 3})  # funz(x=1,y=2,z=3)
'''
**kwagrs如果和*args一起用，那**kwargs必须在后面
'''


def fun12(*args, **kwargs):
    print(args)
    print(kwargs)


fun12()  # () {}

fun12(1, 2, 3, 4, a=1, b=2, c=3)  # (1, 2, 3, 4),{'a': 1, 'b': 2, 'c': 3}

