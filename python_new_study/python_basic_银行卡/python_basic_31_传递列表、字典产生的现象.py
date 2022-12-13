"""
#@Time：2022/7/23-21:09
#@file：python_basic_31_传递列表、字典产生的现象
#@Project:python_new_study
#@Content:

"""
d = {"name": "Alex", "age": 26, "hobbie": "⼤保健"}
l = ["Rebeeca", "Katrina", "Rachel"]


def change_data(info, girls):
    info["hobbie"] = "学习"
    girls.append("XiaoYun")


change_data(d, l)  # 结果:{'name': 'Alex', 'age': 26, 'hobbie': '学习'}
# ['Rebeeca', 'Katrina', 'Rachel', 'XiaoYun']
print(d, l)

# 根据上图我们能看出， 程序只是把d这个dict的内存地址传给了change_data函数，把dict⽐作⻥缸，⾥
# ⾯的k,v⽐作缸⾥装的⻥。现在只是把⻥缸丢给了函数，这个⻥缸本身你不能改，但是⾥⾯的⻥可以。
# 相当于只是传了⼀个对这个d的引⽤关系给到函数的形参。这样是为了减少内存的浪费，因为如果这个
# dict⽐较⼤，传⼀次到函数⾥就要copy⼀份新的值的话，效率太低了.
