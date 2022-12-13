"""
#@Time：2022/8/15-20:02
#@file：python_basic_53
#@Project:python_new_study
#@Content:

"""
import os

print(os.getcwd()) #当前工作目录,D:\FENG1234\python_new_study\data

# 获取当前目录下的文件
print(os.listdir)

#删除一个目录
# os.remove('文件名')

'''
得到当前⼯作⽬录，即当前Python脚本⼯作的⽬录路径: os.getcwd()
返回指定⽬录下的所有⽂件和⽬录名:os.listdir()
函数⽤来删除⼀个⽂件:os.remove()
删除多个⽬录：os.removedirs（r“c：\python”）
检验给出的路径是否是⼀个⽂件：os.path.isfile()
检验给出的路径是否是⼀个⽬录：os.path.isdir()
判断是否是绝对路径：os.path.isabs()
检验给出的路径是否真地存:os.path.exists()
返回⼀个路径的⽬录名和⽂件名:os.path.split() e.g
os.path.split('/home/swaroop/byte/code/poem.txt') 结果：
('/home/swaroop/byte/code', 'poem.txt')
分离扩展名：os.path.splitext() e.g os.path.splitext('/usr/local/test.py')
 结果：('/usr/local/test', '.py')
获取路径名：os.path.dirname()
获得绝对路径: os.path.abspath() 
获取⽂件名：os.path.basename()
运⾏shell命令: os.system()
读取操作系统环境变量HOME的值:os.getenv("HOME")
返回操作系统所有的环境变量： os.environ
设置系统环境变量，仅程序运⾏时有效：os.environ.setdefault('HOME','/home/alex')
给出当前平台使⽤的⾏终⽌符:os.linesep Windows使⽤'\r\n'，Linux and MAC使⽤'\n'
指示你正在使⽤的平台：os.name 对于Windows，它是'nt'，⽽对于Linux/Unix⽤户，它
是'posix'
'''