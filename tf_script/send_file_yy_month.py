#coding=utf-8
import MySQLdb
import pandas as pd
import time
import datetime
import xlutils
import os
from xlrd import open_workbook
from xlutils.copy import copy
from string import Template
import sys
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from impala.dbapi import connect
from tempfile import NamedTemporaryFile
import sys

reload(sys)
sys.setdefaultencoding('utf8')
path="/aliyun/home/etl/workspace/datafile"
ip='10.47.194.252'
# path="D:/Kettle/BD_SOURCE_FILE"
# ip='139.224.46.33'
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=7)
print yesterday

sql1='''
 with store as (
 select distinct store_code,dw_date from tfdw.dwd_dim_date ,tfdw.dwd_dim_store
 where substr(dw_date,1,6)=from_timestamp(date_add(current_timestamp(),interval -1 month),'yyyyMM') and  is_pos=1
 )select * from store t where not exists(
  select 1 from tfdw.dwd_whole_sale_detail t1 where substring(sale_day,1,7)=from_timestamp(date_add(current_timestamp(),interval -1 month),'yyyy-MM')
 and t.store_code=t1.store_code and t.dw_date=regexp_replace(t1.sale_day,'-','')
 )
'''
sql2='''
  select t.sale_day,store_code,store_name,telno,count(distinct seqno) nums from  tfdw.dwd_whole_sale_detail t,tfdw.dwd_dim_cust t1
 where t.telno=t1.usermobile and
 substr(sale_day,1,7)=from_timestamp(date_add(current_timestamp(),interval -1 month),'yyyy-MM')
 group by  t.sale_day,store_code,store_name,telno
'''
sql3='''
 with detail as (
select store_code,seqno ,sum(disamt) disamt from  tfdw.dwd_yy_sale_detail_v
where gtype=1 and substr(saleday,1,7)=from_timestamp(date_add(current_timestamp(),interval -1 month),'yyyy-MM')
group by store_code,seqno
),pay as (
select store_code,seqno ,c_paymentnm,sum(n_paymoney)disamt  from  tfdw.dwd_yy_sale_pay_v
where c_paymentnm in ('微信','支付宝')  and  substr(sale_time,1,6)=from_timestamp(date_add(current_timestamp(),interval -1 month),'yyyyMM')
  and c_paymentsysid in('002','老POS平台')
group by store_code,seqno ,c_paymentnm
)
select t.store_code,c_paymentnm,sum(disamt) disamt from (
select t.store_code,t1.c_paymentnm,least(t.disamt,t1.disamt) as disamt from
detail t,pay t1
where t.store_code=t1.store_code
and t.seqno=t1.seqno
) t group by t.store_code,c_paymentnm
'''
sql4=''' select store_code,name,city,is_pos  from tfdw.dwd_dim_store t where zly='1' '''

sql5='''select  store_code,count(distinct saleday) days from  tfdw.dwd_yy_sale_detail_v
where substr(saleday,1,7)=from_timestamp(date_add(current_timestamp(),interval -1 month),'yyyy-MM')
and store_code is not null
group by store_code'''
impalaconn = connect(host='139.224.46.33', port=21050,auth_mechanism='NOSASL')

result={'无pos交易门店':sql1,'会员交易次数':sql2,'微信支付宝交易费率':sql3,'弄堂口门店':sql4,'门店交易天数':sql5}
# result={'弄堂口门店':sql4}
#定义结果文件

filename=path+'/运营月报'.decode("utf8")+time.strftime("%Y%m%d.xlsx")

rexcel = pd.ExcelWriter(filename)


for key in result:
    df=pd.read_sql(result[key],impalaconn )
    cols = df.columns
    ## 转换每一列的编码
    for e in cols:
        df[e] = df[e].map(lambda x: str(x).decode("utf8").encode("raw_unicode_escape").decode("raw_unicode_escape"))
        # 这里的 utf8 为 python 运行环境默认编码, 即 sys.getdefaultencoding()
        print e
    df.to_excel(rexcel, sheet_name=key.decode("utf8"),index=False,encoding='utf8',engine='io.excel.xlsx.writer')

rexcel.save()



def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# 输入Email地址和口令:
from_addr ='zhouchongwei@chinatopfine.com'
password = 'zcw389565301!'
# 输入SMTP服务器地址:
smtp_server = 'smtp.chinatopfine.com'
# 输入收件人地址:
to_addr = ['dingfangfang@chinatopfine.com','yuanlihua@chinatopfine.com']
#抄送
# CCADDR = ['wangyun@chinatopfine.com','huzhen@chinatopfine.com','aiwei@chinatopfine.com','zhouchongwei@chinatopfine.com']
CCADDR = ['zhouchongwei@chinatopfine.com']

#对信息串中的换行做下处理
message='app每日数据：\n\t\t请查收'
#

msg = MIMEMultipart()
puretext = MIMEText(message, 'plain', 'utf-8')
msg.attach(puretext)

#配置邮件内容
msg['From'] = _format_addr(u'app每日数据<%s>' % from_addr)
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['To'] = ', '.join(to_addr)
msg['Cc'] = ', '.join(CCADDR)
msg['Subject'] = Header(u'app每日数据……', 'utf-8').encode()
#添加附件
# 首先是xlsx类型的附件
xlsxpart = MIMEApplication(open(filename, 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='每日数据.xlsx')
msg.attach(xlsxpart)

server = smtplib.SMTP(smtp_server,587) # SMTP协议默认端口是25
server.ehlo()
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, to_addr+CCADDR, msg.as_string())
server.quit()