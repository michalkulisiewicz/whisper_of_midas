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

def drop_unnecessary_columns(df):
    df = df.drop(['quote_asset_volume', 'number_of_trades',
                  'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
                  'ignore'], axis=1)
    return df


def convert_unix_timestamp(df):
    #Converts unix timestamp to date_time, this is temporary function
    #used only for readability during tests
    #TODO Delete on production

    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
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

def save_df_to_csv(df):
    df.to_csv('sample.csv')

def read_df_from_csv():
    return pd.read_csv('sample.csv')

def test(df):
    # Get a Series object containing the data type objects of each column of Dataframe.
    # Index of series is column name.
    dataTypeSeries = df.dtypes
    print(df)
    print('Data type of each column of Dataframe :')
    print(dataTypeSeries)

def convert_col_to_float(df):
    df = df.astype({'open': 'float64', 'high': 'float64', 'low': 'float64',
                    'close': 'float64', 'volume': 'float64'})
    return df

if __name__ == '__main__':
    credentials = Credentials()
    binance_credentials = credentials.get_auth_tokens()
    client = get_binance_client()
    candlestick_data = get_candlestick_data('BTCUSDT','1m', '1 day ago UTC')
    candlestick_data = candlestick_data[:50]
    df = parse_data_from_binance_to_data_frame(candlestick_data)
    df = drop_unnecessary_columns(df)
    df = convert_unix_timestamp(df)
    df.columns = [x.strip().replace('.', '_') for x in df.columns]
    df = convert_col_to_float(df)
    test(df)
    # analyzer = analyzer(df)




    # fig = create_candlestick_chart(df)
    # fig.show()

    # print(df['Volume'].dtype)
    # ret = analyzyer.calc_mean_vol()
    # print(ret)
