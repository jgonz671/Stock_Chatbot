import streamlit as st
from utils.stock_data import fetch_stock_data

def dashboard_page():
    st.header("Stock Analysis Dashboard")
    st.write("Analyze stock trends and metrics with interactive charts.")

    # Initialize session state for the input field
    if "stock_symbol" not in st.session_state:
        st.session_state.stock_symbol = ""  # Initial empty state for the input field

    # Input field for stock symbol
    stock_symbol = st.text_input(
        "Enter a stock symbol (e.g., TSLA, AAPL):",
        key="stock_symbol",
    )

    if stock_symbol:
        try:
            # Fetch stock data
            data = fetch_stock_data(stock_symbol)
            st.write(f"Showing data for {stock_symbol.upper()}:")
            st.write(data.head())

            # Plot closing prices
            st.line_chart(data['4. close'])

            # Clear the input field and trigger re-render
            st.session_state.stock_symbol = ""
            st.rerun()
        except Exception as e:
            st.error(f"Error fetching data for {stock_symbol.upper()}: {e}")