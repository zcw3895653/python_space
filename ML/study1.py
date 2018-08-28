# -*- coding:utf-8 -*-
import xlrd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


path = './4.iris.data'

def iris_type(s):
    it={'Iris-setosa':0,'Iris-versicolor':1, 'Iris-virginica': 2}
    return it[s]



data=np.loadtxt(path,dtype=float,delimiter=',',converters={4:iris_type})
x,y=np.split(data,(4,),axis=1)
x=x[:,:2]


logs=LogisticRegression()
logs.fit(x,y.ravel())
N, M = 500, 500
x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
t1 = np.linspace(x1_min, x1_max, N)
t2 = np.linspace(x2_min, x2_max, M)
x1, x2 = np.meshgrid(t1, t2)  # 生成网格采样点
x_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

y_hat = logs.predict(x_test)  # 预测值
y_hat = y_hat.reshape(x1.shape)  # 使之与输入的形状相同
plt.pcolormesh(x1, x2, y_hat, cmap=plt.cm.Spectral, alpha=0.1)
plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', cmap=plt.cm.prism)  # 样本的显示
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.grid()
plt.show()

# 训练集上的预测结果
y_hat = dt_clf.predict(x)
y = y.reshape(-1)  # 此转置仅仅为了print时能够集中显示
print y_hat.shape  # 不妨显示下y_hat的形状
print y.shape
result = (y_hat == y)  # True则预测正确，False则预测错误
print y_hat
print y
print result
c = np.count_nonzero(result)  # 统计预测正确的个数
print c
print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))
