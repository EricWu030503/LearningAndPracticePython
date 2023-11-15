import numpy as np
from math import *

print("Input the option type(Enter call or put): ")
option_type=input()
print("Input the current stock price: ")
current_stock_price=float(input())
print("Input the strike price: ")
strike=float(input())
print("Input the barrier price: ")
barrier=float((input()))
print("Input the time left to maturity(in years): ")
dt=float(input())
print("Input the volatility(in %): ")
volatility=float(input())/100
print("Input the interest rate(in %): ")
interest_rate=float(input())/100
print("Input the trials: ")
trials=int(input())

gains=[]
df=e**(-interest_rate*dt)

if option_type == "call":
    for i in range(trials):
        stock_price_at_maturity=current_stock_price*pow(e,(interest_rate-(volatility**2)/2)*dt+volatility*np.random.normal(0,sqrt(dt)))
        if stock_price_at_maturity >= barrier:
            gain=max(0,stock_price_at_maturity-strike)
        else:
            gain=0
        gains.append(gain)
    MC_price = df*sum(gains) / trials
    print(f"The Monte Carlo Simulation Price for the given barrier call option is: {MC_price}")

elif option_type == "put":
    for i in range(trials):
        stock_price_at_maturity=current_stock_price*pow(e,(interest_rate-(volatility**2)/2)*dt+volatility*np.random.normal(0,sqrt(dt)))
        if stock_price_at_maturity<=barrier:
            gain=max(0,strike-stock_price_at_maturity)
        else:
            gain=0
        gains.append(gain)
    MC_price = df*sum(gains) / trials
    print(f"The Monte Carlo Simulation Price for the given barrier put option is: {MC_price}")

else:
    print("wrong option type")


