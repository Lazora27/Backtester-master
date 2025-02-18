import backtrader as bt

class MovingAverage(bt.Indicator):
    """
    Einfacher Moving Average (MA) Indikator
    """
    lines = ('ma',)
    params = (('period', 20),)
    
    def __init__(self):
        self.lines.ma = bt.indicators.MovingAverageSimple(
            self.data, period=self.params.period)
