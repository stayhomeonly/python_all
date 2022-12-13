"""
#@Time：2022/7/24-11:10
#@file：python_basic_34(内置函数)
#@Project:python_new_study
#@Content:

"""
# abs 取绝对值
print(abs(-10))  # 10

# all 要求所有返回值都为真
a = [0, 1, 2, 3, 4, 5, 6, 7]
print(all(a))  # False ,bool值非空为真，非零为真，None假

# any 要求其中一个返回为真则为真
a = [0, 1, 2, 3]
print(any(a))

name = "fengxin"
age = 18
print(dir())  # 打印所有在当前页面的变量名

# map  map(func, *iterables) --> map object ,iterables可迭代的，代表迭代的内存例如列表

l = list(range(10))
print(l)


def calx(x):
    return x ** 2


m = map(calx, l)  # calx代表函数内存，返回一个内存地址
for i in m:
    print(i)
