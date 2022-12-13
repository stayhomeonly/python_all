"""
#@Time：2022/5/30-18:53
#@file：python_basic-11
#@Project:Pythonselenium
#@Content:

"""
import time

# 获得当前时间时间戳
now = int(time.time())
print(now)

# 删除字典里面的某个值  用del
dict1 = {'age': '18', 'name': 'xiaohua', 'sex': 'nv'}
print(len(dict1))  # 求字典的长度
for i in dict1.items(): # 遍历字典得出来的就是元组(key,value)这种形式
    print(i)  # ('age', '18') ('name', 'xiaohua') ,('sex', 'nv')

del dict1['age']
print(dict1)
# 删除字典里面的某个值  也可以用pop
dict1.pop('name')
print(dict1)
# 清空dict 用clear
dict1.clear()
print(dict1)
