"""
#@Time：2022/8/12-21:42
#@file：python_basic_50
#@Project:python_new_study
#@Content:

"""
# 造字典的方法
a=('name','age','height')
# 需求,把元祖里面的元素作为key，None做为值
# 第一种方法
b={}
for i in a:
    b[i]=None
print(b) #{'name': None, 'age': None, 'height': None}

# 第二种方法
print({}.fromkeys(a, None)) #{'name': None, 'age': None, 'height': None}

# 字典的取值
dict1={'a':1,"b":2,"c":3}
# 正常取值方法
print(dict1['a'])
# 如果key不存在
# print(dict1['d']) #KeyError: 'd'

# 第二种方法
print(dict1.get('a'))
# 如果key不存在，用get取值会返回None,可以用来某些需求
print(dict1.get('d')) # None
# 删除值
# del dict1['a']
# popitem
print(dict1.popitem()) #删除字典的最后一个值，并且以元祖的形式返回，但是字典是无序的，是按照添加的顺序老判断的
print(dict1) #
# 字典的update功能,用新字典来更新老字典
hero={"人物":"李白","职业":"刺客","技能1":"青莲战歌"}

new={"技能2":"将敬酒","技能1":"神来之笔"}
hero.update(new)
print(hero)

# setdefault #如果字典里面有这个key，返回对用的值，如果没有字典就新增相对应的key，
info={"name":"张大仙","age":18}
print(info.setdefault('name'))
print(info.setdefault('height',95)) #95写了即返回95，如果不写返回None
print(info)


