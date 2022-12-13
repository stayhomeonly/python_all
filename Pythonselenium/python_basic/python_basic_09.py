# 如果列表太长，不知道索引,想把其中一个值改掉方法
list1 = ['天下', '无双', '第一', '第二', '第三', '第四', '5']

# 先把这个值的索引找出来
index_item = list1.index('5')
print(index_item)
# 在利用索引更改
list1[index_item] = '6'
print(list1)

# 打印索引,以及索引值
list2 = [1, 2, 'd', 4, 6, 8, 9, 1]
for i in enumerate(list2):#enumerate枚举的意思
    print(i)
