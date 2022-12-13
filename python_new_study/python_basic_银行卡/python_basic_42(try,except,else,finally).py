"""
#@Time：2022/8/6-21:38
#@file：python_basic_42
#@Project:python_new_study
#@Content:

"""
'''
try:
    可能出现异常的代码
except Exception as e:
    出现异常时执行的代码
else:
    没有出现异常执行的代码
finally:
    无论是否出现异常都会执行(记录日志，关闭资源)
'''
list1=[1,2,3,4555,777,0,18]
for i in list1:
    try:
        r=10/i
        print(r)
    except  Exception as e:   # Exception 捕获的错误类型，e保存具体错误内容
        print("出现非0错误",e)
    else:
        print('正常执行')
    finally:
        print('执行完毕')