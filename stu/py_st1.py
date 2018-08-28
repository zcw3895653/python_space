#coding=utf-8
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
import ibm_db
import logging

conn = ibm_db.connect("DATABASE=zzdb;HOSTNAME=10.128.113.32;PORT=50000;PROTOCOL=TCPIP;UID=zzuser;PWD=zzuser;", "", "")
cursor = conn.cursor()
cursor.execute ("SELECT  1 ")
row=cursor.fetachall()
logging.info(row)
