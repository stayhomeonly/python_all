"""
==================================
文件名: python_01
作者:    Liu
时间:   2022/6/12-10:33
==================================
"""
"""
知识点1：面向对象：面向对象是一个编程思想（万物皆可作为对象）
知识点2：
什么是类？
    1、特指某一类的事物（猫类、狗类）
    2、类包含属性和方法,属性就是变量，方法就是函数。只不过在类中叫变量和方法
什么是对象？
    对象能够调用类中的属性和方法，就是当你实例化对象时，这个对象就具备了类的所有属性和方法。
    对象和类的关系：一个类可以有无数个对象
"""


# 创建一个类
class Cat:
    color = ''
    name = ''
    age = ''

    def eat(self, food):
        print("我最喜欢吃：{}".format(food))

    def run(self):
        print("我四处溜达溜达，一会儿就回来~")


# 具体化这个类
Tom = Cat()  # 创建对象（实例化对象）
kitty = Cat()
# 为我们的这个对象属性赋值
Tom.color = "蓝色"
Tom.name = 'tom'
Tom.age = 1
print(Tom.color)
kitty.color = "粉色"
print("kitty猫的颜色是：" + kitty.color)  # 拼接字符串

# 对象可以调用类的方法
Tom.eat("小鱼")
Tom.eat("猫粮")
Tom.run()


# 自己定义一个类（不能使用狗），并且声明类属性和类方法，创建该类的对象，并且为对象的属性赋值，再调用该对象的方法
class House:
    city = '上海'
    type = ''
    age = ''

    def price(self, place):
        print('这样价格的房子在：{}'.format(place))

    def lease_price(self, price):
        print("单间出租：{}元".format(price))


villa = House()  # 创建对象，别墅
Under_the_overpass = House()  # 创建对象，天桥底下

print(villa.city)
villa.age = 0
print(villa.age)

# 调用方法1,对象名.方法名()
villa.price("东方星光")

# 调用方法2
Under_the_overpass.lease_price(2500)
