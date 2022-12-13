# coding:utf-8
"""
#@Time：2022/9/29-10:59
#@file：python_basic_62
#@Project:python_new_study
#@Content:

"""
total = 0
l1 = [1, 2, 3, 4, 5, 6]
for i in l1:
    if i % 2 == 0:
        total = total + i
print(total)

l = [66000,
     64000,
     62000,
     60000,
     58000,
     56000,
     54000,
     52000,
     50000,
     48000,
     46000,
     44000,
     42000,
     40000,
     38000,
     36000,
     34000,
     32000,
     30000,
     28000,
     26000,
     24000,
     22000,
     20000,
     18000,
     16000,
     14000,
     12000,
     10000,
     8000,
     6000,
     4000,
     2000,
     0
     ]
total1=0
for i in l:
    a = i * 0.55 / 100
    total1=total1 + a
print(total1)
