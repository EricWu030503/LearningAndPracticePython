import numpy as np

np.random.seed(42)

returns = np.random.normal(
    loc=0.0005,      # average daily return
    scale=0.02,      # daily volatility
    size=(252,5)
)

weights = np.array([0.2,0.25,0.15,0.3,0.1])

print(returns.shape)
print(f"Days: {returns.shape[0]}")
print(f"Stocks: {returns.shape[1]}")
print(" ")

print("Stock returns:")
for i in range(returns.shape[1]):
    print(f"Stock {i+1} return: {np.mean(returns, axis=0)[i]}")
print(" ")

print("Stock Volatility:")
for i in range(returns.shape[1]):
    print(f"Stock {i+1} volatility: {np.std(returns, axis=0)[i]}")
print(" ")

portfolio_return = returns @ weights.reshape(5,1)
print(f"portfolio return shape: {portfolio_return.shape}")
print(" ")

print("Portfolio performance metrics:")
r = (1+np.mean(portfolio_return))**252-1
v = np.std(portfolio_return)*np.sqrt(252)
print(f"annualized return: {r}")
print(f"annualized volatility: {v}")
print(f"sharpe: {r/v}")
print(" ")

print("Covariance matrix: ")
sigma = np.cov(returns.T)
print(sigma)
print(f"covariance matrix shape: {sigma.shape}")
print("")

print("Portfolio volatility(matrix algebra):")
portfolio_vol = weights.T@sigma@weights
print(portfolio_vol)
print(np.std(portfolio_return)**2)
print(" ")

print("Standardization: ")
standardized_return = ( returns - np.mean(returns, axis = 0 ) ) / np.std(returns, axis = 0)
print(f"mean of standardized stock returns: {np.mean(standardized_return, axis = 0)}")
print(f"volatility of standardized stock returns: {np.std(standardized_return, axis = 0)}")
print(' ')


