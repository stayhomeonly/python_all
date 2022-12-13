"""
#@Time：2022/5/22-20:31
#@file：python_basic_08
#@Project:python_basic05.py
#@Content:

"""

# 允许用户最多选3次
# 每次放出20个车牌共用户选择
# 京[A-Z]-[XXXXX]，可以是数字和字母的选择
# import random
# import string
# count = 1
# s = string.ascii_uppercase + string.digits  # 代表大写和数字所有的组合
# print(s)
# c = random.sample(s, 5)
# print(c)
# #
#
#
# while count < 4:
#     list1 = []  # 存储共用户选择的号
#     for i in range(20):
#         n1 = random.choice(string.ascii_uppercase)  # 生成车牌的第一个字母
#         n2 = ''.join(random.sample(string.ascii_uppercase + string.digits, 5))  # 随机生成5个数字和字母的列表
#         c = f'京{n1}-{n2}'
#         list1.append(c)  # 把生成的号码添加到列表
#         print(i + 1, c)
#     choice = input("输入你喜欢的号码：").strip()  # 可以把你输入的前面和后面的空格都去掉
#     if choice in list1:  # 代表选择的是合法的
#         print('恭喜你选择了新车牌号:{}'.format(choice))
#         exit('Good lucky')
#     else:
#         print('不合法的选择')
#     count = count + 1

# 张三科技有限公司有300名员工，开会抽年终奖，奖项如下
# 一等奖1名，泰国5日游
# 二等奖2名，iphone
# 三等奖3名，游戏机一部
# 规则，抽3次，第一个抽三等奖，第二次抽二等奖，第三次抽三等奖，每个员工限制中奖一次
import random

list2 = ['冯鑫', '叶芬', '冯锦萱', '夏', '叶', '王']
leval = [3, 2, 1]  # 代表每个奖的个数

for i in range(3):
    list3=random.sample(list2,leval[i])
    for w in list3:
        list2.remove(w)
    print(f'获得{3-i}等奖的是:{list3}')


