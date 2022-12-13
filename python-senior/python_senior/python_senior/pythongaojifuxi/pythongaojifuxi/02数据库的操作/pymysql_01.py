"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-11:27
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
# 第三步 获取游标对象之后 我们可以用游标对象的 execute 方法来执行我们的sql   execute 方法会返回影响的条目数
# 增
# cur.execute("INSERT into account(NAME,age,nickname) VALUES('xiaohua',18,'校花')")
# cur.execute('DELETE FROM account WHERE age = 18')
count = cur.execute("UPDATE account SET age = 19 WHERE name = 'xiaohua'")
print(count)
# 第四步 对数据的数据进行了增删改 要记得提交
conn.commit()
# 提交完了 要关闭游标和连接
cur.close()
conn.close()

