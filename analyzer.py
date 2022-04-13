from candlestick import candlestick
class analyzer():
    def __init__(self, candlestick_data, num_of_candlesticks=30):
        self.candlestick_data = candlestick_data
        self.num_of_candlesticks = num_of_candlesticks
        self._candlesticks(candlestick_data)

    def _candlesticks(self, candlestick_data):
        candlesticks_data = candlestick_data[:self.num_of_candlesticks]
        print(candlesticks_data)