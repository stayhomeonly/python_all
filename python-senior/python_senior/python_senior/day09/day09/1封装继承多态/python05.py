"""
==================================
文件名: python05
作者:    Liu
时间:   2022/6/26-16:42
==================================
"""

"""
方法重写/方法覆盖:子类继承父类,子类和父类具有相同的方法
"""


class Animal:
    def eat(self):
        print('父类的干饭方法!!!')


class Dog(Animal):  # Dog类继承了Animal
    def eat(self):
        print('子类的干饭方法!')


am = Animal()
am.eat()  # 父类的干饭方法!!!

dd = Dog()
dd.eat()  # 子类的干饭方法!

# 多态: 子类的对象调用父类的方法
super(Dog, dd).eat()  # 父类的干饭方法!!!
