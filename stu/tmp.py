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
test=pd.DataFrame({'A':[1,2,3,4,1,2,3,4],'B':[11,21,33,43,21,41,51,32]})

print(test.groupby('A')['B'].agg(lambda x:x.value_counts().index[1]))

