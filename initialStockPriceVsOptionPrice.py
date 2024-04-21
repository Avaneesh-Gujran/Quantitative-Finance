from blackscholes import blackScholes

import numpy as np

import numpy as np
import matplotlib.pyplot as plt

r = 0.01       # Risk-free interest rate
T = 1       # Initial stock price
K = 100        # Strike price of the option
sigma = 0.2    # Volatility of the underlying asset


initial_price = np.linspace(0.01, 100, 200)  # Avoid T=0 to prevent division by zero in the formula

# Calculate the option price for each time to expiration
call_prices = [blackScholes(r, S, K, T, sigma, 'call') for S in initial_price]
put_prices = [blackScholes(r, S, K, T, sigma, 'put') for S in initial_price]

# Plot the results
plt.figure(figsize=(10, 5))

plt.plot(initial_price, call_prices, label='Call Option Price')
plt.plot(initial_price, put_prices, label='Put Option Price')

plt.title('Option Price vs. Initial Stock Price')
plt.xlabel('Initial Stock Price')
plt.ylabel('Option Price')
plt.legend()
plt.grid(True)

plt.savefig('figureInitialPriceVsOptionPrice.png')
plt.show()
