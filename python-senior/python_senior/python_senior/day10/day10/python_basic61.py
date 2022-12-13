"""
模块的导入  当前模块导入其他模块的类容 我们就可以使用其他模块的变量 函数或者类
导入的方式1.
导入等个模块 import 包名.模块名 as 别名 （不推荐使用 如果导入了多个模块 可以会存在相同的方法名 会造成bug）
"""
import login_and_regist as lr
import day09.aa as ll
print(lr.user)
print(lr.login('xiaohua','a123456'))
print(lr.register("12345",'123455','12232'))
print(ll.a)