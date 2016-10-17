#coding: utf-8
# 导入NumPy函数库，一般都是用这样的形式(包括别名np，几乎是约定俗成的)
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import matplotlib.pyplot as plot
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import math

arr=np.arange(0,60,10).reshape(6,1)+np.arange(6)


a='1000006680_1000006989_1000013330_1000000964_1000000967_1000001049_1000001054_1000001133_1000002067_1000003329_'
b=a.split('_')
n=b.index('1000006989')
for i in b:
    ind=b.index(i)
    if ((n-ind)!=0):
        print '1000006989'+' '+i+' '+str(ind-n)

