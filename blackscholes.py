#implementing the black scholes in python

import numpy as np

from scipy import stats





r = 0.01

S = 30
K = 40
T = 240/365
sigma  = 0.30

def blackScholes(r,S,K,T,sigma,type="call"):
    "Calculate BlackScholes for Option Pricing"
    d1 = (np.log(S/K)+ (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = (np.log(S/K)+ (r - (sigma**2)/2)*T)/(sigma*np.sqrt(T))
    if type == "call":
            price = S*stats.norm.cdf(d1,0,1) - K*np.exp(-r*T)*stats.norm.cdf(d2,0,1)
    elif type == "put":
            price = K*np.exp(-r*T)*stats.norm.cdf(-d2,0,1) - S*stats.norm.cdf(-d1,0,1)
    return price
        



print("Option price is:",round(blackScholes(0.01,30,40,0.5,0.3,"call"),2))
