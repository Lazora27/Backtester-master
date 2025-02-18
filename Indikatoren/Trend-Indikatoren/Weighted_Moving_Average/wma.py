import backtrader as bt

class WeightedMovingAverage(bt.Indicator):
    """
    Weighted Moving Average (WMA) Indikator
    Gewichtet die Werte linear, wobei neuere Werte stärker gewichtet werden
    """
    lines = ('wma',)
    params = (('period', 20),)
    
    def __init__(self):
        self.lines.wma = bt.indicators.WeightedMovingAverage(
            self.data, period=self.params.period)
