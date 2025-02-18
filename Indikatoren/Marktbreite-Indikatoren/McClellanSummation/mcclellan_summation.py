import backtrader as bt

class McClellanSummationIndex(bt.Indicator):
    """
    McClellan Summation Index
    
    Eine kumulative Version des McClellan Oscillators. Zeigt längerfristige Trends
    in der Marktbreite an.
    
    Formel:
    Summation Index(heute) = Summation Index(gestern) + McClellan Oscillator(heute)
    
    Parameter:
    - fast_period (19): Periode für schnellen EMA im McClellan Oscillator
    - slow_period (39): Periode für langsamen EMA im McClellan Oscillator
    """
    
    lines = ('summation', 'ma')
    params = (
        ('fast_period', 19),
        ('slow_period', 39),
        ('ma_period', 20)
    )
    
    plotlines = dict(
        summation=dict(color='darkgreen', _name='Summation'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # McClellan Oscillator berechnen
        self.oscillator = McClellanOscillator(
            self.data0, self.data1,
            fast_period=self.p.fast_period,
            slow_period=self.p.slow_period
        )
        
        # Summation Index initialisieren
        self.cumsum = 0
        
        # Gleitender Durchschnitt
        self.lines.ma = bt.indicators.EMA(
            self.lines.summation,
            period=self.p.ma_period
        )
        
    def next(self):
        # Addiere McClellan Oscillator zum Summation Index
        self.cumsum += self.oscillator.oscillator[0]
        self.lines.summation[0] = self.cumsum
