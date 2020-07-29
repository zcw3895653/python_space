import http.client
import json
# //http://www.weather.com.cn/data/sk/101020100.html
# --{"weatherinfo":{"city":"上海","cityid":"101020100","temp":"23.5","WD":"东北风","WS":"小于3级","SD":"80%","AP":"1006.4hPa","njd":"2903","WSE":"<3","time":"17:00","sm":"1.1","isRadar":"1","Radar":"JC_RADAR_AZ9210_JB"}}
import requests
from application.logger import get_middleware_logger

LOGGER = get_middleware_logger('weather_http')
myheaders = {'Content-type': 'application/json',"content":"text/html; charset=UTF-8"}
def post_api(inputdata, url):
    """
    :param inputdata: 单个样本的输入参数，是json格式的数据
    :return: 单个样本的探真查询变量结果数据
    """
    # 调用接口
    connection = http.client.HTTPConnection(url)
    json_foo = json.dumps(inputdata)
    connection.request('POST', '/data/sk/101020100.html', json_foo, myheaders)
    response = connection.getresponse()
    res = json.loads(response.read().decode())
    # 接口有正确的数据才读入，否则为空
    if res['code'] == '0000':
        res_data = json.loads(res['data'])
    else:
        res_data = {}
    return res_data

def get_api(url):
    """
    :param inputdata: 单个样本的输入参数，是json格式的数据
    :return: 单个样本的探真查询变量结果数据
    """
    # 调用接口
    response = requests.get(url=url, headers=myheaders)
    response.encoding = "UTF-8"
    LOGGER.info(response.json()['weatherinfo'])
    res = response.json()
    # 接口有正确的数据才读入，否则为空
    return res

if __name__ == '__main__':
    FORMAT = "%(asctime)s %(thread)d %(message)s"
    res=get_api('http://www.weather.com.cn/data/sk/101020100.html')
    print(res)
