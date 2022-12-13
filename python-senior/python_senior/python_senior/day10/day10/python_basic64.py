import os

"""
一般用常量对路径进行管理
好处 代使用非绝对路径 可移植性高
"""
path = os.path.dirname(__file__)  # 获取当前文件所在的目录（文件夹）
print(path)

path2 = os.path.dirname(os.path.dirname(__file__))  # 获取当前目录的父级目录
print(path2)

# 地址的拼接
case_dir = os.path.join(path, "config.ini")
print(case_dir)
case_dir = os.path.join(path, "python_basic64.py")
print(case_dir)