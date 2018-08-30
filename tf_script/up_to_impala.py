#coding=utf-8
import pandas as pd
from impala.dbapi import connect
from impala.util import as_pandas
import impala
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url=r"D:\Kettle\BD_SOURCE_FILE\1234.xlsx"
columns=['store_code','name','open_time']
# columns2=['area','area1','store_code','name','addredd','contact','open_name','open_time','mark','old_net','now_net','wx','zhi','huishou','huchu','card_4g']

print url
file=pd.read_excel(url,sheetname=0,header=0,names=columns)
print file

file=file.fillna('')
conn = connect(host='139.224.41.235', port=21050,auth_mechanism='NOSASL')
cur = conn.cursor()
cur.execute("truncate table ods.sg_ntk_store")
print len(file)

for i in range(0,len(file)):
 # sql='''insert into  ods.sg_ntk_store(%s,%s,%s ) values ('%s','%s','%s'  )
 # '''% (columns[0],columns[1],columns[2],str(file[columns[0]].loc[i]).replace('.0',''),file[columns[1]].loc[i],file[columns[2]].loc[i])
       sql='''insert into  ods.sg_ntk_store(%s,%s,%s ) values ('%s','%s',' '  )
         '''% (columns[0],columns[1],columns[2],str(file[columns[0]].loc[i]).replace('.0',''),file[columns[1]].loc[i] )
       cur.execute(sql)
       print sql

conn.close()

# conn = connect(host='139.224.46.33', port=21050,auth_mechanism='NOSASL')
# cur = conn.cursor()
# file.to_sql(name='tmp', con=conn,if_exists='replace',flavor='hive',chunksize=10)
# cur.execute("SELECT * FROM tmp")
# print impala.util.as_pandas(cur)