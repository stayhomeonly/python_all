"""
-------------------------------------------------
   File Name:python_basic75
   Author:Lee
   date: 2021/9/15-17:18
   综合练习：方法设计、和面向对象 改成填写代码的方式
-------------------------------------------------
"""
"""
作业：
1、创建一个类 班级类
2、属性为： 班级编号,班级额定人数，班级实际人数,班级各个课程总成绩(比如 python基础:888、功能测试:999、数据库:777)用字典保存,
            班级学员最高总成绩,班级学员最低总成绩，班级是否已经毕业(使用bool类型声明该变量)
   注意,属性不用声明,直接用__init__方法，为属性赋值
3、设计一个__init__魔法方法，创建对象的时候自动为所有属性赋值。
4、有两个实例方法: 
    1、根据班级号获取班级的人数并返回
    2、获取班级班级学员最高总成绩,和班级学员最低总成绩的值并返回(入参为班级号，出参为字典)
    3、设计一个方法如果传入的是已经毕业的班级,返回班级编号,班级总成绩和就业薪资，返回一个字典(入参为一个参数)。
    4、重新设计第三个题目，不过入参为两个其中有一个使用默认值入参。
    5、传入多个班级，返回各个班级总成绩最高的班级号(入参为 不定长参数)
    6、传入多个班级，返回各个班级总成绩最高的班级号(入参为 列表)
5、创建类方法，该方法可以直接获取各个课程班级额定人数并且返回。
6、创建四个班级对象分别为 TSD01(已经毕业) TSD02(已经毕业) TSD03(未毕业) TSD04(未毕业)
7、为已经毕业的所有班级添加 实例属性 毕业平均薪资
8、调用实例方法1,2,3
"""


class Class:
    # 班级编号,班级额定人数，班级实际人数,班级各个课程总成绩(比如 python基础:888、功能测试:999、数据库:777)用字典保存,
    # 班级学员最高总成绩,班级学员最低总成绩，班级是否已经毕业(使用bool类型声明该变量)
    def __init__(self, class_id, rated_count, actual_count, total_sc, max_sc, min_sc, is_finish):
        self.class_id = class_id
        self.rated_count = rated_count
        self.actual_count = actual_count
        self.total_sc = total_sc
        self.max_sc = max_sc
        self.min_sc = min_sc
        self.is_finish = is_finish

    # 1、获取班级的实际人数并返回
    def get_count(self):
        return self.actual_count

    # 2、获取班级班级学员最高总成绩, 和班级学员最低总成绩的值并返回(出参为字典)
    def get_sc(self):
        return {"最高成绩": self.max_sc, "最低成绩": self.min_sc}

    # 3、设计一个方法如果传入的是已经毕业的班级,返回班级编号,班级总成绩和就业薪资，返回一个字典(入参为一个参数)。
    # 如果是未毕业返回 班级编号、班级总成绩
    def get_tol(self):
        if self.is_finish:
            return {'班级编号': self.class_id, '班级总成绩': sum(list(self.total_sc.values())), '就业薪资': self.sal}
        else:
            return {'班级编号': self.class_id, '班级总成绩': sum(list(self.total_sc.values()))}


# class_id, rated_count, actual_count, total_sc, max_sc, min_sc, is_finish
tsd24 = Class(1001, 60, 50, {"python": 888, "java": 777, "database": 999}, 999, 111, False)
tsd22 = Class(1002, 60, 50, {"python": 888, "java": 777, "database": 999}, 999, 111, True)
tsd22.sal = 1000

print(tsd24.get_count())
print(tsd24.get_sc())
print(tsd24.get_tol())
print(tsd22.get_tol())


