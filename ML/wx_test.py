#coding=utf-8
import urllib
appid="wx16270cb3adb66b0f"
secret="cc7f5eb8314fc4d554a1c00ac3e6af24"
url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+appid+"&secret="+secret




rst=urllib.urlopen(url).read()
data={}
data=eval(rst)
# print data['access_token']
# print data

print(u'\u8fd9\u91cc\u53ef\u4ee5\u4e70\u70df\u5417')