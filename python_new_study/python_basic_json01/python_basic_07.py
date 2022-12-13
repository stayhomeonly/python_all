"""
#@Time：2022/6/21-21:38
#@file：python_basic07
#@Project:python_new_study
#@Content:

"""
# r是只能读取文件，不能写
f=open('name_list',"r")
# print(f.read())#读出所有的内容
print('------------------')
print(f.readline())#读第一行，如果先读取了所有内容的东西，在读取第一行，就不能读了
print(f.read())# 看读取文件的内容的的图片