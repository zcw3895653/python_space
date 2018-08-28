#coding=utf-8
import numpy as np



a=np.array([1,2,3,4,5])
b=np.array([4,5,6,7,8])
c=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,0]],dtype=np.string_).reshape(3,-1)

d=np.arange(1,13,1).reshape(3,-1)

persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S32','i', 'f']})
#print np.arange(1,60,10).reshape(-1,1)+np.arange(0,5,1)
#print np.linspace(0,1,12)
#print np.logspace(0,2,20)
#print np.fromstring("sabcdefg",dtype=np.int8)
np.random.seed(2)
r= np.random.rand(10)
#print r[r>0.4]
a=np.array([("zhang",32,12.2)],dtype=persontype)
b= np.arange(1,60,10).reshape(-1,1)+np.arange(0,5,1)
#print b[::2,::2]
c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.float32 )

#print c
x=np.linspace(0,2*np.pi,10)
y=np.sin(x)
#print x
x=np.arange(1,6).reshape(-1,1)
y=np.arange(12,16)
z=x+y

#print np.add.reduce(z,axis=1)
#print np.add.accumulate(z)
#print np.add.reduceat(x,indices=[0,1,0,2])
a=np.matrix([[1,2],[3,4]])
b=np.array([[1,2],[3,4]],dtype=np.float)
print a**-1
np.savetxt("D:\\zcw\\a.txt",a,fmt="%d",delimiter=",")
c=np.loadtxt("D:\\zcw\\a.txt",delimiter=",")
print c