import backtrader as bt
import numpy as np

class HullMovingAverage(bt.Indicator):
    """
    Hull Moving Average (HMA) Indikator
    Reduziert Lag bei gleichzeitiger Glättung
    HMA = WMA(2*WMA(n/2) - WMA(n)), sqrt(n))
    """
    lines = ('hma',)
    params = (('period', 20),)
    
    def __init__(self):
        half_period = int(self.params.period / 2)
        sqrt_period = int(np.sqrt(self.params.period))
        
        wma1 = bt.indicators.WMA(self.data, period=half_period)
        wma2 = bt.indicators.WMA(self.data, period=self.params.period)
        
        self.lines.hma = bt.indicators.WMA(2.0 * wma1 - wma2, period=sqrt_period)
