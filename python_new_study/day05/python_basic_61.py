# coding:utf-8
"""
#@Time：2022/9/28-13:33
#@file：python_basic_61
#@Project:python_new_study
#@Content:

"""
l1 = [
    {"姓名": "张三", "年龄": 18, "职业": "律师", "爱好": "篮球"},
    {"姓名": "李四", "年龄": 20, "职业": "律师", "爱好": "篮球"},
]

l2 = {"姓名": ['张三', "李四"],
      "年龄": [18, 20],
      "职业": ["律师", "律师"],
      "爱好": ["篮球", "篮球"]}


# l1转换成l2
# def l1_to_l2(l1):
#     l3 = {}
#     for i in l1:
#         for key, value in i.items():
#             if key not in l3:
#                 l3[key] = []
#                 # print(l3)
#             l3[key].append(value)
#     return l3


# print(l1_to_l2(l1))

# 把l2转换成l1
# 字典的长度就是key的长度，len(字典)
def l2_to_l1(l2):
    l4 = []
    l5 = {}
    for i in range(len("姓名")):  # 这里是用value的长度
        print(i)
        for k, v in l2.items():
            l5[k] = v[i]
            # print(l5)
        l4.append(l5)  # 和下面一步的功能一样，下面的代码更加简洁

        # l4.append({k:v[i] for k,v in l2.items()} )
    return l4


print(l2_to_l1(l2))
