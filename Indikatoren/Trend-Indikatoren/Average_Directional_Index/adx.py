import backtrader as bt

class AverageDirectionalIndex(bt.Indicator):
    """
    Average Directional Index (ADX)
    
    Der ADX misst die Stärke eines Trends, unabhängig von seiner Richtung.
    Werte über 25 deuten auf einen starken Trend hin.
    
    Komponenten:
    - +DI: Positive Directional Indicator
    - -DI: Negative Directional Indicator
    - ADX: Average Directional Index
    
    Parameter:
    - period (14): Periode für die Berechnung
    """
    
    lines = ('adx', 'dip', 'din')
    params = (('period', 14),)
    
    plotlines = dict(
        adx=dict(color='black'),
        dip=dict(color='green'),
        din=dict(color='red')
    )
    
    def __init__(self):
        # Berechne True Range
        self.tr = bt.indicators.TrueRange(self.data)
        self.atr = bt.indicators.SmoothedMovingAverage(self.tr, period=self.p.period)
        
        # Berechne Directional Movement
        self.dp = bt.indicators.Max(0.0, self.data.high - self.data.high(-1))
        self.dm = bt.indicators.Max(0.0, self.data.low(-1) - self.data.low)
        
        # Berechne +DI und -DI
        self.dip = bt.indicators.SmoothedMovingAverage(self.dp, period=self.p.period) / self.atr * 100
        self.din = bt.indicators.SmoothedMovingAverage(self.dm, period=self.p.period) / self.atr * 100
        
        # Berechne DX
        self.dx = abs(self.dip - self.din) / (self.dip + self.din) * 100
        
        # Berechne ADX
        self.adx = bt.indicators.SmoothedMovingAverage(self.dx, period=self.p.period)
