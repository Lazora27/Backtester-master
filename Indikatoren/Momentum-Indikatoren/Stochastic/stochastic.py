import backtrader as bt

class StochasticOscillator(bt.Indicator):
    """
    Stochastic Oscillator
    
    Der Stochastic Oscillator vergleicht den aktuellen Schlusskurs mit der Preisspanne
    über einen bestimmten Zeitraum. Er besteht aus zwei Linien:
    - %K: Die Hauptlinie (Fast Stochastic)
    - %D: Signal-Linie (Slow Stochastic)
    
    Parameter:
    - period_k (14): Periode für %K Berechnung
    - period_d (3): Periode für %D Berechnung (Signal-Linie)
    - period_smooth (3): Glättungsperiode für Slow Stochastic
    """
    
    lines = ('percentK', 'percentD')
    params = (
        ('period_k', 14),
        ('period_d', 3),
        ('period_smooth', 3),
    )
    
    plotlines = dict(
        percentK=dict(color='blue', _name='%K'),
        percentD=dict(color='red', _name='%D')
    )
    
    def __init__(self):
        # Höchster Hoch und niedrigster Tief über period_k
        highest_high = bt.indicators.Highest(self.data.high, period=self.p.period_k)
        lowest_low = bt.indicators.Lowest(self.data.low, period=self.p.period_k)
        
        # %K Berechnung (Fast Stochastic)
        k = 100 * (self.data.close - lowest_low) / (highest_high - lowest_low)
        
        # Glättung für Slow Stochastic
        k_smooth = bt.indicators.SMA(k, period=self.p.period_smooth)
        
        self.lines.percentK = k_smooth
        self.lines.percentD = bt.indicators.SMA(k_smooth, period=self.p.period_d)
