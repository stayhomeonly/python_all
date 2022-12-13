"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/17-11:19
   contents:
-------------------------------------------------
"""
"""
我们每次操作数据库都要进行连接和关闭，所以我们可以封装连接和关闭这些步骤，封装以后我们每次调用就可以。
"""
import pymysql


class DBUtils(object):
    # 封装连接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                        db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库工具类连接出现异常，请检查DBUtils中的__init__方法！")
            print(e)

    # 封装关闭游标和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 封装查询结果集有多少条数据：条目数
    # 如果execute()括号里只传一个参数，我们需要运行 cursor.execute(sql)
    # 如果execute()括号里传二个参数，我们需要运行 cursor.execute(sql, 元组)
    def find_count(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
            return self.count
        except Exception as e:
            print("查询数据库条目数失败！", e)

    # 封装增删改
    # 如果execute()括号里只传一个参数，我们需要运行 cursor.execute(sql)
    # 如果execute()括号里传二个参数，我们需要运行 cursor.execute(sql, 元组)
    def cud(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            if isinstance(params, tuple):
                self.count = self.cursor.execute(sql, params)
            if isinstance(params, list):
                self.count = self.cursor.executemany(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print("增删改执行失败！", e)


if __name__ == '__main__':  # 当前模块下运行
    # __init__ 是在创建对象的时候自动调用的
    db = DBUtils()  # 创建对象时，自动创建了conn和cursor

    # 自测查询数据条目数
    # count = db.find_count("select *from tb_user where name=%s and passwd=%s", ('xiaohua', '123456'))
    # print(count)

    # 自测增删改
    # 新增单个
    # count = db.cud("insert into account(name,age,nickName) values(%s,%s,%s);", ('小花2', 20, '花花'))
    # print(count)
    # 新增多个
    count = db.cud("insert into account(name,age,nickName) values(%s,%s,%s);",
                               [('小花1', 20, '花花'), ('小花2', 20, '花花'), ('小花3', 20, '花花')])
    print(count)
    db.close()
