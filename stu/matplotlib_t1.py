#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10,0.1)
# y=np.sin(x)
y= np.logspace(1,10,90)
# plt.plot([1,2,3,4],[5,6,7,8])
# plt.plot(x,y,'ro')
# plt.ylabel('some numbers')
t = np.arange(0., 5., 0.2)
# line, =plt.plot(t, t, 'r--')
# plt.setp(animated=True)
# line.set_antialiased(False)
np.random.seed(19680801)
mu,sigma=100,30
x=mu+sigma*np.random.randn(10000)
n,bins,patches=plt.hist(x,50,normed=1,facecolor='g',alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()