#!/usr/bin/python

from main import _get_cfg_json,_DEV_CONFIG_PATH,_PROD_CONFIG_PATH,_CONFIG_ROOT
import MySQLdb
from application import   config


# # mysql数据库url
# SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
#     config.get('MYSQL_USER'),
#     config.get('MYSQL_PASSWORD'),
#     config.get('MYSQL_SERVER'),
#     config.get('MYSQL_PORT'),
#     config.get('MYSQL_DB_NAME')
# )

# DB_USER:str=_CONFIG[_DB_KEY]['DB_USER']
# DB_PASSWORD:str=_CONFIG[_DB_KEY]['DB_PASSWORD']
# DB_SERVER:str=_CONFIG[_DB_KEY]['DB_SERVER']
# DB_PORT:str=_CONFIG[_DB_KEY]['DB_PORT']
# DB_NAME:str=_CONFIG[_DB_KEY]['DB_NAME']

DB_USER:str="mysql"
DB_PASSWORD:str="mysql"
DB_SERVER:str="localhost"
DB_PORT:str="3306"
DB_NAME:str="tianqi"
# 打开数据库连接
db = MySQLdb.connect(DB_SERVER, DB_USER, DB_PASSWORD, DB_NAME, charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)


def query(Sql):
    cursor.execute(Sql)
    return cursor.fetchone()


def insert(Sql):
    cursor.execute(Sql)
    db.commit()