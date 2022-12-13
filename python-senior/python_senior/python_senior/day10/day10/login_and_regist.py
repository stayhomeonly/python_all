# 模拟下数据库的数据  假设数据库只有一下数据
user = {"username": "xiaohua", "password": "a123456"}


# 模拟注册功能
def register(username, password, re_password):
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif username == user.get("username"):
        return {"code": 1002, "msg": "用户名已注册"}
    elif len(password) == 0:
        return {"code": 1003, "msg": "密码不能为空"}
    elif password != re_password:
        return {"code": 1004, "msg": "两次密码输入不一致"}
    elif not (6 <= len(username) <= 18 and 6 <= len(password) <= 18):
        return {"code": 1005, "msg": "用户名和密码必须在6-18位之间"}
    else:
        return {"code": 1000, "msg": "注册成功"}


# 模拟下登录的功能
def login(username, password):
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif len(password) == 0:
        return {"code": 1002, "msg": "密码不能为空"}
    elif username == user.get("username") and password == user.get("password"):
        return {"code": 1003, "msg": "登录成功"}
    else:
        return {"code": 1004, "msg": "用户名或者密码输入错误"}


print('*******************')
print(__name__)
if __name__ == '__main__':
    print("我只会在当前模块执行")
