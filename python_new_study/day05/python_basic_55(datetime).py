"""
#@Time：2022/8/19-21:51
#@file：python_basic_55(datetime).py
#@Project:python_new_study
#@Content:

"""
'''
datetime.date：表示⽇期的类。常⽤的属性有year, month, day；
datetime.time：表示时间的类。常⽤的属性有hour, minute, second, microsecond；
datetime.datetime：表示⽇期时间。
datetime.timedelta：表示时间间隔，即两个时间点之间的⻓度。
datetime.tzinfo：与时区有关的相关信息。（这⾥不详细充分讨论该类，感兴趣的童鞋可以参考
python⼿册）

1. d=datetime.datetime.now() 返回当前的datetime⽇期类型, d.timestamp(),d.today(),
d.year,d.timetuple()等⽅法可以调⽤
2. datetime.date.fromtimestamp(322222) 把⼀个时间戳转为datetime⽇期类型
'''
import datetime
# 返回当前的datetime⽇期类型
d=datetime.datetime.now()
print(d.today())
#
print(d.timetuple())# time.struct_time(tm_year=2022, tm_mon=8, tm_mday=19, tm_hour=21, tm_min=55, tm_sec=57, tm_wday=4, tm_yday=231, tm_isdst=-1)

# 把时间戳转换成时间
print(datetime.datetime.fromtimestamp(222223333))

# 时间的运算
print(d+datetime.timedelta(5,hours=5))

# 时间的替换
print(d.replace(year=2120,month=6))