#coding=utf-8
import theano.tensor as T
import numpy
from theano import function
x=T.dscalar('x')
y=T.dscalar('y')
z=x+y
f=function([x,y],z)
print f(2,3)
