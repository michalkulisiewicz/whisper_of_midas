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

    def _get_upper_wick_upbar_value(self, high, close):
        return high - close

    def _get_lower_wick_upbar_value(self, open, low):
        return open - low

    def _get_upper_wick_downbar_value(self, high, open):
        return high - open

    def _get_lower_wick_downbar_value(self, close, low):
        return close - low

    def _get_upbar_body_value(self, close, open):
        return close - open

    def _get_downbar_body_value(self, close, open):
        return open - close

    def _get_candlestick_direction(self):
        #TODO instead of only getting direction, get wicks aswell
        for index, row in self.df.iterrows():
            open = self.df.iloc[index]['open']
            close = self.df.iloc[index]['close']
            high = self.df.iloc[index]['open']
            low = self.df.iloc[index]['low']
            upbar_body_value = self._get_upbar_body_value(close, open)
            downbar_body_value = self._get_downbar_body_value(close, open)

            if open < close:
                self._set_candlestick_direction(index, 'upbar')
                upper_wick_value = self._get_upper_wick_upbar_value(high, close)
                lower_wick_value = self._get_lower_wick_upbar_value(open, low)

                self._set_candlestick_wick(index, 'upper_wick', upper_wick_value)
                self._set_candlestick_wick(index, 'lower_wick', lower_wick_value)
                self._set_candlestick_body(index, upbar_body_value)
                print('dupa')


            elif open == close:
                self.df.loc[index, 'direction'] = 'empty'
            else:
                self.df.loc[index, 'direction'] = 'downbar'

    def _get_upbar_dataframe(self):
        df = self.df.loc[self.df['direction'] == 'upbar']
        return df

    def _get_downbar_dataframe(self):
        df = self.df.loc[self.df['direction'] == 'downbar']
        return df

    def _get_upbar_volume(self, upbar_df):
        return upbar_df['volume'].sum()

    def _get_downbar_volume(self, downbar_df):
        return downbar_df['volume'].sum()
