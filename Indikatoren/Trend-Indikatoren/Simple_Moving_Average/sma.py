import backtrader as bt

class SimpleMovingAverage(bt.Indicator):
    """
    Simple Moving Average (SMA) Indikator
    Berechnet den einfachen Durchschnitt der letzten N Perioden
    """
    lines = ('sma',)
    params = (('period', 20),)
    
    def __init__(self):
        self.lines.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=self.params.period)
