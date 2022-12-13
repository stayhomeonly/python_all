"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/10-15:05
   contents:
-------------------------------------------------
"""
"""
知识点：python操作mysql，进行增删改
"""

# 第一步：导入第三方模块，pymysql是一个第三方的模块(我们需要先进行安装),再导包，然后通过pymysql操作mysql数据库
import pymysql

# 第二步：获取连接对象(我们需要指定mysql服务器的ip地址，端口号，用户名，密码，指定的库名)
# mysql默认的端口号：3306   oracle默认的端口号：1521 http默认的端口号80 8080，https默认的端口号443
# 127.0.0.1或者localhost代表本地ip地址
# db是database数据库的缩写
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)  # <pymysql.connections.Connection object at 0x000001A7491A6048>

# 第三步：获取一个游标对象
cursor = conn.cursor()  # 游标能够储存结果集

# 第四步：通过游标对象执行sql语句，调用execute执行
'''
通过execute方法提供的另外一个方式操作数据库 execute(sql,params)
把需要更换的数据通过%s进行占位，再通过元组进行赋值[这种方式更加的安全,它会优先发送sql语句结构，再发送参数数据，这样就避免了sql注入]
'''
# 新增
# count = cursor.execute("insert into account(name,age,nickName) values(%s,%s,%s);", ('小花', 20, '花花'))
# 删除
# count = cursor.execute("delete from account where name=%s;", ('小花',))

# 修改
count = cursor.execute("update account set name=%s where id=%s;", ('xiaohua', 17))
print(count)
# 第五步：增删改需要提交,不要忘记了，否则数据库数据不会落库
conn.commit()

# 第六步：关闭游标
cursor.close()

# 第七步：关闭连接
conn.close()
