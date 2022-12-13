"""
#@Time：2022/6/25-9:05
#@file：python_basic_11_递归1
#@Project:python_new_study
#@Content:

"""
# 计算1到10 的和
# 正常写法
i = 10


total=0
# while i>0:
#     total += i
#
#     i=i-1
# print(total)

# 递归写法
# 第一步：
# def my_sum():
#     global i,total
#     total += i
#
#     i = i - 1
#     if i==0:
#         return
#
#     my_sum()
#
#
#     i=i-1
# print(total)
# 第二步优化：
# def my_sum(i):
#     global  total
#     total += i
#
#     i=i-1
#     if i == 0:
#         return
#
#     my_sum(i)

# 第三步优化：
def my_sum(i):
    global  total
    total += i


    if i == 0:
        return

    return my_sum(i-1)

my_sum(i)
print(total)

