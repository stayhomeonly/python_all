"""
#@Time：2022/5/22-19:56
#@file：python_basic_07
#@Project:python_basic05.py
#@Content:

"""
# random
import random
import string

# random.choice随机抽取字符串中任意一个
a = random.choice('abcdefghijklmnopqrstuvwsyz')
print(a)

# random.choice也可以随机抽取列表中任意一个
list1 = ['冯鑫', '叶芬', '冯锦萱']
b = random.choice(list1)
print(b)

# random.sample(a,3) # 从数据源中随机抽取三个
d = 'abcdefghijklmnopqrstuvwsyz'
c = random.sample(d, 3)
print(c)
# 打印所有大小写字母
print(string.ascii_letters)
# 打印所有大写字母
print(string.ascii_uppercase)
# 打印所有小写字母
print(string.ascii_letters)
# 打印所有的特殊字符
print(string.punctuation)
# 打印所有的数字，返回的是字符串
print(string.digits)
