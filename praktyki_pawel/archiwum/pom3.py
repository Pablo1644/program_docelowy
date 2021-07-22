import numpy as np
from scipy.interpolate import interp1d
import scipy.optimize as opt
import matplotlib.pyplot as plt
def func(x,a,b):
    return a*x+b

x=[1,2,3,4,5,6,7,8,9]
y=[5,10,16,20,24.5,30,34,42,46]
Keyz=['Ola','Ola','Ola','Ola','Kasia','Kasia','Kasia','Kasia','Kasia']
arr=np.array(x)
arr2=np.array(y)

t=opt.curve_fit(func,arr,arr2)[0]
a=t[0]
b=t[1]
plt.plot(x,y,'o')
lin_arr=a*arr+b
plt.plot(x,lin_arr)
plt.show()