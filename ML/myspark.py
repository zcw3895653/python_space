# #coding=utf-8
from pyspark import SparkConf,SparkContext
import os
print os.getenv("SPARK_HOME")

conf = SparkConf().setMaster('local')
sc = SparkContext(conf=conf)
 # sc = SparkContext(conf=conf)
# file=sc.textFile("D:/apps/data/movies.dat")
#
arr=[1,2,3,4,5]
data=sc.parallelize(arr)
print arr
print data

print "successful!"


