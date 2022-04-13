class candlestick():
    def __init__(self, open_time, open, high, low, close, volume, close_time,
                 quote_asset_volume, number_of_trades, taker_buy_base_asset_volume, taker_buy_quote_asset_volume):
        '''At the moment fields are created based on data provided by binance api'''
        self.open_time = open_time
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = float(volume)
        self.close_time = close_time
        self.quote_asset_volume = float(quote_asset_volume)
        self.number_of_trades = number_of_trades
        self.taker_buy_base_asset_volume = float(taker_buy_base_asset_volume)
        self.taker_buy_quote_asset_volume = float(taker_buy_quote_asset_volume)