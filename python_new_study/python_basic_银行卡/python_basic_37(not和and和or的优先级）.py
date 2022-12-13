"""
#@Time：2022/7/26-21:50
#@file：python_basic_37(and和or和and的优先级）
#@Project:python_new_study
#@Content:

"""
# 优先级 not>and>or
84 != 73 and not 22 > 23 or 31 == 27
print(84 != 73 and not 22 > 23 or 31 == 27)  # True ,先判断not,在判断and，在判断or

# 成员运算符 in 运用于容器类型，字符串
# in,对于字典的话，是判断key不是判断value
