"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/10-15:24
   contents:
-------------------------------------------------
"""
"""
知识点：python操作mysql，查询(查询单条，查询多条，查询所有)
"""
# 第一步：导入第三方模块，pymysql是一个第三方的模块(我们需要先进行安装),再导包，然后通过pymysql操作mysql数据库
import pymysql

# 第二步：获取连接对象(我们需要指定mysql服务器的ip地址，端口号，用户名，密码，指定的库名)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')

# 第三步：获取一个游标对象
cursor = conn.cursor()

# 第四步：通过游标去执行sql语句,把结果存在cursor里，并且返回条目数
count = cursor.execute('select *from tb_user;')
print(count)

# 第五步：获取数据,cursor里面的数据只能获取一次,获取完了就没有了
# 第一种：获取结果集的一行数据
# data = cursor.fetchone()
# print(data, type(data))  # 返回一行数据，并且打包成元组

# 第二种：获取结果集的多行数据
# data = cursor.fetchmany(2)  # 获取结果集的2行数据
# print(data)  # 返回多行数据，格式为元组套元组：((数据1),(数据2))

# 第三种：获取所有数据
data = cursor.fetchall()
print(data)

# 第六步：关闭游标
cursor.close()

# 第七步：关闭连接
conn.close()