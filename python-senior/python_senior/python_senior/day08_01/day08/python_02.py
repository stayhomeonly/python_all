"""
==================================
文件名: python_02
作者:    Liu
时间:   2022/6/12-14:07
==================================
"""
"""
self  代表当前实例对象，谁调用此时的方法就代表谁

类属性是所有对象共同享有的属性,实例属性是实例对象独有的属性
私有属性: 类属性前加上两个下划线,这个属性就是私有属性,只能在该类中使用
"""


class Student:  # 声明一个类，类名是Student
    stu_id = ''  # 类属性 所有对象共享的属性
    stu_name = ''
    stu_sex = ''
    __stu_age = 0  # 类属性前加上两个下划线 这个属性就是私有属性 只能在该类中使用

    def study(self):  # 声明了一个方法
        print(self.stu_name, '正在学python')


stu01 = Student()  # 创建了Student类的实例对象stu01

# print(stu01.stu_age)  # 私有属性只可以在类的内部使用

# 通过实例对象调用属性和方法
stu01.stu_name = '小花'  # 实例属性
stu01.stu_id = '1001'
stu01.stu_sex = '女'

print(stu01.stu_name)  # 小花

stu01.study()  # 小花 正在学python

stu02 = Student()  # 创建了Student类的实例对象stu02
print(stu02.stu_name)  # 空

stu02.stu_name = '小徐'
print(stu02.stu_name)  # 小徐

stu02.study()  # 小徐 正在学python
