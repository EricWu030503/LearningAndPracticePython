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
print("Input volatility(in %): ")
sigma=float(input())/100
is_call=True if option_type=="call" else False

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    N = norm.cdf
    call = S * N(d1) -  N(d2)* K * np.exp(-r * T)
    return call

call_option_price=black_scholes_call(S,K,T,r,sigma)
put_option_price=call_option_price-S+K*(e**(-r*T))
if is_call:
    print(f"call option price: {call_option_price}")
else:
    print(f"put option price: {put_option_price}")