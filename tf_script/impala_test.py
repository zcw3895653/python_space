#coding=utf-8
from impala.dbapi import connect

import os
import pandas as pd
import sys
from string import Template
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
reload(sys)
sys.setdefaultencoding("utf-8")

impala_saledetail_sql='''
select productid,productbrand,productdetails from webmagicdb.wb_jd_product_details t where not exists (
select 1 from  webmagicdb.ods_wb_jd_product_details t1 where t.productid=t1.product_id and length(productdetails)>2
)
'''
# ip = '139.224.46.33'
ip='10.47.194.252'
impalaconn = connect(host=ip, port=21050, auth_mechanism='NOSASL',user='zhouchongwei')

cursor = impalaconn.cursor()
cursor.execute(impala_saledetail_sql)
row = cursor.fetchall()
print len(row)
for line in row:
    print line
    if(line[2]!=''):
        for st in line[2].lstrip('[').rstrip(']').split(','):
            if (st.find('：')>0):
                brad=line[1].replace(r"'",'-')
                key=st.split('：')[0].replace(r"'",'-')
                v=st.split('：')[1].replace(r"'",'-')
                sql='''insert into webmagicdb.ods_wb_jd_product_details values('%s','%s','%s','%s')'''%(line[0],brad,key,v)
                # print line[0],line[1],st.split('：')[0]," -> ",st.split('：')[1]
                print sql
                cursor.execute(sql)
cursor.close();