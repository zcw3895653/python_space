# #coding=utf-8
# import sys
# from  hive_service import ThriftHive
# from  hive_service.ttypes import HiveServerException
# from  thrift import Thrift
# from  thrift.transport import TSocket
# from  thrift.transport import TTransport
# from  thrift.protocol import TBinaryProtocol
#
#
# def hiveExe(sql):
#     try:
#         transport = TSocket.TSocket('139.224.46.33', 10000)
#         transport = TTransport.TBufferedTransport(transport)
#         protocol = TBinaryProtocol.TBinaryProtocol(transport)
#         client = ThriftHive.Client(protocol)
#         transport.open()
#
#         client.execute(sql)
#
#         print "The return value is : "
#         print client.fetchAll()
#         print "............"
#         transport.close()
#     except Thrift.TException, tx:
#         print '%s' % (tx.message)
#
#
# if __name__ == '__main__':
#     hiveExe("show tables")

import pyhs2

with pyhs2.connect(host='139.224.46.33',
                   port=10000,
                    authMechanism='PLAIN',
                   user='hdfs',
                   password='hdfs',
                   database='webmagicdb') as conn:
    with conn.cursor() as cur:
        #Show databases
        print cur.getDatabases()

        #Execute query
        cur.execute("select * from d_hot_search limit 10;")

        #Return column info from query
        print cur.getSchema()

        #Fetch table results
        for i in cur.fetch():
            print i