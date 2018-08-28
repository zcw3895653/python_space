#coding=utf-8
import numpy as np

import matplotlib.pyplot as plt
plt.figure(1)
plt.figure(2)
plt.rcParams['font.sans-serif']=['FangSong']
plt.rcParams['axes.unicode_minus']=False
ax1=plt.subplot(211)
ax2=plt.subplot(212)
x=np.linspace(0,3,100)
for i in xrange(5):
    plt.figure(1)
    plt.title(u"性别分析1")
    plt.plot(x,np.exp(i*x/3))
    plt.sca(ax1)
    plt.plot(x,np.sin(i*x))
    plt.title(u"性别分析2")
    plt.sca(ax2)
    plt.plot(x,np.cos(i*x))

    plt.xlabel(u"行不")
    plt.ylabel(u"年龄")
    plt.xticks((0,1),(u'男',u'女'))
    plt.title(u"性别分析2")
    plt.legend(u"图例")

plt.show()
# for idx,color in enumerate("rgbyk"):
#      plt.subplot(321+idx,axisbg=color)
#      print idx,color
# plt.show()
#
#
# for i in 'sddfsddf':
#     print i

X1 = range(0, 50)
Y1 = [num**2 for num in X1] # y = x^2
X2 = [0, 1]
Y2 = [0, 1]  # y = x
Fig = plt.figure(figsize=(8,4))                      # Create a `figure' instance
Ax = Fig.add_subplot(111)               # Create a `axes' instance in the figure
Ax.plot(X1, Y1, X2, Y2)                 # Create a Line2D instance in the axes
Fig.show()
# Fig.savefig("test.pdf")