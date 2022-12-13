"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/17-11:40
   contents:
-------------------------------------------------
"""
import pymysql


class DBUtils(object):
    count = -1

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

    # 封装查询一条数据
    def find_one(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
            elif params is not None:
                self.cursor.execute(sql, params)
            return self.cursor.fetchone()  # 从结果集中获取单条数据
        except Exception as e:
            print("查询单条数据失败！", e)

    # 封装查询所有数据
    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
            elif params is not None:
                self.cursor.execute(sql, params)
            return self.cursor.fetchall()  # 从结果集中获取所有数据
        except Exception as e:
            print("查询单条数据失败！", e)


if __name__ == '__main__':
    db = DBUtils()
    data = db.find_all("select *from account;")
    print(data)
    db.close()
