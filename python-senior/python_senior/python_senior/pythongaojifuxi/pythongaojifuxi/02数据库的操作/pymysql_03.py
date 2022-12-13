"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-14:35
知识点: 
---------------------------------
"""
# 数据库的封装
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


if __name__ == '__main__':
    db = DBUtils()
    print(db.conn, db.cur)
    c = db.cur.execute('select * from tb_user')
    print(c)
    db.close()
