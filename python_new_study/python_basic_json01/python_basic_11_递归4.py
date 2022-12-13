"""
#@Time：2022/6/25-9:05
#@file：python_basic_11_递归1
#@Project:python_new_study
#@Content:

"""

# 1、要求：把下面列表的每一个值单独打印出来
l = [1, 2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12]]]]]]]]]]]
l1 = [1, 2, [3, 4]]


def func(li):
    for i in li:
        if type(i) is list:
            func(i)

        else:
            print(i)


func(l)

# 打印 abcd全排列
c='abcd'
for m in c:
    print(m)

