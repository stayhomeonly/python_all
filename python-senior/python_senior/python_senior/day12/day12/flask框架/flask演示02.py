"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/17-10:11
   contents:
-------------------------------------------------
"""
from day12.数据库封装.DBUtils import DBUtils

"""
flask框架介绍：该框架为后端服务框架，能够部署服务，这样我们的接口/代码就能够使用http协议来调用
"""
# 第一步：导包  pip install flask
import flask, json

# 第二步：创建app对象，把当前的python文件当成一个服务，__name__代表当前文件
app = flask.Flask(__name__)


# 第三步：发布服务,route是路由的意思
@app.route('/user_login', methods=['post', 'get'])
def login():
    data = flask.request.values  # 接收请求发送过来的数据
    username = data["username"]  # 获取请求中的username
    passwd = data['passwd']  # 获取请求中的passwd
    if len(username) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(passwd) == 0:
        return json.dumps({"code": 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    else:
        db = DBUtils()
        count = db.find_count("select *from tb_user where name=%s and passwd=%s", (username, passwd))
        db.close()
        if count == 0 or count == -1:
            return json.dumps({"code": 1007, 'msg': '用户名或者密码错误'}, ensure_ascii=False)
        else:
            return json.dumps({"code": 1000, "msg": "登录成功"}, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
