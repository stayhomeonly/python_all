"""
#@Time：2022/8/14-21:25
#@file：python_basic_52(set的交集、并集、差集)
#@Project:python_new_study
#@Content:

"""
hobbies1={'吃饭','睡觉','看书','钢琴','跳舞','游泳','旅行'}
hobbies2={'吃饭','睡觉','追剧','打游戏'}
# 取交集
print(hobbies1 & hobbies2)

# 取并集
print(hobbies1 | hobbies2)

# 取差集
print(hobbies1 - hobbies2)
print(hobbies2 - hobbies1)

# 对称差集,就是两个的各自有的东西
print(hobbies1 ^ hobbies2)
print((hobbies1 - hobbies2) | (hobbies2 - hobbies1))

# 父子集
a={1,2,3}
b={1,2}
print(a>b)  #True