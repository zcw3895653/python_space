import http.client
import json
import requests
import re
from application.logger import get_middleware_logger
import math
from database import database
import datetime  # datetime
import time

LOGGER = get_middleware_logger('jijin_http')
myheaders = {'Content-type': 'application/json',"content":"text/html; charset=UTF-8"}
url = "http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList['Gb3sH5uawH5WCUZ9']/NetValue_Service.getNetValueOpen?page=1&num=40&sort=nav_date&asc=0&ccode=&type2=2&type3="
size:int=40

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

def get_fund_history(fund_id):
    url = "http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList['Gb3sH5uawH5WCUZ9']/NetValue_Service.getNetValueOpen?page="+str(page)+"&num="+str(size)+"&sort=nav_date&asc=0&ccode=&type2=2&type3="
    print("获取page="+str(fund_id))
    print(url)
    response = requests.post(url,   headers = myheaders)
    print(response.text)
    response=re.findall(r"\((.+?)\);",response.text)
    data=response[0]
    print(data)
    res = json.loads(data)['data']
    return res

def get_page_finance(page):
    url = "http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList['Gb3sH5uawH5WCUZ9']/NetValue_Service.getNetValueOpen?page="+str(page)+"&num="+str(size)+"&sort=nav_date&asc=0&ccode=&type2=2&type3="
    print("获取page="+str(page))
    print(url)
    # json_foo = json.dumps(inputdata)
    response = requests.post(url,   headers = myheaders)
    print(response.text)
    response=re.findall(r"\((.+?)\);",response.text)
    data=response[0]
    print(data)
    res = json.loads(data)['data']
    return res


def update_fund_date_nav(fund_info):
    sql=" REPLACE  INTO `tianqi`.`fund_date_nav`(`fund_id`, `fund_name`, `per_nav`, `total_nav`, `yesterday_nav`, `nav_rate`, `nav_a`, `nav_date`, `fund_manager`, `fund_type`, `fund_total_num`) " \
        "VALUES ('%(fund_id)s','%(fund_name)s', '%(per_nav)s', '%(total_nav)s', '%(yesterday_nav)s', '%(nav_rate)s', '%(nav_a)s', '%(nav_date)s', '%(fund_manager)s', '%(fund_type)s', '%(fund_total_num)s');"\
        % {'fund_id':fund_info['fund_id'],'fund_name':fund_info['fund_name'],'per_nav':fund_info['per_nav'],'total_nav':fund_info['total_nav']
           ,'yesterday_nav':fund_info['yesterday_nav'],'nav_rate':fund_info['nav_rate'],'nav_a':fund_info['nav_a'],'nav_date':fund_info['nav_date']
           ,'fund_manager':fund_info['fund_manager'],'fund_type':fund_info['fund_type'],'fund_total_num':fund_info['fund_total_num']}
    print("更新：" +sql)
    database.insert(sql)

def update_fund_history_nav(fund_history_info):
    sql=" REPLACE  INTO `tianqi`.`fund_history_nav`(`fund_id`, `fund_date`, `fund_nav`, `fund_total_nav`) " \
        "VALUES ('%(fund_id)s','%(fund_date)s', '%(fund_nav)s', '%(fund_total_nav)s');"\
        % {'fund_id':fund_history_info['fund_id'],'fund_date':fund_history_info['fund_date'],'fund_nav':fund_history_info['fund_nav'],'fund_total_nav':fund_history_info['fund_total_nav']}
    print("更新：" +sql)
    database.insert(sql)



def get_all_finance():
    num=int(get_all_finance_num())
    pages=math.ceil(num/size)+1
    # pages=3
    fund_info={}


    time.sleep(5)
    for i in range(1,pages):
        res=get_page_finance(i)
        print(len(res))
        time.sleep(2)
        for x in res:
            print(x)
            time.sleep(1)
            fund_id=x['symbol']
            fund_info['fund_id']=fund_id
            fund_info['fund_name'] = x['sname']
            fund_info['per_nav'] = x['per_nav']
            fund_info['total_nav'] = x['total_nav']
            fund_info['yesterday_nav'] = x['yesterday_nav']
            fund_info['nav_rate'] = x['nav_rate']
            fund_info['nav_a'] = x['nav_a']
            fund_info['nav_date'] = x['nav_date']
            fund_info['fund_manager'] = x['fund_manager']
            fund_info['fund_type'] = x['jjlx']
            fund_info['fund_total_num'] = x['jjzfe']
            update_fund_date_nav(fund_info)
            get_fund_history(fund_id)
        print("=======")


t = datetime.date.today()
delat=datetime.timedelta(days=15)
format = "%Y-%m-%d"
dateto=t.strftime(format)
datefrom=(t-delat).strftime(format)
def get_finance_history_num(fund_id):
    url = "https://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?callback=jQuery1112006034245173649988_1597501048435&symbol="\
          +str(fund_id)+"&datefrom="+datefrom+"&dateto="+dateto+"&page=1&_=1597501048446"
    response = requests.post(url, headers = myheaders)
    print(response.text)
    response=re.findall(r"\((.+?)\)",response.text)
    print(response[0])
    res = json.loads(response[0])['result']['data']
    print(res)
    return res['total_num']

def get_finance_history_page(fund_id,page):
    url = "https://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?callback=jQuery1112006034245173649988_1597501048435&symbol="\
          +str(fund_id)+"&datefrom="+datefrom+"&dateto="+dateto+"&page="+str(page)+"&_=1597501048446"
    response = requests.post(url, headers = myheaders)
    print(response.text)
    response=re.findall(r"\((.+?)\)",response.text)
    print(response[0])
    res = json.loads(response[0])['result']['data']
    print(res)
    return res['data']
def get_fund_history(fund_id):
    histroy_size=21
    num=int(get_finance_history_num(fund_id))
    pages=math.ceil(num/histroy_size)+1
    fund_history_info={}
    for i in range(1,pages):
        res=get_finance_history_page(fund_id,i)
        print(len(res))
        for x in res:
            print(x)
            fund_history_info['fund_id']=fund_id
            fund_history_info['fund_date'] = x['fbrq']
            fund_history_info['fund_nav'] = x['jjjz']
            fund_history_info['fund_total_nav'] = x['ljjz']
            update_fund_history_nav(fund_history_info)
        print("=======")

def get_all_finance_num():

    inputdata={
        "page": 1,
        "num": 40,
        "sort": "nav_date",
        "asc": 0,
        "type2": 2,
    }
    json_foo = json.dumps(inputdata)
    response = requests.post(url, data =json_foo, headers = myheaders)
    print(response.text)
    response=re.findall(r"\((.+?)\);",response.text)
    print(response[0])
    res = json.loads(response[0])
    print(res['total_num'])
    return res['total_num']

if __name__ == '__main__':
    FORMAT = "%(asctime)s %(thread)d %(message)s"
    # print(get_fund_history("001113"))
    get_all_finance()
