from credentials import Credentials
from binance import Client
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from analyzer import analyzer

def get_binance_client():
    client = Client(binance_credentials['api_key'], binance_credentials['api_secret'])
    return client

def get_candlestick_data(symbol, interval, time_frame):
    candlestick_data = client.get_historical_klines(symbol, interval, time_frame)
    return candlestick_data

def parse_data_from_binance_to_data_frame(candlestick_data):
    df = pd.DataFrame(candlestick_data, columns = ['open_time', 'open', 'high', 'low', 'close',
                                                   'volume', 'close_time', 'quote_asset_volume',
                                                   'number_of_trades', 'taker_buy_base_asset_volume',
                                                   'taker_buy_quote_asset_volume', 'ignore'])
    return df

def drop_ignore_column(df):
    df = df.drop('ignore', 1)
    return df


def convert_unix_timestamp(df):
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    return df

def create_candlestick_chart(df):
    # # Create subplots and mention plot grid size

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'),
                        row_width=[0.2, 0.7])

    # Plot OHLC on 1st row
    fig.add_trace(go.Candlestick(x=df['Close.time'], open=df['Open'], high=df['High'],
                                 low=df['Low'], close=df['Close'], name='OHLC'),
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
    candlestick_data = get_candlestick_data('BTCUSDT','1m', '1 day ago UTC')
    candlestick_data = candlestick_data[:50]
    df = parse_data_from_binance_to_data_frame(candlestick_data)
    df = drop_ignore_column(df)
    df = convert_unix_timestamp(df)
    df['volume'] = pd.to_numeric(df['volume'], downcast="float")
    df.columns = [x.strip().replace('.', '_') for x in df.columns]
    print(len(df.index))
    analyzer = analyzer(df)




    # fig = create_candlestick_chart(df)
    # fig.show()

    # print(df['Volume'].dtype)
    # ret = analyzyer.calc_mean_vol()
    # print(ret)
