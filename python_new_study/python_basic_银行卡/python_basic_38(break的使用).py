"""
#@Time：2022/7/29-21:47
#@file：python_basic_38(break的使用)
#@Project:python_new_study
#@Content:

"""
count1 = 1
while count1 < 10:

    while count1==5:
        break   # 直接终止本层的循环
    break
    print(count1)  # 不显示

# 打印0-9不要4
count2=0
while count2 < 10:
    if count2 == 4:
        count2 += 1
        continue  #continue结束本次循环 ，进入下一次循环
    print(count2)
    count2 += 1



