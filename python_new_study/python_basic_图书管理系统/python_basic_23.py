"""
#@Time：2022/7/6-21:39
#@file：python_basic_23
#@Project:python_new_study
#@Content:

"""
dict1={}
f=open("stock_data.txt",'r+',encoding='utf-8')
lines = f.readlines() # 读取所有数据

line1=lines[0] #读取第一行数据
line2=line1.strip().split(',') #把第一行数据转换成列表
print(line2)
for i in line2:
    print(i) #遍历列表，把每个值读取出来
























