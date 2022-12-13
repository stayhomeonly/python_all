"""
#@Time：2022/6/25-9:05
#@file：python_basic_11_递归1
#@Project:python_new_study
#@Content:

"""
# 递归
# 在调用一个函数的过程中，又调用自己本身这个函数
import sys
print(sys.getrecursionlimit() )  #递归深度，也就是递归的层级次数
#sys.setrecursionlimit(1500)  #可以修改递归的层级次数
#直接调用
# def func():
#     print("张大仙")
#     func()
# # func()

#间接调用

# def func1():
#     print('func1')
#
#     func2()
# def func2():
#     print('func2')
#     func1()
#
# func1()


