import backtrader as bt

class ExponentialMovingAverage(bt.Indicator):
    """
    Exponential Moving Average (EMA) Indikator
    Gewichtet neuere Daten stärker als ältere
    """
    lines = ('ema',)
    params = (('period', 20),)
    
    def __init__(self):
        self.lines.ema = bt.indicators.ExponentialMovingAverage(
            self.data, period=self.params.period)
