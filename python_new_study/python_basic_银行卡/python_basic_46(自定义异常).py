"""
#@Time：2022/8/10-20:20
#@file：python_basic_46(自定义异常)
#@Project:python_new_study
#@Content:

"""
exp = Exception('性别只能是男或者女')

sex = input("请输入你的性别(男,女):")

if sex == "男" or sex == "女":
    print("你输入的性别:", sex)
else:
    print("你输入的性别有误")
    raise exp
