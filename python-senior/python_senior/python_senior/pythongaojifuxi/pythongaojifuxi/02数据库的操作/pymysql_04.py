"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-15:03
知识点: 
---------------------------------
"""
import pymysql


class DBUtils():

    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
            # print(conn)
            # 第二步  通过连接对象获取游标对象
            self.cur = self.conn.cursor()
            # print(cur)
        except Exception as e:
            print('数据库连接有异常 请检出DBUtils的init方法')
            print(e)

    def close(self):
        self.cur.close()
        self.conn.close()

    # 封装查询结果集的条目数
    def find_count(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cur.execute(sql)
                return self.count
            if params is not None:
                self.count = self.cur.execute(sql, params)
                return self.count
        except Exception as e:
            print('查询数据库条目数失败', e)

    # 封装增删改
    def cud(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cur.execute(sql)
                self.conn.commit()
                return self.count
            if params is not None:
                self.count = self.cur.execute(sql, params)
                self.conn.commit()
                return self.count
        except Exception as e:
            print('对数据库数据进行增删改失败', e)

    # 封装从数据库中捞一条数据
    def find_one(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cur.execute(sql)
                return self.cur.fetchone()
            if params is not None:
                self.count = self.cur.execute(sql, params)
                return self.cur.fetchone()
        except Exception as e:
            print('从数据库获取单条数据失败', e)

    # 封装从数据库中捞取所有数据
    def find_all(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cur.execute(sql)
                return self.cur.fetchall()
            if params is not None:
                self.count = self.cur.execute(sql, params)
                return self.cur.fetchall()
        except Exception as e:
            print('从数据库获取所有数据失败', e)


if __name__ == '__main__':
    db = DBUtils()
    # c = db.find_count('select * from tb_user')
    # print(c)
    # db.cud("INSERT into account(NAME,age,nickname) VALUES('xiaomei',18,'校花')")
    # d = db.find_one('select * from tb_user')
    # print(d)
    d2 = db.find_all("select * from tb_user where name = 'xiaohua'")
    print(d2)
