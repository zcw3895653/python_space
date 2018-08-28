#coding=utf-8
import matplotlib.pyplot as plt
import  numpy as np
im = plt.imread("d:/zcw/test.jpg")
x=np.random.randn(100)
# plt.plot(x,[xi**2 for xi in x],'r--')
plt.grid(True)
# plt.axis([1,5,2,90])
plt.xlabel('this is x')
plt.ylabel('this is y')
# plt.plot([1,3,2,4],label='normal')
# plt.legend(loc='lower left')
plt.hist(x)
plt.show()

# print im
