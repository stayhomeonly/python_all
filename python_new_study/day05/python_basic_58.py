# coding:utf-8
"""
#@Time：2022/9/13-16:53
#@file：python_basic_58
#@Project:python_new_study
#@Content:

"""
dict1={"name":None,"age":18,"sex":None}

# 需求删除值为None的键
dict2 = []
for key in dict1:
    result={key:value for key,value in dict1.items() if dict1[key] is not None}
    if dict1[key] is not  None:
        dict2.append(result)
        print(dict2)












