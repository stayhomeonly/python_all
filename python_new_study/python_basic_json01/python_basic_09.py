"""
#@Time：2022/6/22-21:29
#@file：python_basic_09
#@Project:python_new_study
#@Content:

"""
f=open('phone.txt', encoding='utf-8')
for line in f:# 每循环一次就读一行
    line=line.split() #split分隔符，# 以空格为分隔符，包含 \n
    print(line)
    # height=line[3]
    # weight = line[4]
    # if int(height)>=170 and int(weight)<=50:
    #     print(line)
