"""
time: 2022/7/18-10:58
file: demoflask.py
author: ldc
email: 123456@qq.com
"""
import flask, json
from flask import render_template
from day12.数据库封装.DBUtils import DBUtils

app = flask.Flask(__name__)


# 登录接口
@app.route('/login', methods=['post', 'get'])
def login():
    data = flask.request.values  # 接收请求发送过来的数据
    username = data["username"]  # 获取请求中的username
    pwd = data['pwd']  # 获取请求中的pwd
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif len(pwd) == 0:
        return {"code": 1002, "msg": "密码不能为空"}
    else:
        db = DBUtils()
        count = db.find_count("select *from tb_user where name=%s and passwd=%s", (username, pwd))
        db.close()
        if count == 0 or count == -1:
            return {"code": 1007, 'msg': '用户名或者密码错误'}
        else:
            return {"code": 1000, "msg": "登录成功"}


@app.route('/')
def demo1():
    return render_template('demo.html')


if __name__ == '__main__':
    app.run(debug=True)
