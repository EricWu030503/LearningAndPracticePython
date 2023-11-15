import numpy as np
from math import *

print("Input the option type(Enter call or put): ")
option_type=input()
print("Input the current stock price: ")
stock_price=float(input())
print("Input the strike price: ")
strike=float(input())
print("Input the barrier price: ")
barrier=float((input()))
print("Input the time left to maturity: ")
dt=float(input())
print("Input the volatility(in %): ")
volatility=float(input())/100
print("Input the interest rate(in %): ")
interest_rate=float(input())/100
print("Input the observation frequencies before maturity(assuming constant interval between each observation time)")
observation_frequency=int(input())
print("Input the trials: ")
trials=int(input())

gains=[]
df = e**(-interest_rate*dt)

if option_type == "call":
    for i in range(trials):
        current_stock_price=stock_price
        barrier_breached=False
        for j in range(0, observation_frequency):
            next_stock_price = current_stock_price*pow(e, (interest_rate-(volatility**2)/2)*(dt/observation_frequency)+volatility*np.random.normal(0, sqrt(dt/observation_frequency)))
            if next_stock_price >= barrier:
                barrier_breached = True
            current_stock_price = next_stock_price
        if barrier_breached:
            gain = max(0, current_stock_price-strike)
        else:
            gain = 0
        gains.append(gain)
    MC_price = df * sum(gains) / trials
    print(f"The Monte Carlo Simulation Price for the given Bermudan barrier call option is: {MC_price}")

elif option_type == "put":
    for i in range(trials):
        current_stock_price=stock_price
        barrier_breached=False
        for j in range(0, observation_frequency):
            next_stock_price = current_stock_price*pow(e, (interest_rate-(volatility**2)/2)*(dt/observation_frequency)+volatility*np.random.normal(0, sqrt(dt/observation_frequency)))
            if next_stock_price <= barrier:
                barrier_breached = True
            current_stock_price = next_stock_price
        if barrier_breached:
            gain = max(0, strike-current_stock_price)
        else:
            gain = 0
        gains.append(gain)
    MC_price = df * sum(gains) / trials
    print(f"The Monte Carlo Simulation Price for the given Bermudan barrier put option is: {MC_price}")

else:
    print("wrong option type")



