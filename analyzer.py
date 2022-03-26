class analyzer():
    def __init__(self, df, num_of_candlesticks=30):
        self.num_of_candlesticks = num_of_candlesticks
        self.df = df[:num_of_candlesticks]

    def get_mean_vol(self):
        return self.df['Volume'].mean()


