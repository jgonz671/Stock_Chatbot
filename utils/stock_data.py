import os
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def fetch_stock_data(symbol):
    """
    Fetches stock data for the given symbol using Alpha Vantage.
    """
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
    return data
