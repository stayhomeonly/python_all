"""
==================================
文件名: python_basic51
作者:    星光梁朝伟
时间:   2022/5/15-10:22
==================================
"""
""""
for  循环 1.遍历可迭代数据 2.常和 range函数一起使用  除了number之外 其他的都是可以用for循环进行遍历

语法: 
for i in range():
    pass

range()函数会生成一个整数队列,但是包前不包后
"""
# for i in range(5): # range(5)相当于range(0,5)会生成 [0,1,2,3,4] 并且把这个列表的每一个成员赋值给i,每赋值一次循环体就执行一次
#     print(i)  # 0,1,2,3,4
# for i in range(0, 5):
#     print(i)
# for i in range(1, 5):# 和切片类似 前包含后不包含 [1,2,3,4]
#     print(i)  # 1,2,3,4
# for i in range(1, 10, 2):  # 第三个参数是步长,代表每隔几个取一个  range()函数生成的整数队列[1,3,5,7,9]
#     print(i)  # 1,3,5,7,9

# 用for循环求1到100中所有奇数的和
sum1 = 0
for i in range(1, 101):  # 循环遍历1-100之间的整数
    if i % 2 == 1:  # 一个整数取余2只有2个结果,要么是1,1是True,也就是奇数,反之是0,是False,也就是偶数
        # sum1 += i
        sum1 = sum1 + i
print(sum1)

sum1 = 0
for i in range(1, 101, 2):  # range()函数刚好生成的是1-100之间的奇数的整数队列
    sum1 += i

print(sum1)

print(sum(range(1, 101, 2)))

# 用for循环求出1到1000 所有偶数的和
sum2 = 0
# for i in range(1, 1001):
#     if i % 2 == 0:
#         sum2 += i
# print(sum2)
for i in range(0, 1001, 2):
    sum2 += i
print(sum2)

print(sum(range(0, 1001, 2)))
