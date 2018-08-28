#coding=utf-8
import pandas as pd
import numpy as np
s=pd.Series([1,3,5,np.nan,6,8])
dates=pd.date_range('20130101',periods=6)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('abcd'))


# print df.T
# print df.describe()
# print df.sort_index(axis=0,ascending=True)
# ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
# ts.cumsum()
# ts.plot()
# plt.show()
#
# print df.sort_index(axis=0,ascending=False)
# print df.sort_values(by='a')
# print df.mean(0),df.mean(1)

# df=pd.DataFrame(np.random.randn(10,4))
print df.apply(np.cumsum)
# print df
# pieces = pd.DataFrame(np.random.rand(3,4))
# print pieces
# print df.concat(pieces)
left = pd.DataFrame({'key': ['foo', 'fo2','fo3'], 'lval': [1, 2,3]})
right = pd.DataFrame({'key': ['foo', 'fo2'], 'rval': [4, 5]})
print pd.merge(left,right, on='key',how='left')