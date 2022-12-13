"""
知识点1：布尔类型
知识点2：类型转换
"""

# 知识点1：布尔类型(bool)有两个值，一个是True(真、成立)，一个是False(假、不成立)

boo1 = 10 > 20
print(boo1)  # False
boo2 = 20 > 10
print(boo2)  # True
print(type(boo1), type(boo2))  # <class 'bool'> <class 'bool'>

# 知识点2：类型转换(int/float/str/bool)

# 1、int和float之间的转换
a = 10
flt = float(a)  # 把 int类型转换为 float
print(flt)  # 10.0

it = int(10.999999)  # 把10.5转换为 整数类型 并且赋值给 it
print(it)  # 10 ,注意：小数转整数的时候是直接舍去小数点后边的数据的。(截取整数位)

# 2、字符串和数字的转换

str1 = str(10)  # 把数字转为字符串
print(str1, type(str1))  # 10 <class 'str'>

int1 = int("10")  # 把数字类型的字符串 转换为 数字类型
print(int1, type(int1))  # 10 <class 'int'>

# 布尔类型和数字、字符串之间的转换
# 1、数字类型和字符串 转为 布尔类型
boo1 = bool(1.5)  # 注意 数字转布尔类型 非0为True
print(boo1, type(boo1))  # True <class 'bool'>

boo2 = bool(" ")  # 注意 str转布尔类型 非空为True,非None为True
print(boo2, type(boo2))  # True <class 'bool'>

# 布尔类型转为 数字
int2 = int(True)
print(int2)  # 1
int3 = int(False)
print(int3)  # 0










