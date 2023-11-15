import numpy as np
from scipy.stats import norm

print("Input the option type(Enter call or put): ")
option_type=input()
print("Input current asset price: ")
S=float(input())
print("Input strike price: ")
K=float(input())
print("Input time left to maturity(in years): ")
T=float(input())
print("Payout at maturity: ")
payout=float(input())
print("Input interest rate(in %): ")
r=float(input())/100
print("Input volatility(in %): ")
sigma=float(input())/100

def black_scholes_digital_put(S, K, T, r, sigma, payout):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    N = norm.cdf
    put = np.exp(-r * T)*(1-N(d2))*payout
    return put

df=np.log(-r*T)
digital_put=black_scholes_digital_put(S,K,T,r,sigma,payout)
digital_call=df*payout-digital_put

if option_type == "call":
    print(f"Digital call option price: {digital_call}")
elif option_type == "put":
    print(f"Digital put option price: {digital_put}")
else:
    print("wrong option type")