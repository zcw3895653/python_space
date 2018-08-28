#coding=utf-8
from hdfs import *
client= Client("http://127.0.0.1:50070",root="/",timeout=100,session=False)