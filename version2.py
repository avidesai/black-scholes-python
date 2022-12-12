# Implementing the black-scholes formula in python
# Creating a streamlit dashboard to input custom values

import numpy as np
import streamlit as st
from PIL import Image
from scipy.stats import norm

# Define variables
# r = risk free interest rate
r = st.sidebar.number_input('Risk free interest rate (in decimal)', min_value=None, max_value=None, value= 0.04)
# S = underlying share price
S = st.sidebar.number_input('Underlying share price', min_value=None, max_value=None, value= 30)
# K = strike price of contract
K = st.sidebar.number_input('Option strike price', min_value=None, max_value=None, value= 40)
# T = time till expiration / total life of contract
T = st.sidebar.number_input('Days to expiration', min_value=None, max_value=None, value= 240)
total = st.sidebar.number_input('Total contract length (days)', min_value=None, max_value=None, value= 365)
T = T/total
# sigma = volatility
sigma = st.sidebar.number_input('Volatility', min_value=None, max_value=None, value= 0.30)
# Call or put
type = st.sidebar.radio('Call (C) or Put (P)', ("C", "P"))

def black_scholes(r, S, K, T, sigma, type):
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


st.write("""
# Black-scholes options pricing dashboard
This is the formula used to calculate prices:
""")
image = Image.open('bsf.jpeg')
st.image(image, caption='Black-scholes formula', width=600)


st.write("Theoretical option price is: ", round(black_scholes(r, S, K, T, sigma, type="C"), 2))