#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.cross_validation import train_test_split
data=np.loadtxt("D:\\Kettle\\BD_SOURCE_FILE\\test1.txt",delimiter=",",dtype=str)
#data=np.loadtxt("D:\\Kettle\\BD_SOURCE_FILE\\1.txt",delimiter=",",dtype=float)
iris = datasets.load_iris()
X =data[:,0:4]
y =data[:,5:]


X_train,X_test,y_train,y_test =  train_test_split(X, y, test_size =0.5)


# fit the model
clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
clf.fit(X_train, y_train)
rest=clf.predict(X_test )

cnt=len(y_train)
right=0
for i,value in enumerate(rest):
    if (value==y_test[i]):
        right+=1
print  float(right)/cnt

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