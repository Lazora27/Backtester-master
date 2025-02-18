import backtrader as bt

class KeltnerChannels(bt.Indicator):
    """
    Keltner Channels
    
    Ähnlich wie Bollinger Bands, aber verwendet ATR statt Standardabweichung für
    die Bandbreite. Besteht aus einem mittleren Band (typischerweise EMA) und zwei
    äußeren Bändern, die n ATR vom mittleren Band entfernt sind.
    
    Formel:
    Middle Line = EMA(Typical Price)
    Upper Band = Middle Line + (n × ATR)
    Lower Band = Middle Line - (n × ATR)
    
    Parameter:
    - period (20): Periode für EMA
    - atr_period (10): Periode für ATR
    - atr_factor (2.0): Multiplikator für ATR
    - movav (EMA): Typ des gleitenden Durchschnitts
    """
    
    lines = ('mid', 'top', 'bot')
    params = (
        ('period', 20),
        ('atr_period', 10),
        ('atr_factor', 2.0),
        ('movav', bt.indicators.EMA)
    )
    
    plotlines = dict(
        mid=dict(color='navy', _name='Middle'),
        top=dict(color='green', _name='Upper'),
        bot=dict(color='green', _name='Lower')
    )
    
    plotinfo = dict(subplot=False)
    
    def __init__(self):
        # Typical Price
        typical_price = (self.data.high + self.data.low + self.data.close) / 3.0
        
        # Mittlere Linie
        self.lines.mid = self.p.movav(typical_price, period=self.p.period)
        
        # ATR für die Bandbreite
        atr = bt.indicators.ATR(
            self.data,
            period=self.p.atr_period
        )
        
        # Oberes und unteres Band
        self.lines.top = self.lines.mid + self.p.atr_factor * atr
        self.lines.bot = self.lines.mid - self.p.atr_factor * atr
