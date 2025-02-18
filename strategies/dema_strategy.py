import backtrader as bt

class DEMAStrategy(bt.Strategy):
    params = (
        ('period', 14),
    )

    def __init__(self):
        self.dema = bt.indicators.DoubleExponentialMovingAverage(
            self.data,
            period=self.params.period,
        )

    def next(self):
        if self.data.close[0] > self.dema[0]:
            self.buy()
        elif self.data.close[0] < self.dema[0]:
            self.sell()
