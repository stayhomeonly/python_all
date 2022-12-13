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


# 函数的重中之重
def fun1(x, y, z):
    print(x, y, z)


def fun2(*args, **kwargs):  # 这样写的好处就是，不管fun1以后怎么变动，都不会用改动fun2
    fun1(*args, **kwargs)  # *args是打散位置形参，args=(1,2),kwargs={"z":1}


fun1(1, 2, z=1)  # 1 2 1

import this
