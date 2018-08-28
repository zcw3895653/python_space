#coding=utf-8
import numpy  as np
import numbers
import warnings
import matplotlib.pyplot as plt
message=''
for a in 'HIVE ETL REPROT:||||hive etl 调度成功的有:||#加载pos数据 is successes||#加载批发数据 is successes||#加载主数据 is successes||#加载老pos is successes||#加载app is successes||#加载zly is successes||#加载云pos is successes||#tfdw is successes||#报表 is successes||hive etl 调度失败的有:'.split("||"):
    message=message+'\n'+a
print message