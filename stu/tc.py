#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data
import pandas as pd

s=pd.Series([1,2,3,4,5,np.nan,6,8])

dates=pd.date_range('20180101',periods=6)
start= datetime(2018,1,1)
end= datetime.now()

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('abcd'))
# df=data.DataReader('TSLA', 'yahoo', start, end)
#
print df