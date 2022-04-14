from candlestick import candlestick


class analyzer():
    def __init__(self, df):
        self.df = df
        self._get_candlestick_direction()

    def get_mean_vol(self):
        return self.df['volume'].mean()

    def get_highest_vol(self):
        return self.df['volume'].max()

    def get_lowest_vol(self):
        return self.df['volume'].min()

    def _percentage(self, part, whole):
        return 100 * float(part) / float(whole)


    def _get_candlestick_direction(self):
        for index, row in self.df.iterrows():
            open = self.df.iloc[index]['open']
            close = self.df.iloc[index]['close']
            if open < close:
                self.df.loc[index, 'direction'] = 'upbar'
            elif open == close:
                self.df.loc[index, 'direction'] = 'nonebar'
            else:
                self.df.loc[index, 'direction'] = 'downbar'

    def _get_upbar_dataframe(self):
        df = self.df.loc[self.df['direction'] == 'upbar']
        return df

    def _get_downbar_dataframe(self):
        df = self.df.loc[self.df['direction'] == 'downbar']
        return df

