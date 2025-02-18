import backtrader as bt

class WilliamsR(bt.Indicator):
    """
    Williams %R
    
    Ähnlich wie der Stochastic Oscillator, aber mit invertierter Skala (-100 bis 0).
    Werte unter -80 deuten auf überverkaufte, Werte über -20 auf überkaufte 
    Bedingungen hin.
    
    Parameter:
    - period (14): Lookback-Periode für die Berechnung
    """
    
    lines = ('williams_r',)
    params = (('period', 14),)
    
    plotlines = dict(
        williams_r=dict(color='darkblue', _name='%R')
    )
    
    def __init__(self):
        # Höchster Hoch und niedrigster Tief über die Periode
        highest_high = bt.indicators.Highest(self.data.high, period=self.p.period)
        lowest_low = bt.indicators.Lowest(self.data.low, period=self.p.period)
        
        # Williams %R Berechnung
        # Formel: %R = (Highest High - Close) / (Highest High - Lowest Low) * -100
        self.lines.williams_r = -100 * (highest_high - self.data.close) / (highest_high - lowest_low)
