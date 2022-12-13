"""
==================================
文件名: python_02
作者:    Liu
时间:   2022/6/12-14:07
==================================
"""
"""
self  代表当前实例对象，谁调用此时的方法就代表谁
"""


class Student:  # 声明一个类，类名是Student
    stu_id = ''
    stu_name = ''
    stu_sex = ''

    def study(self):  # 声明了一个方法
        print(self.stu_name, '正在学python')


stu01 = Student()  # 创建了Student类的实例对象stu01

# 通过实例对象调用属性和方法
stu01.stu_name = '小花'
stu01.stu_id = '1001'
stu01.stu_sex = '女'
stu01.study()  # 小花 正在学python

stu02 = Student()  # 创建了Student类的实例对象stu02
stu02.stu_name = '小徐'
stu02.study()  # 小徐 正在学python
