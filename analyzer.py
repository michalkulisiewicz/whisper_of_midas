class analyzer():
    def __init__(self, data, num_of_candlesticks=30):
        self.num_of_candlesticks = num_of_candlesticks
        self.data = data[:num_of_candlesticks]

