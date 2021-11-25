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

def parse_data_from_binance_to_data_frame(candlestick_data):
    df = pd.DataFrame(candlestick_data, columns = ['Open.time', 'Open', 'High', 'Low', 'Close',
                                                   'Volume', 'Close.time', 'Quote.asset.volume',
                                                   'Number of trades', 'Taker.buy.base.asset.volume',
                                                   'Taker.buy.quote.asset.volume', 'Ignore'])
    return df

def convert_unix_timestamp(df):
    df['Close.time'] = pd.to_datetime(df['Close.time'], unit='ms')
    return df

def create_candlestick_chart():
    # # Create subplots and mention plot grid size

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'),
                        row_width=[0.2, 0.7])

    # Plot OHLC on 1st row
    fig.add_trace(go.Candlestick(x=df["Close.time"], open=df["Open"], high=df["High"],
                                 low=df["Low"], close=df["Close"], name="OHLC"),
                  row=1, col=1
                  )

    # Bar trace for volumes on 2nd row without legend
    fig.add_trace(go.Bar(x=df['Close.time'], y=df['Volume'].astype(float).round(12), showlegend=False), row=2, col=1)

    # Do not show OHLC's rangeslider plot
    fig.update(layout_xaxis_rangeslider_visible=False)
    return fig

if __name__ == '__main__':
    credentials = Credentials()
    binance_credentials = credentials.get_auth_tokens()
    client = get_binance_client()
    candlestick_data = get_candlestick_data("BTCUSDT",'1m', '1 day ago UTC')
    df = parse_data_from_binance_to_data_frame(candlestick_data)
    df = convert_unix_timestamp(df)

