#coding=utf-8
from scipy import linalg
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
arr=np.array([[1,2],[3,4]])

tm=misc.imread('D:\\zcw\\test.jpg')
print linalg.inv(arr)
print  np.ones((2,2))
# print plt.imread('D:\\zcw\\test.jpg')


