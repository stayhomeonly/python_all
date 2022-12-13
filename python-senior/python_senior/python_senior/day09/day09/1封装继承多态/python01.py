"""
==================================
文件名: python01
作者:    Liu
时间:   2022/6/26-15:17
==================================
"""

"""
继承: 子类继承父类,子类就可以使用父类的属性和方法。子类叫派生类,父类叫基类
继承的好处: 减少代码冗余,提高代码重用性(派生类一旦继承基类就可以使用基类的所有的属性和方法)
Java单继承,Python多继承
继承的语法: 在声明类的时候在类名之后使用(基类1,基类2,基类3...)
"""


class Class1:
    pass


class Class2:
    pass


class Class3(Class1):  # Class3继承了Class1
    pass


class Class4(Class1, Class2):  # Class4 继承了 Class1、Class2
    pass
