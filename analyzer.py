from candlestick import candlestick


class analyzer():
    def __init__(self, candlestick_data, num_of_candlesticks=30):
        self.candlestick_data = candlestick_data
        self.num_of_candlesticks = num_of_candlesticks
        self._create_candlesticks_list(candlestick_data[:num_of_candlesticks])

    def _create_candlesticks_list(self, candlestick_data):
        candlesticks_data = candlestick_data[:self.num_of_candlesticks]
        # Ignores last value which is irrelevant
        candlestick_list = [candlestick(*candle[:11]) for candle in candlesticks_data]
        return candlestick_list
