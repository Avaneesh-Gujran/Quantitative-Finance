from blackscholes import blackScholes

import numpy as np

import numpy as np
import matplotlib.pyplot as plt

S = 100      # Current stock price
K = 100      # Option strike price
T = 1        # Time to maturity in years
sigma = 0.2  # Volatility

# Varying interest rates
interest_rates = np.linspace(0, 0.1, 100)  # Interest rates from 0% to 10%
prices = [blackScholes(S, K, T, r, sigma) for r in interest_rates]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(interest_rates, prices, label='Option Price')
plt.title('Option Price vs Interest Rate')
plt.xlabel('Interest Rate')
plt.ylabel('Option Price')
plt.legend()
plt.grid(True)

plt.savefig('figureInterestRatevsTime.png')
plt.show()