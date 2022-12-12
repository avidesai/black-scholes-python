# Implementing the black-scholes formula in python

import numpy as np
from scipy.stats import norm

# Define variables
# r = risk free interest rate
r = 0.01
# S = underlying share price
S = 30
# K = strike price of contract
K = 40
# T = time till expiration / total life of contract
T = 240/365
# sigma = volatility
sigma = 0.30

def black_scholes(r, S, K, T, sigma, type = "C"):
    #Calculate the black-scholes options price for a call/put
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm all of the option parameters above!")

print("Theoretical option price is: ", round(black_scholes(r, S, K, T, sigma, type="C"), 2))