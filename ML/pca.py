#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from PIL import *
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

iris=datasets.load_iris()
x=iris.data[:,2]
y=iris.target
print y[1]


