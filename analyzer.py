from candlestick import candlestick


class analyzer():
    def __init__(self, df):
        self.df = df
        self.get_candlestick_direction(df)

    def get_mean_vol(self):
        return self.df['volume'].mean()

    def get_highest_vol(self):
        return self.df['volume'].max()

    def get_lowest_vol(self):
        return self.df['volume'].min()

    def _percentage(self, part, whole):
        return 100 * float(part) / float(whole)

