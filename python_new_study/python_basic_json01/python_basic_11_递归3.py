"""
#@Time：2022/6/25-9:05
#@file：python_basic_11_递归1
#@Project:python_new_study
#@Content:

"""

i = 10


def my_sum(i):
    if i == 0:
        return i

    return i + my_sum(i - 1)

res=my_sum(i)
print(res)
