"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/10-16:00
   contents:
-------------------------------------------------
"""
"""
使用db_utils01查询account表,和新增一个用户
"""
from db_utils01 import DBUtils

# 查询
# db = DBUtils()
# db.cursor.execute("select *from account;")
# data = db.cursor.fetchall()
# print(data)
# db.close()

# 新增
db = DBUtils()
count = db.cursor.execute("insert into account(name,age,nickName) values(%s,%s,%s);", ('小花1', 20, '花花'))
db.conn.commit()
db.close()
