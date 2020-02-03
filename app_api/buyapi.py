from flask import Flask
from flask import make_response, jsonify
app = Flask(__name__)

@app.route('/v1.0/tuijian/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/goods/')
def goods():
    # response = jsonify( code=200,
    #                    msg="success",
    #                    data={"goods":{"id":1,"name":"test1","price":"123","photo":"https://img-blog.csdnimg.cn/20191225111311593.png"}})
    response = jsonify( {"goods":[{"id":1,"name":"test1","price":"123","photo":"https://img-blog.csdnimg.cn/20191225111311593.png"}
                                  ,{"id":2,"name":"test2","price":"1223","photo":"https://img-blog.csdnimg.cn/20191225111311593.png"}]})
    return response
@app.route('/v1.0/homePage/', methods=['GET', 'POST'])
def homepage():
    """
     上面 /v1.0/homePage/ 定义的url最后带上"/"：
     1、如果接收到的请求url没有带"/"，则会自动补上，同时响应视图函数
     2、如果/v1.0/homePage/这条路由的结尾没有带"/"，则接收到的请求里也不能以"/"结尾，否则无法响应
    """
    response = jsonify(code=200,
                       msg="success",
                       data=[1,"123"])

    return response
    # 也可以使用 make_response 生成指定状态码的响应
    # return make_response(response, 200)

if __name__ == '__main__':
    # flask内部自带的web服务器，只可以在测试时使用
    # 应用启动后，在9001端口监听所有地址的请求，同时根据配置文件中的DEBUG字段，设置flask是否开启debug
    app.run(host='0.0.0.0', port=8081, debug=app.config['DEBUG'])