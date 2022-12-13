"""
==================================
文件名: python_05
作者:    Liu
时间:   2022/6/12-16:14
==================================
"""
"""
总结类:
1、类中虽然有属性和方法，但是都不是必须的
2、类的作用(在实际工作中，更多的是把数据库中的表，抽象为一个类，数据库表中的一行数据就是一个具体的对象)
"""


# 案例1：定义一个最简单的类（没有属性和方法）
class A:
    pass


# 案例2： 只有属性的类，可以保存数据。Emp类在创建对象的同时需要传入3个参数，创建的对象自动就有了这三个属性
class Emp:
    emp_job = 'engineer'

    def __init__(self, no, name, sal):
        self.emp_no = no
        self.emp_name = name
        self.emp_sal = sal


emp01 = Emp('1001', 'xiaohua', 5000)
print(emp01.emp_name, emp01.emp_job)
emp02 = Emp('1002', 'xiaoxu', 6000)
print(emp02.emp_name, emp01.emp_job)


# 案例3：类中也可以只有方法，没有属性。封装的方法可以通过对象无限次调用，极大的减少了代码的冗余
class Math:
    @staticmethod
    def my_add(a, b):  # 封装了一个两位数加法运算
        return a + b

    @staticmethod
    def my_sum(*args):  # 封装了一个求和方法,使用的是不定长参数，可以传入0-N个参数。
        return sum(args)


print(Math.my_add(1, 1))  # 2
print(Math.my_sum())  # 0
print(Math.my_sum(1, 2, 3, 4, 5))  # 15
