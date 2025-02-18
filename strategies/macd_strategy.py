import backtrader as bt

class MACDStrategy(bt.Strategy):
    params = (
        ('me1_period', 12),
        ('me2_period', 26),
        ('signal_period', 9),
    )

    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data,
            me1_period=self.params.me1_period,
            me2_period=self.params.me2_period,
            signal_period=self.params.signal_period,
        )

    def next(self):
        if self.macd.macd[0] > self.macd.signal[0]:
            self.buy()
        elif self.macd.macd[0] < self.macd.signal[0]:
            self.sell()
