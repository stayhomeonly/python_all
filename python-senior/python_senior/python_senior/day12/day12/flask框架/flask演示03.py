"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/17-14:19
   contents:
-------------------------------------------------
"""
"""
注册接口：
1.只允许post请求
2.用户入参必须有用户名，密码，确认密码，且都不能为空
3.密码和确认密码必须保持一致
4.用户名和密码必须在6-18位之间
5.用户名、手机号、邮箱不能重复
6.手机号（11位纯数字）和邮箱格式是否正确（判断是否包含@、com、cn）
"""
import flask, json, re
from day12.数据库封装.DBUtils import DBUtils

app = flask.Flask(__name__)


# 注册接口
@app.route('/register', methods=['post'])
def register():
    data = flask.request.values  # 获取请求的值
    username = data['username']  # 接收传入的参数
    pwd = data['pwd']
    re_pwd = data['re_pwd']
    phone = data['phone']
    email = data['email']
    if len(username) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(pwd) == 0:
        return json.dumps({"code": 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    elif pwd != re_pwd:
        return json.dumps({"code": 1003, "msg": "两次密码输入不一致"}, ensure_ascii=False)
    elif len(phone) == 0:
        return json.dumps({"code": 1004, "msg": "手机号不能为空"}, ensure_ascii=False)
    elif len(email) == 0:
        return json.dumps({"code": 1005, "msg": "邮箱不能为空"}, ensure_ascii=False)
    elif not (6 <= len(username) <= 18 and 6 <= len(pwd) <= 18):
        return json.dumps({"code": 1006, "msg": "用户名和密码必须在6-18位之间"}, ensure_ascii=False)
    elif len(phone) != 11 or not phone.isnumeric():
        return json.dumps({"code": 1007, "msg": "手机号格式错误"}, ensure_ascii=False)
    # elif not ('@' in email and (('com' or 'cn') in email)):
    #     return json.dumps({"code": 1008, "msg": "邮箱格式错误"}, ensure_ascii=False)
    reg = re.compile((r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'))
    if not re.fullmatch(reg, email):
        return json.dumps({"code": 1008, "msg": "邮箱格式错误"}, ensure_ascii=False)
    else:
        db = DBUtils()
        count1 = db.find_count("select *from tb_user where name=%s", (username,))
        count2 = db.find_count("select *from tb_user where phone=%s", (phone,))
        count3 = db.find_count("select *from tb_user where email=%s", (email,))
        if count1 >= 1:
            db.close()
            return json.dumps({"code": 1009, "msg": "用户名不能重复！"}, ensure_ascii=False)
        elif count2 >= 1:
            db.close()
            return json.dumps({"code": 1010, "msg": "手机号不能重复！"}, ensure_ascii=False)
        elif count3 >= 1:
            db.close()
            return json.dumps({"code": 1011, "msg": "邮箱不能重复！"}, ensure_ascii=False)
        else:
            count = db.cud("insert into tb_user(name,passwd,phone,email) values(%s,%s,%s,%s)",
                           (username, pwd, phone, email))
            db.close()
            if count == 1:
                return json.dumps({"code": 1000, "msg": "注册成功"}, ensure_ascii=False)
            else:
                return json.dumps({"code": 9999, "msg": "注册失败"}, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
