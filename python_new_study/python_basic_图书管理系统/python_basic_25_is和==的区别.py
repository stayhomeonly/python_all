"""
#@Time：2022/7/11-17:02
#@file：python_basic_25_is和==的区别
#@Project:python_new_study
#@Content:

"""
# is 和 == 的区别
a = "张大仙"
b = "张大仙"
print(id(a),id(b))# 1946316554032 1946316554032 pycharm里面id显示一样,但是在
# python 里面显示是不一样的
print(a==b)#代表着左右两边的
print(a is b)#代表着两者的id地址是否相同，pycharm是一样的，python里面是不一样的