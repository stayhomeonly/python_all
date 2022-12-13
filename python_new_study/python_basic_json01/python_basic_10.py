"""
#@Time：2022/6/24-12:03
#@file：python_basic_10
#@Project:python_new_study
#@Content:

"""
list1=["语文","86分","数学","150","英语","120","理综","200"]
#把上面列表转换为字典格式
dict1={}
for key,value in zip(list1[::2],list1[1::2]):
    dict1[key]=value
print(dict1)