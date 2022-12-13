"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/17-10:11
   contents:
-------------------------------------------------
"""
"""
flask框架介绍：该框架为后端服务框架，能够部署服务，这样我们的接口/代码就能够使用http协议来调用
"""
# 第一步：导包  pip install flask
import flask

# 第二步：创建app对象，把当前的python文件当成一个服务，__name__代表当前文件
app = flask.Flask(__name__)


# 第三步：发布服务,route是路由的意思
@app.route('/index', methods=['post', 'get'])
def index():
    return "高级班的第一个接口服务"


@app.route('/login', methods=['post', 'get'])
def login():
    return "高级班的第二个接口服务"


if __name__ == '__main__':
    # 0到65535 端口号的范围
    app.run(debug=True)  # 启动服务，使用debug调试模式启动服务，debug可调试模式,默认端口号为：5000
