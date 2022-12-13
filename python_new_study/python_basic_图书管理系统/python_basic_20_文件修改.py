"""
#@Time：2022/6/29-21:46
#@file：python_basic_20
#@Project:python_new_study
#@Content:

"""
f=open('stock_data.txt','r+',encoding='utf-8')

# 加载到内存
data = f.read()
new_data=data.replace('吉贝尔','路飞学城')
#清空文件
f.seek(0) #移动光标到0号位置
f.truncate()#截断文件

# 3.把新内容写回硬盘
f.write(new_data)
f.close()
