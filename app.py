import streamlit as st
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Set up the page
st.set_page_config(page_title="Stock Analysis Chatbot", layout="wide")

# Alpha Vantage API Key
API_KEY = st.secrets["ALPHA_VANTAGE_API_KEY"]

# Function to fetch stock data
def fetch_stock_data(symbol):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
    return data

# Chatbot interface
st.title("Stock Analysis Chatbot")

symbol = st.text_input("Enter a stock symbol (e.g., TSLA, AAPL):")

if symbol:
    try:
        data = fetch_stock_data(symbol)
        st.write(f"Showing data for {symbol.upper()}:")
        st.write(data.head())

        # Plot closing prices
        st.line_chart(data['4. close'])
    except Exception as e:
        st.error(f"Error fetching data: {e}")
