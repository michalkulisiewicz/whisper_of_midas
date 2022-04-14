from candlestick import candlestick


class analyzer():
    def __init__(self, df):
        self.df = df
        self._get_candlestick_direction(df)

    def get_mean_vol(self):
        return self.df['volume'].mean()

    def get_highest_vol(self):
        return self.df['volume'].max()

    def get_lowest_vol(self):
        return self.df['volume'].min()

    def _percentage(self, part, whole):
        return 100 * float(part) / float(whole)


    def _get_candlestick_direction(self, df):
        for index, row in df.iterrows():
            open = df.iloc[index]['open']
            close = df.iloc[index]['close']
            if open < close:
                df.loc[index, 'direction'] = 'upbar'
            elif open == close:
                df.loc[index, 'direction'] = 'nonebar'
            else:
                df.loc[index, 'direction'] = 'downbar'
        print(df.head())

