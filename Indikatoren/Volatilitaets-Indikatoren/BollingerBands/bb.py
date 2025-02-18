import backtrader as bt

class BollingerBands(bt.Indicator):
    """
    Bollinger Bands (BB)
    
    Besteht aus einem mittleren Band (typischerweise SMA) und zwei äußeren Bändern,
    die n Standardabweichungen vom mittleren Band entfernt sind.
    
    Formel:
    Middle Band = SMA(n)
    Upper Band = Middle Band + (Standardabweichung × Multiplikator)
    Lower Band = Middle Band - (Standardabweichung × Multiplikator)
    
    Parameter:
    - period (20): Periode für SMA und Standardabweichung
    - devfactor (2.0): Multiplikator für Standardabweichung
    - movav (SMA): Typ des gleitenden Durchschnitts
    """
    
    lines = ('mid', 'top', 'bot', 'pct_b', 'bandwidth')
    params = (
        ('period', 20),
        ('devfactor', 2.0),
        ('movav', bt.indicators.SMA),
    )
    
    plotlines = dict(
        mid=dict(color='navy', _name='Middle'),
        top=dict(color='red', _name='Upper'),
        bot=dict(color='red', _name='Lower'),
        pct_b=dict(_plotskip=True),  # %B wird nicht standardmäßig geplottet
        bandwidth=dict(_plotskip=True)  # Bandwidth wird nicht standardmäßig geplottet
    )
    
    plotinfo = dict(subplot=False)
    
    def __init__(self):
        # Mittleres Band (SMA)
        self.lines.mid = ma = self.p.movav(self.data, period=self.p.period)
        
        # Standardabweichung
        stddev = bt.indicators.StandardDeviation(self.data, period=self.p.period)
        
        # Oberes und unteres Band
        self.lines.top = ma + stddev * self.p.devfactor
        self.lines.bot = ma - stddev * self.p.devfactor
        
        # %B = (Preis - Unteres Band) / (Oberes Band - Unteres Band)
        self.lines.pct_b = (self.data - self.lines.bot) / (self.lines.top - self.lines.bot)
        
        # Bandwidth = (Oberes Band - Unteres Band) / Mittleres Band
        self.lines.bandwidth = (self.lines.top - self.lines.bot) / self.lines.mid
