#coding=utf-8
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets, svm
from sklearn.cross_validation import train_test_split
data=np.loadtxt("D:\\Kettle\\BD_SOURCE_FILE\\test1.txt",delimiter=",",dtype=str)
#data=np.loadtxt("D:\\Kettle\\BD_SOURCE_FILE\\1.txt",delimiter=",",dtype=float)
iris = datasets.load_iris()
X =data[:100000,0:4]
y =data[:100000,5:]

# 0.94924
X_train,X_test,y_train,y_test =  train_test_split(X, y, test_size =0.2,random_state=2)


# fit the model
clf =DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)
rest=clf.predict(X_test )

cnt=len(y_train)
r1=[val for val in rest if val in y_test]
print  float(len(r1))/cnt

#     plt.figure(fig_num)
#     plt.clf()
#     plt.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired)
#
#     # Circle out the test data
#     plt.scatter(X_test[:, 0], X_test[:, 1], s=80, facecolors='none', zorder=10)
#
#     plt.axis('tight')
#     x_min = X[:, 0].min()
#     x_max = X[:, 0].max()
#     y_min = X[:, 1].min()
#     y_max = X[:, 1].max()
#
#     XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
#     Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
#
#     # Put the result into a color plot
#     Z = Z.reshape(XX.shape)
#     plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
#     plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
#                 levels=[-.5, 0, .5])
#
#     plt.title(kernel)
# plt.show()