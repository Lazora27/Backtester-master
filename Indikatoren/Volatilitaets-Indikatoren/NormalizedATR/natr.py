import backtrader as bt

class NormalizedAverageTrueRange(bt.Indicator):
    """
    Normalized Average True Range (NATR)
    
    Eine normalisierte Version des ATR, die als Prozentsatz des Schlusskurses
    ausgedrückt wird. Dies ermöglicht bessere Vergleiche zwischen verschiedenen
    Instrumenten.
    
    Formel:
    NATR = (ATR / Close) × 100
    
    Parameter:
    - period (14): Periode für ATR-Berechnung
    - movav (EMA): Typ des gleitenden Durchschnitts
    """
    
    lines = ('natr', 'atr')
    params = (
        ('period', 14),
        ('movav', bt.indicators.EMA)
    )
    
    plotlines = dict(
        natr=dict(color='darkgreen', _name='NATR'),
        atr=dict(_plotskip=True)
    )
    
    def __init__(self):
        # Berechne normalen ATR
        self.lines.atr = atr = bt.indicators.ATR(
            self.data,
            period=self.p.period,
            movav=self.p.movav
        )
        
        # Normalisiere ATR
        self.lines.natr = (atr / self.data.close) * 100
        
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Volatilitäts-Breakouts oder Position Sizing
        pass
