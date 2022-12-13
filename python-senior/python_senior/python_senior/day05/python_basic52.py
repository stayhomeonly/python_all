"""
==================================
文件名: python_basic52
作者:    星光梁朝伟
时间:   2022/5/15-11:08
==================================
"""

"""
用for循环 遍历可迭代对象

语法:
for 变量 in 可以迭代对象(str/list/tuple/dict/set):
    循环体
"""

# 遍历  就是把对象中的每个元素都拿出来过一遍
# 遍历字符串  2种方式  值遍历  下标遍历
str1 = '你的笑容很温暖'
for i in str1:
    print(i)

for i in range(len(str1)):  # range(0,7)  [0,1,2,3,4,5,6]
    print(str1[i])

# 遍历列表
list1 = [1, 2, 2, 3, 34, 555, 5]
for i in list1:
    print(i, end=' ')  # 1 2 2 3 34 555 5

for i in range(len(list1)):  # range(0,7)  [0,1,2,3,4,5,6]
    print(list1[i], end=' ')

# 遍历字典 重点********
dict1 = {1: 'xiaohua1', 2: 'xiaohua', 3: 'xiaohua', 4: 'xiaohua'}
for i in dict1:  # 字典默认是操作键
    print(i)  # 1 2 3 4

for i in dict1.keys():  # 与上面的写法效果是一样的  dict_keys[1,2,3,4]
    print(i)

for i in dict1.values():  # 遍历字典的值 dict_values['xiaohua1','xiaohua','xiaohua','xiaohua']
    print(i)

for a in dict1.items():  # 遍历字典所有的键值对  dict_items[(1,'xiaohua1'),(2,'xiaohua'),(3,'xiaohua'),(4,'xiaohua')]
    print(a, type(a))  # (1,'xiaohua1')  tuple

for i, j in dict1.items():  # dict_items[(1,'xiaohua1'),(2,'xiaohua'),(3,'xiaohua'),(4,'xiaohua')]
    print(i, j)  # 1 xiaohua1  2 xiaohua  3 xiaohua  4 xiaohua

# 统计字典dict1的值中 xiaohua出现的次数
count = 0  # 计数器
for i in dict1.values():  # 遍历字典的值 dict_values['xiaohua1','xiaohua','xiaohua','xiaohua']
    if i == 'xiaohua':
        count += 1  # count自增1
print(count)

# 实例2 用for循环统计元组中某个元素出现的次数
tup1 = (1, 2, 3, 5, 4, 85, 85, 41, 6, 5, 6, 87, 1, 2, 3, 15, 3)

count = 0
for i in tup1:
    if i == 2:
        count += 1
print(count)

for i in range(len(tup1)):  # range(0,17)  [0,1,2,3...16]
    if tup1[i] == 2:
        count += 1
print('2在tup1元组出现的次数是{}次!'.format(count))
