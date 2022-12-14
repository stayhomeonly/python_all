"""
#@Time：2022/12/13-20:39
#@file：python_basic_77(列表生成式)
#@Project:git_python
#@Content:

"""
# 列表生成式
list1 = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大金野_老坛酸菜', '白象']
new_list = []
# 找出里面已老坛酸菜结尾的
for name in list1:
    if name.endswith('老坛酸菜'):  # engswith就是已XX结尾的，择添加进去
        new_list.append(name)
print(new_list)
# 列表生达式写法
new_l = [name for name in list1 if name.endswith('老坛酸菜')]
print(new_l)
# 列表生成式写法，第一步把正常代码写成一个列表
# [for name in list1:
#     if name.endswith('老坛酸菜'):  # engswith就是已XX结尾的，择添加进去
#         new_list.append(name)]

# 第二步去掉冒号，然后放在一行，去掉最后一行列表的代码
# [for name in list1 if name.endswith('老坛酸菜')]

# 第三步,因为最后生成一个列表，所有需要把生成的列表内容变量放在最前面，然后用一个变量接收
res=[ name for name in list1 if name.endswith('老坛酸菜')]
print(res)

# 列表生成式 [ 结果 for item in 可迭代对象 if 条件]
