#reproduces the "stats" or "verbose" output from LINEST in Excel or Google Sheets

import numpy as np
import scipy.optimize as opt

def f(a,x,b):
    return a*x+b

x = [20.9, 248.1, 999.7, 999.9, 999.6, 393.7, 1000.0, 1000.3, 1000.1, 1000.2]
y = [1, 3, 9, 9, 9, 4, 9, 9, 9, 9]
n = len(y)
dofreedom = n-2

z, cov = np.polyfit(x,y,1,cov=True)
p = np.poly1d(z)
yp = p(x) #predicted y values based on fit
a = z[0]
b = z[1]

regression_ss = np.sum( (yp-np.mean(y))**2)
residual_ss = np.sum( (y-yp)**2 )
u_a = np.sqrt(residual_ss / (dofreedom * np.sum((x - np.mean(x)) ** 2)))
u_b = u_a*np.sqrt(np.sum(np.power(x,2))/n)

print (f'a:{a},    b:{b},     u_a:{u_a},      u_b:{u_b}')

for i in range(0,2):
    print(i)
#a1=opt.curve_fit(f,x,y)[0][0]
#print(a1)

