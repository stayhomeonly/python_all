"""
模块导入的方式2 导入某个模块的部分内容（推荐使用） 用什么拿什么
格式 from 包名.模块名 import 函数名1，函数名2，变量
"""
from day10.login_and_regist import user, register

print(user)
print(register('11', '111', '111'))
