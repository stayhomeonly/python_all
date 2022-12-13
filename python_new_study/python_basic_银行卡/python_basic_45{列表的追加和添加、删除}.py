"""
#@Time：2022/8/9-21:24
#@file：python_basic_45{列表的追加和添加}
#@Project:python_new_study
#@Content:

"""
l = ['天下第一', '张大仙', '年龄']
# 添加
l.append(5)
print(l)  # ['天下第一', '张大仙', '年龄', 5]
# 追加
l.insert(2, '大仙')  # 2代表索引，后面跟着内容
print(l)  # ['天下第一', '张大仙', '大仙', '年龄', 5]

# extend
l2 = ['天下第一', '张大仙', '年龄']
l1 = ['昨天', '今天', '明天']
l2.extend(l1)
print(l2)  # 直接添加列表

# 删除
# del
# names=["美杜莎",'云韵','古熏儿']
# del names[0]
# print(names)

# pop
# names=["美杜莎",'云韵','古熏儿']
# names.pop()
# # names.pop(2)
# print(names)

# remove
names = ["美杜莎", '云韵', '古熏儿', "美杜莎"]
# names.remove('美杜莎')  #只会删除第一次出现的元素
print(names)
print('-' * 50)

for i in range(len(names)):
    if names[i] == "美杜莎":
        names.pop(i)
    else:
        pass
    i = i + 1
    print(i)
    if i < len(names):
        pass
    else:
        break

print(names)
# 找出下列列表相同的元素和不同的元素
a = [1, 2, 3]
b = [3, 4, 5]

# 相同的元素
c = [x for x in a if x in b]
print(c)
print(list(set(a) & set(b)))  # 另外一种写法

# 不同的元素
d = [y for y in (a + b) if y not in c]
print(d)
print(list(set(a) ^ set(b)))  # 另外一种写法
