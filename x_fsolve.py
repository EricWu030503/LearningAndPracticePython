from scipy.optimize import fsolve
import numpy as np
def f(t0kL):
    t0=t0kL[0]
    k=t0kL[1]
    L=t0kL[2]
    f1=0.5*(np.exp(k*t0)-np.exp(-1*k*(1/3-t0)))*L/((1+np.exp(-1*k*(1/3-t0)))*(1+np.exp(k*t0)))-2
    f2=0.4*(np.exp(k*t0)-np.exp(-1*k*(1-t0)))*L/((1+np.exp(-1*k*(1-t0)))*(1+np.exp(k*t0)))-3
    f3=0.6*(np.exp(k*t0)-np.exp(-1*k*(2.5-t0)))*L/((1+np.exp(-1*k*(2.5-t0)))*(1+np.exp(k*t0)))-3.5
    return np.array([f1,f2,f3])
f0=np.array([2,2,2])
print(fsolve(f,f0))
