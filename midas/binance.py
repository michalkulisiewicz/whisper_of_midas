from binance import Client
from credentials import Credentials
import pandas as pd


class Binance:
    def __init__(self):
        self.binance_credentials = self._get_binance_credentials()
        self.client = self._get_binance_client()

    def _get_binance_credentials(self):
        credentials = Credentials()
        return credentials.get_binance_credentials()

    def _get_binance_client(self):
        client = Client(self.binance_credentials['api_key'], self.binance_credentials['api_secret'])
        return client

    def get_candlestick_data(self, symbol, interval, time_frame):
        candlestick_data = self.client.get_historical_klines(symbol, interval, time_frame)
        candlestick_data = self._parse_dataframe(candlestick_data)
        return candlestick_data

    def _parse_dataframe(self, candlestick_data):
        df = self._parse_data_from_binance_to_data_frame(candlestick_data)
        df = self._drop_unnecessary_columns(df)
        df = self._convert_unix_timestamp(df)
        df = self._convert_col_to_float(df)
        df = self._replace_dot_to_underscore(df)
        return df

    def _parse_data_from_binance_to_data_frame(self, candlestick_data):
        df = pd.DataFrame(candlestick_data, columns=['open_time', 'open', 'high', 'low', 'close',
                                                     'volume', 'close_time', 'quote_asset_volume',
                                                     'number_of_trades', 'taker_buy_base_asset_volume',
                                                     'taker_buy_quote_asset_volume', 'ignore'])
        return df

    def _drop_unnecessary_columns(self, df):
        df = df.drop(['quote_asset_volume', 'number_of_trades',
                      'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
                      'ignore'], axis=1)
        return df

    def _convert_unix_timestamp(self, df):
        # Converts unix timestamp to date_time, this is temporary function
        # used only for readability during tests
        # TODO Delete on production
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        return df

    def _convert_col_to_float(self, df):
        df = df.astype({'open': 'float64', 'high': 'float64', 'low': 'float64',
                        'close': 'float64', 'volume': 'float64'})
        return df

    def _replace_dot_to_underscore(self, df):
        # Replaces dot with underscore in all columns name for easier processing with python
        df.columns = [x.strip().replace('.', '_') for x in df.columns]
        return df

