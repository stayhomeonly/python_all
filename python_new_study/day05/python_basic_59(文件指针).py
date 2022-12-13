# coding:utf-8
"""
#@Time：2022/9/14-21:01
#@file：python_basic_59
#@Project:python_new_study
#@Content:

"""
# 文件指针的位置

# f.seek(5,0) 就是指针放在开始的位置，移动5个字节

# f.seek(5,2) 就是指针放在第二个字节的位置，移动5个字节

# f.seek(-5,0) 就是指针放在末尾的位置，移动5个字节

# 上面三种模式只可以在b模式下用,t模式下用第一个

# with open('新建 文本文档.txt',mode='rb') as f:
#     f.seek(5,0)
#     print(f.tell())  #读取自己读到哪个字节

# 修改文件 第一种方法,文本编辑器的修改方式,对于内存要求过高,对于计算机性能不够友好
# with open('新建 文本文档.txt', mode='rt', encoding='utf-8') as f:
# 第一种写法,写入内存的方法
# res = f.read()
# print(res)
# l = list(res)
# print(l)
# l.insert(1, '不')
# print(l)
# new_res = ''.join(l)
# print(new_res)

# 第二种写法
# res = f.read()
# new_res=res.replace("我喜欢你","我不喜欢你")
# print(new_res)

# with open('新建 文本文档.txt', mode='wt', encoding='utf-8') as f1:
#     f1.write(new_res)
#

# 第二种修改文件的方式
import os

with open('k.txt', mode='rt', encoding='utf-8') as f, \
        open('k.txt.swap', mode='wt', encoding='utf-8') as f1:
    # 这里用w主要是打开之后没有关闭，所以不会覆盖原有的内容
    for line in f:
        res = line.replace("一天", "一年")
        f1.write(res)
    # 代码运行完了之后，会出现差不多的两个文件，需要把原文件删除掉，新文件的 名称改为原文件的名称
os.remove('k.txt')  # 移除旧文件
os.rename('k.txt.swap', 'k.txt')  # 新文件的名称更改掉
