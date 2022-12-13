"""
函数传递值的方式 1.值传递 2.引用传递

值传递  传递的是变量的值而非变量本身  被传递的值发生变化 变量不会被改变
引用传递 传递的是变量本省  被传递的变量的值会发生改变

注意点
1.可变类型 （list dict set ） 用的是引用传递
2.不可变类型 （number str tuple） 用的是值传递

"""


def fun1(a):
    a += 1
    print(a)


b = 10
fun1(b)
print(b)  # 10


def fun2(lis):
    lis.append(5)
    print(lis)


a = [1, 2, 2]
fun2(a)
print(a)