#coding=utf-8
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

data=pd.read_csv("D:\\zcw\\text.csv\\part-00000",header=None );
#
# with  open("D:\\zcw\\text.csv\\tmp1.txt","w") as f:
#     for i  in range(0 , 3321):
#         sss=''
#         for j in data:
#
#             if (j==0):
#                 sss= str(data[j][i]) + " "
#             else:
#                 sss =sss+ str(j) + ":" + str(data[j][i]) + " "
#         f.write( sss)
#         f.write("\n")
train=data.iloc[:,1:]
target=data[0]
print train.shape
train_X,test_X, train_y, test_y = train_test_split(train,
                                                   target,
                                                   test_size = 0.2,
                                                   random_state = 0)
clf = SVC(decision_function_shape='ovo',C=10,kernel='rbf')
clf.fit(train_X,train_y)
pre_y=clf.predict(test_X)

print test_y[test_y==3].size
print  classification_report(test_y, pre_y)
print score(test_X, test_y, sample_weight=None)
