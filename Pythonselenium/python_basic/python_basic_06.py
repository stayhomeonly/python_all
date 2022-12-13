"""
#@Time：2022/5/22-10:51
#@file：python_basic_06
#@Project:python_basic05.py
#@Content:

"""
class CaseData:
    def __init__(self, dict_case):
        for i in dict_case.items():  # 获取字典中的每一对键值对，并且进行遍历
            setattr(self, i[0], i[1])
all_cases = []
dict_case={"name":"fengxin","age":"18"}
cd=CaseData(dict_case=dict_case)
all_cases.append(cd)

print(all_cases)
for i in all_cases:
    print(i) # 是一个迭代器，类型是字典
    print(i.name)
# 求1-100的所有奇数的和
count1 = 0
# for i in range(1,101):
#     if i %2==1:
#         count1 =count1 + i
# print(count1)

# 第二种方法
# for i in range(1, 101, 2): #利用步长来计算
#     if i % 2 == 1:
#         count1 = count1 + i
# print(count1)