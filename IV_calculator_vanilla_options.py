import numpy as np
from scipy.stats import norm
from math import *

print("Input the option type(Enter call or put): ")
option_type=input()
print("Input current asset price: ")
S=float(input())
print("Input strike price: ")
K=float(input())
print("Input time left to maturity(in years): ")
T=float(input())
print("Input interest rate(in %): ")
r=float(input())/100

sigma=0.2
d1=(np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
d2=d1-sigma*np.sqrt(T)
N=norm.cdf

if option_type=="call":
    print("Input the market price for call option: ")
    call=float(input())
    while abs(call - (S * N(d1) - N(d2) * K * np.exp(-r * T))) > 0.001:
        if call > S * N(d1) - N(d2) * K * np.exp(-r * T):
            if call > S * N(d1) - N(d2) * K * np.exp(-r * T)+1:
                sigma += 0.01
            else:
                sigma += 0.00001
        else:
            if call < S * N(d1) - N(d2) * K * np.exp(-r * T)-1:
                sigma -= 0.01
            else:
                sigma -= 0.00001
        d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
    print(f"implied volatility: {sigma * 100}%")

elif option_type=="put":
    print("Input the market price for put option: ")
    put = float(input())
    while abs(put - (S * N(d1) - N(d2) * K * np.exp(-r * T)-S+K*(e**(-r*T)))) > 0.001:
        if put > S * N(d1) - N(d2) * K * np.exp(-r * T)-S+K*(e**(-r*T)):
            if put>S * N(d1) - N(d2) * K * np.exp(-r * T)-S+K*(e**(-r*T))+1:
                sigma+=0.01
            else:
                sigma+=0.00001
        else:
            if put < S * N(d1) - N(d2) * K * np.exp(-r * T)-S+K*(e**(-r*T))-1:
                sigma-=0.01
            else:
                sigma -= 0.00001
        d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
    print(f"implied volatility: {sigma * 100}%")

else:
    print("Wrong option type")







