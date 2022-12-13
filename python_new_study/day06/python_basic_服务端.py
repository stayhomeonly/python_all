# coding:utf-8
"""
#@Time：2022/10/15-19:31
#@file：python_basic_服务端
#@Project:python_new_study
#@Content:
"""
# 服务端：接收客户端消息并显示

from socket import *

# 创建socket对象

s=socket(AF_INET,SOCK_STREAM)

# 绑定监听端口
s.bind(('localhost',6363))

# 监听
s.listen()

# 等待消息
conn,adr = s.accept()

# 接收消息
msg=conn.recv(1024)

print("-------:",msg.decode())

s.close()