"""
#@Time：2022/8/18-20:32
#@file：python_basic_54(time,datetime)
#@Project:python_new_study
#@Content:

"""
import time

# s_time = time.time()  # 打印时间戳
#
# time.sleep(5)

# print(f"cost{time.time() - s_time}")  # 程序运行了5秒

# 将⼀个时间戳转换为当前时区的struct_time。若secs参数未提供,则以当前时间为准
print(time.localtime())
# 将⼀个struct_time转化为时间戳.
print(time.mktime(time.localtime()))

# 把⼀个代表时间的元组或者struct_time（如由
# time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传⼊
# time.localtime()。
# 举例： time.strftime(“%Y-%m-%d %X”, time.localtime()) #输出’2017-10-01 12:14:23'
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 时间转换成字符串

time_str = time.strftime("%Y-%m-%d %H:%M:%S")
# time.strptime(string[, format]) ：把⼀个格式化时间字符串转化为struct_time。实际上它
# 和strftime()是逆操作。
# 举例： time.strptime(‘2017-10-3 17:54’,”%Y-%m-%d %H:%M”) #输出
# time.struct_time(tm_year=2017, tm_mon=10, tm_mday=3, tm_hour=17, tm_min=54,
# tm_sec=0, tm_wday=1, tm_yday=276, tm_isdst=-1)
print(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))  # 字符串转换时间



