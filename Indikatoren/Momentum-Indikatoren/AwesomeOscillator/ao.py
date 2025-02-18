import backtrader as bt

class AwesomeOscillator(bt.Indicator):
    """
    Awesome Oscillator (AO)
    
    Misst das Marktmomentum durch Vergleich eines schnellen und eines langsamen 
    gleitenden Durchschnitts der Mittelpunktpreise.
    
    Formel: AO = SMA(5, Median Price) - SMA(34, Median Price)
    Median Price = (High + Low) / 2
    
    Signale:
    - Kreuzen der Nulllinie
    - Saucerschallenmuster
    - Twin Peaks
    
    Parameter:
    - fast_period (5): Periode für den schnellen MA
    - slow_period (34): Periode für den langsamen MA
    """
    
    lines = ('ao',)
    params = (
        ('fast_period', 5),
        ('slow_period', 34)
    )
    
    plotlines = dict(
        ao=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Berechne Median Price
        median_price = (self.data.high + self.data.low) / 2.0
        
        # Berechne schnellen und langsamen SMA
        fast_sma = bt.indicators.SMA(median_price, period=self.p.fast_period)
        slow_sma = bt.indicators.SMA(median_price, period=self.p.slow_period)
        
        # Awesome Oscillator = Fast SMA - Slow SMA
        self.lines.ao = fast_sma - slow_sma
