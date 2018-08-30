#coding=utf-8
import pandas as pd
from impala.dbapi import connect
from impala.util import as_pandas

impala_saledetail_sql='''
select t.sale_day,t.store_code,name,t.telno,count(distinct seqno) from  tfdw.dwd_telno_detail t,tfdw.dwd_dim_cust t1,tfdw.dwd_dim_store t2
where t.telno=t1.usermobile and sale_day>='20160101' and t.store_code=t2.store_code
group by 1,2,3,4
'''