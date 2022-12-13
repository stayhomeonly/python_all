from configparser import ConfigParser
from python_basic64 import case_dir


# 创建解析类的实例对象
cp = ConfigParser()

# 读取文件
# cp.read(r'./config.ini', encoding="utf-8")  # 读取文件
# host = cp.get('mysql', 'host')  # 通过解析类的提供的get 方法 获取值  需要的入参是 section和option
# print(host)
# print(type(host)) # 解析类提供的get方法返回的是 str
#
# port = cp.get("mysql", "port")
# print(port)
# print(type(port))
#
# p = cp.getint("mysql","port")
# print(p)
# print(type(p))


# 读取文件
cp.read(case_dir, encoding="utf-8")  # 读取文件
host = cp.get('mysql', 'host')  # 通过解析类的提供的get 方法 获取值  需要的入参是 section和option
print(host)
print(type(host)) # 解析类提供的get方法返回的是 str