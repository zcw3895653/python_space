#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import  LineCollection
from sklearn.linear_model import LinearRegression
from  sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
##保序回归
n=100
x=np.arange(n)
rs=check_random_state(0)


y=rs.randint(-50,50,size=(n,))+50.*np.log(1+np.arange(n))
print rs.randint(-50,50,size=(n,))