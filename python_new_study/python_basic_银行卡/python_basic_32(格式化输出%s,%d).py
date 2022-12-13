"""
#@Time：2022/7/23-21:21
#@file：python_basic_32(格式化输出%s,%d)
#@Project:python_new_study
#@Content:

"""
# 格式化输出 %s 传入的是字符串,不管传入的是什么类型，都默认字符串
'my name is 张大仙,come from 广东'
info = 'my name is %s,come from %s' % ('张大仙', '广东')
print(info)
inf2 = 'my name is %s' % '张大仙'

# 也可以传入字典，写法
info3 = 'my name is %(name)s,come from %(address)s' % ({'name': '张大仙', "address": '广东'})
print(info3)  # 如果传入的值是字典类型的，只需要在%s的中间写入key即可

# %d 表示接收的是一个整型，默认必须是整型


