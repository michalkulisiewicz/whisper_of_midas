class Connector:
    """
            This class is used for possessing data from various of official market platforms such as:
            crypto exchanges, MetaTrader 5, IC Markets official broker exchange.
        Parameters:
            market (str): Desired marketplace that will be used for further processing.
                          Currently, scanner supports official binance exchange API
                          documentation available at: https://python-binance.readthedocs.io/en/latest/
    """

    def __init__(self, market: str):
        self.market = market
