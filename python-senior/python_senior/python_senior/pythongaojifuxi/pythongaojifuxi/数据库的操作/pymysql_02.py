"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-14:22
知识点: 
---------------------------------
"""
import pymysql

# 第一步 建立连接对象
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)
# 第二步  通过连接对象获取游标对象
cur = conn.cursor()
print(cur)
# 第三步  通过游标的execute方法来执行sql
cou = cur.execute('select * from tb_user')
print(cou)

# 第四步 通过游标获取结果集中的数据
# data = cur.fetchone()
# data = cur.fetchmany(2)
data = cur.fetchall()
print(data, type(data))

# 第五步 关闭游标 关闭连接
cur.close()
conn.close()
