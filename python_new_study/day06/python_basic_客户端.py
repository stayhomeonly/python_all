# coding:utf-8
"""
#@Time：2022/10/15-19:21
#@file：python_basic_客户端
#@Project:python_new_study
#@Content:

"""

# 客户端：发送消息给服务端

from socket import *

# 创建socket对象
# AF_UNIX 本机通信,AF_INET(IPV4),AF_INET6(TPV6)
# SOCK_STREAM(TCP),SOCK_DGRAM(UDP)
s=socket(AF_INET,SOCK_STREAM) # 第一个参数代表通信，第二个参数代表协议

# 和目标建立连接
s.connect(('localhost',6363)) # 因为服务端和客户端在一个电脑上，所以用localhost

# 发送消息
s.send("你好！服务端".encode()) #.encode()对字符串进行编码

