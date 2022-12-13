"""
#@Time：2022/8/7-20:28
#@file：python_basic_44
#@Project:python_new_study
#@Content:

"""
# 索引取值
info = 'good good study,day day up!'
# print(info[-1])

# 切片
print(info[0:4])
print(info)

# strip去除空格
name = ' 张大仙  '
res = name.strip()
print(res)  # strip去除空格，默认只能去除左右两边的空格，张大仙

name1 = '!!! 张大仙!!!!'
res1 = name1.strip('!')  # 去除左右两边的！，如果左右两边有多种符号，全部写进去
print(res1)

# split拆分
# names = '李白 韩信 露娜 孙悟空'
# res2 = names.split()  # 默认按照空格分割，返回列表
# print(res2)

# names1 = '李白-韩信-露娜-孙悟空'
# res3 = names1.split('-')
# print(res3, type(res3))  # ['李白', '韩信', '露娜', '孙悟空'] <class 'list'>

names1 = '李白-韩信-露娜-孙悟空'
res3 = names1.split('-', 1)  # 按照'-'分割,后面1代表分割次数
print(res3, type(res3))  # ['李白', '韩信-露娜-孙悟空'] <class 'list'>

# join
l = ['李白', '杜甫', '韩信']
print('-'.join(l))  # 讲列表转换成字符串，前提里面都是字符串

# replace
names = '李白-杜甫-韩信-白居易'
print(names.replace('-', ':'))  #2代表次数，如果不写代表所有

# isdigit
print('84'.isdigit()) # 判断字符串是否是纯数字
