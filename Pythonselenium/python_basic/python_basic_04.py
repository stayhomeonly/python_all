"""
#@Time：2022/5/21-17:42
#@file：python_basic_04
#@Project:python_basic05.py
#@Content:

"""
# 打印楼层例如L2-201
for i in range(1, 6):
    print(f"==========={i}层============")
    for j in range(1, 10):
        print(f"L{i}-{i}0{j}室")  # 用f支持括号里面的内容也就是""里面的内容

'''
continue的语法作用，只要程序一遇到continue，本次循环就不继续了，直接进入到下一次循环
break的语法作用是，只要程序一遇到break，就会结束本次循环，注意如果是多层循环，只结束当前这一层的循环
'''
# 打印楼层例如L2-201，到第三层自动跳过
for i in range(1, 6):
    print(f"==========={i}层============")
    for j in range(1, 10):
        if i == 3:
            continue
        print(f"L{i}-{i}0{j}室")  # 用f支持括号里面的内容也就是""里面的内容


# 当走到第三层的时候，小循环执行了吗？执行的
# 但是实际情况是三层不想被执行，完全跳过怎么执行，用法
for i in range(1, 6):
    if i == 3:
        continue # 直接要三层不走
    print(f"==========={i}层============")
    for j in range(1, 10):

        print(f"L{i}-{i}0{j}室")  # 用f表示括号里面的内容也就是""里面的内容


# 如果想走到404的时候自动跳过怎么做呢？

for i in range(1, 6):
    if i == 3:
        continue # 直接要三层不走
    print(f"==========={i}层============")
    for j in range(1, 10):
        if i == 4 and j == 4:
            print("不走了")
            break

        print(f"L{i}-{i}0{j}室")  # 用f支持括号里面的内容也就是""里面的内容
