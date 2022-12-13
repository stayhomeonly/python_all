"""
#@Time：2022/6/25-15:36
#@file：python_basic_14_2进制操作文件
#@Project:python_new_study
#@Content:

"""
'''
如何处理图⽚、视频⽂件呢？
可以⽤2进制模式打开⽂件
rb 2进制只读模式
wb 2进制创建模式，若⽂件已存在，则覆盖旧⽂件
ab 2进制追加模式，新数据会写到⽂件末尾
这样，你读出来的数据，就是bytes字节类型了，当然写进去的也必须是bytes格式了
'''
#
# f=open("读取文件的内容的图片.png","rb")
# for line in f:
#     print(line)

#encoding=None,就是告诉解释器，当前要打开的文件是什么格式
#如果是None，则用解释器默认编码。utf-8


# wb二进制写
f=open("wb_file",'wb')
s='冯鑫1'
# f.write(s.encode('gbk'))
print(s.encode('utf-8')) #字节类型
f.write(s.encode('utf-8'))