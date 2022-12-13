"""
#@Time：2022/8/14-15:10
#@file：python_basic_68
#@Project:python_new_study
#@Content:

"""
 # python 连接数据库
import  pymysql
import random

# 需要先创建一个数据库，才能连接
host='localhost'
port=3307
user='root'
password='123456'
db='51db'
charset='utf8'

# 创建数据库库连接对象，并建立连接
db=pymysql.Connect(host=host,port=port,user=user,passwd=password,db=db,charset=charset)
print("数据库已经连接")
# 创建游标对象(执行sql,处理查询结果)
cursor=db.cursor()
for x in range(3,13):
    num=x # id
    name = random.choice(['王五','李六','老七','大宝'])
    age=random.choice([2,13,32,32,32,43,35,43])

    # 编写sql语句,列名,列数据类型,拼接时字符串中的单引号需要加上
    # sql='CREATE TABLE stu(id int,name varchar(10),age int)'
    sql="insert into stu values("+str(num)+",'"+name+"',"+str(age)+");"
    """
    拼接字符串的时候用+name+,中间就是变量
    """




    #执行sql
    cursor.execute(sql)

    # 提交
    db.commit()

# 关闭游标
cursor.close()

# 关闭数据库
db.close()