import matplotlib.pylab as plt
import numpy as np
from sklearn.metrics import mean_squared_error
import scipy.optimize as opt

def f(a,x,b):
    return a*x+b
x=np.array([1000.1, 999.4, 1000.1, 1000.0, 1000.0, 999.7, 999.8, 999.0, 999.8])
y=np.array([11, 11, 11, 11, 11, 11, 11, 11, 11])
x=list(dict.fromkeys(x))
y=y[0:x.__len__()]
print(x)
print(y)
# if x.__len__()==2:
#      y2=y[1]
#      y1=y[0]
#      x2=x[1]
#      x1=x[0]
#      a=(y2-y1)/(x2-x1)
#      b =(y1+y2-a*(x1+x2))/2
# else:
#      a = opt.curve_fit(f,x,y)[0][0]
#      b = opt.curve_fit(f,x,y)[0][1]
# print(a,b)