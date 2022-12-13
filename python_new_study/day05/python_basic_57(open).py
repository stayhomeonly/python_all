# coding:utf-8
"""
#@Time：2022/8/25-21:04
#@file：python_basic_57(open)
#@Project:python_new_study
#@Content:

"""
# open()控制文件读写操作的模式

'''
    r:只读模式
    w:只写模式
    a:只追加写模式
    +：r+,w+,a+

'''

# 控制文件读写内容的模式
"""
    t模式:
        读写都是以字符串（unicode）为单位的
        指定参数encoding='utf-8'
        只针对文件内容
    b模式：
        bytes模式/二进制模式
        
    

"""

# 打开文件
# open(r'D:\FENG1234\python_new_study\data\文件') # 绝对路径
# f=open(r'data/文件.txt', mode='rt',encoding='utf-8') # 在t模式下的最好指定encoding='utf-8'
# print(f)
# # 操作文件(读写)
# res=f.read()
# print(res)
#
#
# # 关闭文件
# f.close()


# with 语法(上下文管理器)
# with open(r'data/文件.txt',mode='rt',encoding='utf-8') as f,\
#         open(r'data/b.txt',mode='rt',encoding='utf-8') as f2:
#     res=f.read()
#     print(res)
#
#     res2=f2.read()
#     print(res2)

# t\b
# rt
# with open('data/文件.txt',mode='rt',encoding='utf-8') as f: # r模式下文件指针会跳到文件开始位置,会一次性读取、
#     # 所有内容，如果文件小还行，如果文件太大，就非常不好
#     print("第1次读".center(80,'-'))
#     res1=f.read()
#     print(res1)
#
#     print("第2次读".center(80, '-'))
#     res2 = f.read()
#     print(res2)
# with open('data/b.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         # print(line, end=' ')  # print自带了一个换行符，data/b.txt的数据也自带了一个换行符\n
#         l=line.strip().split('---')  # strip默认去除首尾两端默认的字符,split按照什么拆分，返回列表
#         print(l)

# wt
# with open('data/c.txt', mode='w', encoding='utf-8') as f: # w模式下如果文件不存在会自动创建，文件存在打开
#     # 的时候会清空内容
#     f.write('晓看天色暮看云\n')
#     f.write('兴业湘军看叶湘军\n')# 不会清空上面的内容



# at, a模式下如果文件不存在会自动创建
# with open('data/d.txt', mode='a', encoding='utf-8') as f:
#     f.write("向前一小步，文明一大步\n")
#     f.write("向前一小步，文明一大步\n")
#     f.write("向前一小步，文明一大步\n")


# +模式
# r
with open('data/d.txt', mode='r+', encoding='utf-8') as f:
    # res=f.read()
    # print(res)
    f.write("1234")
# r+,read()会直接读取到文件的最后，如果在写，就写在文件的后面
# 如果去掉read(),就会写在文件的最前面


# x 模式，如果文件不存在，就会创建，文件存在，就会报错，不可读

# b模式，可以打开任何文件方式，但是不要指encoding
