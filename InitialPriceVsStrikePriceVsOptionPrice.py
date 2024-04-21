from blackscholes import blackScholes

import numpy as np

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm
from math import log, sqrt, exp

K = 100  # Strike price
T = 1    # Time to maturity in years
r = 0.05 # Risk-free interest rate
q = 0.02 # Dividend yield

# Create a range for S and sigma
S_values = np.linspace(50, 150, 100)  # Stock price from $50 to $150
sigma_values = np.linspace(0.1, 0.5, 100)  # Volatility from 10% to 50%

# Generate grid of stock price and volatility
S_grid, sigma_grid = np.meshgrid(S_values, sigma_values)

# Calculate option prices for both call and put
call_prices = np.array([blackScholes(S, K, T, r, sigma, type="call") for S, sigma in zip(np.ravel(S_grid), np.ravel(sigma_grid))])
put_prices = np.array([blackScholes(S, K, T, r, sigma, type="put") for S, sigma in zip(np.ravel(S_grid), np.ravel(sigma_grid))])

# Reshape for 3D plotting
call_prices = call_prices.reshape(S_grid.shape)
put_prices = put_prices.reshape(S_grid.shape)

# Plotting
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Surface plot for call prices
call_surf = ax.plot_surface(S_grid, sigma_grid, call_prices, color='b', alpha=0.5, label='Call Option Price')
call_surf._facecolor2d = call_surf._facecolor3d  # Hack to show legend properly for 3D surface
call_surf._edgecolor2d = call_surf._edgecolor3d

# Surface plot for put prices
put_surf = ax.plot_surface(S_grid, sigma_grid, put_prices, color='r', alpha=0.5, label='Put Option Price')
put_surf._facecolor2d = put_surf._facecolor3d
put_surf._edgecolor2d = put_surf._edgecolor3d

# Labels and title
ax.set_xlabel('Stock Price')
ax.set_ylabel('Volatility')
ax.set_zlabel('Option Price')
ax.set_title('Black-Scholes Prices for Call and Put Options')
ax.legend()

plt.show()