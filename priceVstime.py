from blackscholes import blackScholes

import numpy as np

import numpy as np
import matplotlib.pyplot as plt

r = 0.01       # Risk-free interest rate
S = 100        # Initial stock price
K = 100        # Strike price of the option
sigma = 0.2    # Volatility of the underlying asset


time_to_expiration = np.linspace(0.01, 2, 100)  # Avoid T=0 to prevent division by zero in the formula

# Calculate the option price for each time to expiration
call_prices = [blackScholes(r, S, K, T, sigma, 'call') for T in time_to_expiration]
put_prices = [blackScholes(r, S, K, T, sigma, 'put') for T in time_to_expiration]

# Plot the results
plt.figure(figsize=(10, 5))

plt.plot(time_to_expiration, call_prices, label='Call Option Price')
plt.plot(time_to_expiration, put_prices, label='Put Option Price')

plt.title('Option Price vs. Time to Expiration')
plt.xlabel('Time to Expiration (Years)')
plt.ylabel('Option Price')
plt.legend()
plt.grid(True)

plt.savefig('figurePriceVsTime.png')
plt.show()

