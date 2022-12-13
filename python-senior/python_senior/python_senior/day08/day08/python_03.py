"""
==================================
文件名: python_03
作者:    Liu
时间:   2022/6/12-14:18
==================================
"""
"""
实例方法：最少需要包含一个self参数，用来绑定调用此方法的实例对象
类方法： 用装饰器@classmethod 来标识其为一个类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数，
可以通过类本身和实例对象去访问。
静态方法：用装饰器@staticmethod 来标识其为静态方法，静态方法没有self/cls这样特殊的参数，静态方法无法调用任何类属性和类方法
"""


class Emp:
    emp_no = ''
    emp_name = ''
    emp_sal = 2500

    # 实例方法，计算年薪
    def year_sal(self):
        return self.emp_sal * 12

    # 类方法,计算请假天数的扣款
    @classmethod
    def fine(cls, day):  # 类方法，cls代表类本身
        return cls.emp_sal / 22 * day

    # 静态方法
    @staticmethod
    def select():  # 静态方法，没有self和cls这样的特殊参数，无法使用类属性和类方式
        return "查询结果为：KING是最高领导"


# 实例方法：使用对象进行调用
emp01 = Emp()  # 创建对象
print(emp01.year_sal())  # 通过实例对象.方法名()去调用

# 类方法：使用对象进行调用
emp02 = Emp()
emp02.emp_sal = 5000
print(emp02.fine(5))  # 568.1818181818182

# 推荐使用类名.方法名
print(Emp.fine(5))  # 568.1818181818182
Emp.emp_sal = 5000  # 重新为类属性赋值
print(Emp.fine(5))  # 1136.3636363636365

# 静态方法：
emp03 = Emp()  # 推荐使用类名.方法名
print(emp03.select())

print(Emp.select())
