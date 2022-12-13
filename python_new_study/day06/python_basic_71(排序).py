"""
#@Time：2022/12/2-17:20
#@file：python_basic_71(排序)
#@Project:git_python
#@Content:

"""
list1 = [23, 45, 78, 99, 11, 0, -1]
# 除了用sort之外用代码排序从小到大
for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)