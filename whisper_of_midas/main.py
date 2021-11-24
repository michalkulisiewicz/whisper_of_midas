from whisper_of_midas.credentials import Credentials
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_binance_client():
    client = Client(binance_credentials['api_key'], binance_credentials['api_secret'])
    return client

def get_candlestick_data(symbol, interval, time_frame):
    candlestick_data = client.get_historical_klines(symbol, interval, time_frame)
    return candlestick_data

def parse_data_from_binance_to_data_frame():
    df = pd.DataFrame(candlestick_data, columns = ['Open.time', 'Open', 'High', 'Low', 'Close',
                                                   'Volume', 'Close.time', 'Quote.asset.volume',
                                                   'Number of trades', 'Taker.buy.base.asset.volume',
                                                   'Taker.buy.quote.asset.volume', 'Ignore'])
    return df

if __name__ == '__main__':
    credentials = Credentials()
    binance_credentials = credentials.get_auth_tokens()
    client = get_binance_client()
    candlestick_data = get_candlestick_data("BTCUSDT",'1m', '1 day ago UTC')
    df = parse_data_from_binance_to_data_frame()
