# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import hashlib
from  tyuling_replay import tyuling_replay
import time
import re
# import ReplayFromExcel
import xml.etree.ElementTree as ET


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# test.jindongyun.cn

@app.route("/wechat", methods=["GET","POST"])
def weixin():
    if request.method == "GET":     # 判断请求方式是GET请求
        my_signature = request.args.get('signature')     # 获取携带的signature参数
        my_timestamp = request.args.get('timestamp')     # 获取携带的timestamp参数
        my_nonce = request.args.get('nonce')        # 获取携带的nonce参数
        my_echostr = request.args.get('echostr')         # 获取携带的echostr参数
        # my_token = request.args.get('token')
        print(my_signature)
        print(my_timestamp)
        print(my_nonce)
        print(my_echostr)
        # print(my_token)
        token = 'sdfdfjosdfo123124123dfsdf'     # 一定要跟刚刚填写的token一致

        # 进行字典排序
        data = [token,my_timestamp ,my_nonce ]
        data.sort()
        # 拼接成字符串,进行hash加密时需为字符串
        data = ''.join(data)
        #创建一个hash对象
        s = hashlib.sha1()
        #对创建的hash对象更新需要加密的字符串
        s.update(data.encode("utf-8"))
        #加密处理
        mysignature = s.hexdigest()

        print("handle/GET func: mysignature, my_signature: ", mysignature, my_signature)

        # 加密后的字符串可与signature对比，标识该请求来源于微信
        if my_signature == mysignature:
            return my_echostr
        else:
            return ""
    else:
            # 解析xml
            xml = ET.fromstring(request.data)
            toUser = xml.find('ToUserName').text
            fromUser = xml.find('FromUserName').text
            msgType = xml.find("MsgType").text
            createTime = xml.find("CreateTime")
            # 判断类型并回复
            if msgType == "text":
                content = xml.find('Content').text
                #根据公众号粉丝的ID生成符合要求的图灵机器人userid
                if len(fromUser)>31:
                    tuling_userid = str(fromUser[0:30])
                else:
                    tuling_userid = str(fromUser)
                tuling_userid=re.sub(r'[^A-Za-z0-9]+', '', tuling_userid)
                #调用图灵机器人API返回图灵机器人返回的结果
                tuling_replay_text = tyuling_replay.get_message(content,tuling_userid)
                return reply_text(fromUser, toUser, tuling_replay_text)

            else:
                return reply_text(fromUser, toUser, "我只懂文字")

def reply_text(to_user, from_user, content):
    """
    以文本类型的方式回复请求
    """
    return """
    <xml>
        <ToUserName><![CDATA[{}]]></ToUserName>
        <FromUserName><![CDATA[{}]]></FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{}]]></Content>
    </xml>
    """.format(to_user, from_user, int(time.time() * 1000), content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8800)