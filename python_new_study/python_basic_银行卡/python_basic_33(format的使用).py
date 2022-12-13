"""
#@Time：2022/7/23-21:29
#@file：python_basic_33(format的使用)
#@Project:python_new_study
#@Content:

"""
# format 默认传入的字符串
info = 'my name is {},come from {}'.format('张大仙', '广东')
print(info)

info1 = 'my name is {0},come from {1}'.format('张大仙', '广东')
print(info1)  # my name is 张大仙,come from 广东 里面的0和1代表索引

# 如果想重复
info2 = 'my name is {0}{0}{0},come from {1}{1}{1}'.format('张大仙', '广东')
print(info2)

# format也可以按照key-value的方式传值
info2 = 'my name is {name},come from {age}'.format(name='张大仙',age=18)
# 大括号里面写的key
print(info2) #my name is 张大仙,come from 18

