#coding=utf-8
import pandas as pd
import numpy as np
import os
from tqdm import tqdm
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn import metrics
import warnings
import matplotlib.pyplot as plt
import math

warnings.filterwarnings('ignore')
# data=[1,4,7,9,11,1,4,1,7,7,7,7,7,12]
# df=pd.DataFrame(data,columns=['v'])
# print(df)
# plt.plot(df['v'])
# plt.show()
# for x in range(10):
#     print(x)
#
# print(np.random.randint(123))
agg_dict={}
target='a'
ag='sdf'
test=pd.DataFrame({'Aa':[1,2,3,4,1,2,3,4],'B':[11,21,33,43,21,41,51,32]},index= [1,2,3,4,1,2,3,4])

print(test)
print(test.apply(lambda x:x['Aa']*math.cos(math.radians(x['B'])), axis=1))
print(2*math.cos(21))
print(math.cos(21))

df = pd.DataFrame(np.array([[1, 1], [1, 10], [1, 100], [4, 100]]),columns=['a', 'b'])
print(df.groupby('a')['b'].quantile(.1).reset_index() )
print(df.groupby('a')['b'].agg({"person":np.percentile(q=0.1,a=range(1,101))}).reset_index())
