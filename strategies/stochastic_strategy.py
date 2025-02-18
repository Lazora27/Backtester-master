import backtrader as bt

class StochasticStrategy(bt.Strategy):
    params = (
        ('period', 14),
        ('period_dfast', 3),
        ('upperband', 80),
        ('lowerband', 20),
    )

    def __init__(self):
        self.stochastic = bt.indicators.Stochastic(
            self.data,
            period=self.params.period,
            period_dfast=self.params.period_dfast,
        )

    def next(self):
        if self.stochastic.percK[0] > self.params.upperband:
            self.sell()
        elif self.stochastic.percK[0] < self.params.lowerband:
            self.buy()
