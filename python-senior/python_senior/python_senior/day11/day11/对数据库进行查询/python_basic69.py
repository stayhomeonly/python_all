"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/10-15:41
   contents:
-------------------------------------------------
"""
"""
知识点：python操作mysql，通过占位符查询
"""
# 第一步：导入第三方模块，pymysql是一个第三方的模块(我们需要先进行安装),再导包，然后通过pymysql操作mysql数据库
import pymysql

# 第二步：获取连接对象(我们需要指定mysql服务器的ip地址，端口号，用户名，密码，指定的库名)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')

# 第三步：获取一个游标对象
cursor = conn.cursor()

# 第四步：把需要更换的数据通过%s进行占位，再通过元组进行赋值
# [这种方式更加的安全,它会优先发送sql语句结构，再发送参数数据，这样就避免了sql注入]
count = cursor.execute('select *from tb_user where name=%s;', ('xiaohua',))
print(count)

# 第五步：获取数据,cursor里面的数据只能获取一次,获取完了就没有了
data = cursor.fetchall()
print(data)

# 第六步：关闭游标
cursor.close()

# 第七步：关闭连接
conn.close()
