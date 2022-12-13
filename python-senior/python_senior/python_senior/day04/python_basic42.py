"""
==================================
文件名: python_basic42
作者:    xiaoliu
时间:   2022/5/8-11:33
==================================
"""
"""
本章讲解：多分支条件判断
语法：
if 条件1：
    语句块1
elif 条件2：
    语句块2
elif 条件3：
    语句块3
…………
else:
    语句块
"""

# 0-6岁为婴幼儿，7-12岁为少儿，13-17岁为青少年，18-45岁为青壮年；46-69为中年；69岁以上为老年(老者)
age = input("请输入年龄：")
if age.isnumeric():
    age = int(age)
    if 0 < age <= 6:
        print("婴幼儿阶段，玩泥巴")
    elif 7 <= age <= 12:
        print("少儿阶段，玩弹钢珠")
    elif 13 <= age <= 17:
        print("青少年，好好学习不要早恋")
    elif 18 <= age <= 45:
        print("努力拼搏，争取和老徐一样开上宝马")
    elif 46 <= age <= 69:
        print("带娃，享受生活")
    else:
        print("下象棋，饮酒当歌：年华一去不复返，是非成败转头空")
else:
    print("请输入一个数字")

"""
天王盖地虎  小鸡炖蘑菇
宝塔镇河妖  蘑菇放辣椒

开始对暗号：第一次对暗号是对天王盖地虎，第二次对暗号是对小鸡炖蘑菇
两个暗号都对上了，请打印：自己人，请进来。     暗号对错了，请打印：来人，拖出去砍了！
"""
# ctrl+alt+L 调整格式快捷键（可以和QQ有冲突，需要重设QQ按键）

cipher1 = input("来者何人，请对暗号天王盖地虎，请接下一句：\n")
if cipher1 == "宝塔镇河妖":
    cipher2 = input("请对第二个暗号，小鸡炖蘑菇：\n")
    if cipher2 == "蘑菇放辣椒":
        print("自己人，请进来。")
    else:
        print("来人，拖出去砍了！")
else:
    print("来人，拖出去砍了！")

"""
酒驾判定：
酒精含量<20 不构成饮酒行为
20<=酒精含量<80 已经达到饮酒驾驶标准
酒精含量>=80 已经达到醉酒驾驶标准
"""

alcohol_content = int(input("酒精含量："))
if alcohol_content < 20:
    print("不构成饮酒行为")
elif 20 <= alcohol_content < 80:
    print("已经达到饮酒驾驶标准")
else:
    print("已经达到醉酒驾驶标准")

