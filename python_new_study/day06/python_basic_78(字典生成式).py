"""
#@Time：2022/12/14-20:50
#@file：python_basic_78(字典生成式)
#@Project:git_python1
#@Content:

"""
# 集合生成式
# list1 = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大金野_老坛酸菜', '白象']
# res = {name for name in list1}
# print(res,type(res))

# 字典生成式
# list1 = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大金野_老坛酸菜', '白象']
# res = {name:5 for name in list1}
# print(res, type(res))
# list1 = [('康师傅_老坛酸菜', 5), ('统一_老坛酸菜', 6), ('大金野_老坛酸菜', 7), ('白象', 8)]
# res = {k:v for k, v in list1 if not k.startswith('康师傅')}
# print(res, type(res))
#
# for k ,v in list1:
#     print(k,v)
# 康师傅_老坛酸菜 5
# 统一_老坛酸菜 6
# 大金野_老坛酸菜 7
# 白象 8

# 生成器表达式
list1 = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大金野_老坛酸菜', '白象']
res = (name for name in list1)
print(res)
print(next(res))  # 康师傅_老坛酸菜
print(res.send(None))  # 统一_老坛酸菜 send(None)等于next
print(res.send(10))  # 大金野_老坛酸菜
print(res.send('张大仙'))#白象



