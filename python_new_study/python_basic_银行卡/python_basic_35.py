"""
#@Time：2022/7/24-22:07
#@file：python_basic_35
#@Project:python_new_study
#@Content:

"""
# 格式化填充
# *****开始******
a='{0:*^10}'.format('开始') #0代表索引位置，如果是key-value也可以写key
print(a)

b='{num:.2f}'.format(num=3.121518) #保留2位小数
print(b)