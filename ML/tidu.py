
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5, 5, 0.001)
y=x**2
plt.plot(x,y)
plt.show()


old = 0
new= 2
step = 0.01
precision = 0.00001

def derivative(x):
    return 2*x

while abs(new - old) > precision:
    print new,step * derivative(new)
    old = new
    new = new - step * derivative(new)

print (new)