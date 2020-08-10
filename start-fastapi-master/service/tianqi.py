from typing import Dict
from model.tianqi import Tianqi
from application.logger import get_service_logger
import time, pprint
from database import database
import datetime
from middleware import weather_http

LOGGER = get_service_logger('Tianqi')


def get_tianqi(cityid: str) -> Tianqi:
    day =datetime.datetime.now().strftime('%Y-%m-%d')
    key=day+"-"+cityid
    sql="select city,cityid,temp from tianqi where tianqi_id='%(name)s'" % {'name':key}
    res={}
    LOGGER.info("finding tian with key="+key)
    db_data=database.query(sql)
    if db_data!=None:
        res['city'] = db_data[0]
        res['cityid'] = db_data[1]
        res['temp'] = db_data[2]
        res['tianqi_id'] = key
    else:
        api_data = weather_http.get_api("http://www.weather.com.cn/data/sk/%s.html" % cityid)
        print(api_data)
        res['city'] = api_data['weatherinfo']['city']
        res['cityid'] = api_data['weatherinfo']['cityid']
        res['temp'] = api_data['weatherinfo']['temp']
        res['tianqi_id'] = key
        update_tianqi(res)
    print(res)
    return res

def update_tianqi(Tianqi):
    sql="insert into tianqi(tianqi_id,city,cityid,temp) values('%(tianqi_id)s','%(city)s','%(cityid)s','%(temp)s')" % {'tianqi_id':Tianqi['tianqi_id'],'city':Tianqi['city'],'cityid':Tianqi['cityid'],'temp':Tianqi['temp']}
    print("更新：" +sql)
    print("更新成功："+Tianqi['tianqi_id'])
    database.insert(sql)

if __name__ == '__main__':
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    cityid="101020100"

    res = get_tianqi(cityid)
    print(res)