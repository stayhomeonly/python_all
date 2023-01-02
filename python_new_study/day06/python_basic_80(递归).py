"""
#@Time：2022/12/17-21:12
#@file：python_basic_80(递归)
#@Project:git_python1
#@Content:

"""
# 函数嵌套
# 1、定义的时候调用(装饰器)
# 2、调用的时候嵌套

# 递归
# 在调用一个函数的过程中，又调用了自己本身这个函数

# import sys
#
# print(sys.getrecursionlimit())  # 递归层数1000层

# sys.setrecursionlimit(1500) # 可以修改递归层数
# 直接调用
# def func():
#     print("张大仙")
#     func()  # 如果这样写，相当于一个死循环，而且是在不停地调用内存
#
#
# func()

# 间接调用
# def func1():
#     print("func1")
#     func2()
#
# def func2():
#     print('func2')
#     func1()
#
# func1()


# 计算1-10 的和





# while i>0:
#     total=total + i
#     i=i-1
#
#
# print(total)

# 用递归的做法
# def my_sum():
#     global i,total
#     total = total + i
#     i=i-1
#     if i==0:
#         return
#     else:
#         my_sum()

# 优化修改

# total=0
def my_sum(i):
    # global total
    # total += i   写了这行代码之后i + my_sum(i-1)，这两行就可以删除掉了
    # i=i-1  # 这行代码直接可以删除，把my_sum(i)改成my_sum(i-1)
    if i == 0:
        return  0 # 为什么return 因为这个时候i=0,如果不写这行代码就会报错，显示整型不能和None相加
    return i + my_sum(i-1)


res=my_sum(10)
print(res)

# 优化的代码之后，代码少了，不过相对来讲可读性弱了点

