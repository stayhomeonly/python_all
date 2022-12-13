"""
==================================
文件名: python04
作者:    Liu
时间:   2022/6/26-16:15
==================================
"""

"""
封装:
第一层面的封装:把属性和方法组合成一个类,就是简单封装
第二层面的封装:类中把某些属性和方法隐藏起来(或者定义为私有),只能在类的内部使用、外部无法访问,或者留下少量的函数供外部访问
"""

# 怎么形容一个学生?
# 弊端: 太零散
name1 = 'xiaohua'
age1 = 18
sex1 = '女'


class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


one = Student("老刘", 38, '男')
two = Student("老王", 33, '男')

print('姓名:{},年龄:{},性别:{}'.format(one.name, one.age, one.sex))  # 姓名:老刘,年龄:38,性别:男


# 第二层面的封装: 控制访问的权限
# 我们可以把所有的属性设置为私有,不在允许对象访问

class Student1:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex


three = Student1("老徐", 18, '男')


# print('姓名:{},年龄:{},性别:{}'.format(three.name, three.age, three.sex))  无法访问

# 问题来了: 现在我们把name、age、sex全部设置为私有,但是又想通过我们指定方式访问或修改属性,怎么办?

class Stu1:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# 这样有效的控制了访问和修改的权限,name、age、sex都可以访问,但只有age允许修改

four = Stu1("xiaohua", 18, '女')
print('姓名:{},年龄:{},性别:{}'.format(four.get_name(), four.get_age(), four.get_sex()))  # 姓名:xiaohua,年龄:18,性别:女
four.set_age(20)
print('姓名:{},年龄:{},性别:{}'.format(four.get_name(), four.get_age(), four.get_sex()))  # 姓名:xiaohua,年龄:20,性别:女

