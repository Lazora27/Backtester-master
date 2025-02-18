import backtrader as bt

class EldersForceIndex(bt.Indicator):
    """
    Elder's Force Index (EFI)
    
    Kombiniert Preis und Volumen, um die Kraft hinter einer Preisbewegung zu messen.
    Positive Werte zeigen Kaufdruck an, negative Werte Verkaufsdruck.
    
    Formel:
    1. Raw Force = (Current Close - Previous Close) × Volume
    2. Force Index = EMA(Raw Force, period)
    
    Parameter:
    - period (13): Periode für den EMA
    """
    
    lines = ('efi',)
    params = (('period', 13),)
    
    plotlines = dict(
        efi=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Berechne Preisänderung
        price_change = self.data.close - self.data.close(-1)
        
        # Raw Force = Preisänderung × Volumen
        raw_force = price_change * self.data.volume
        
        # Force Index = EMA der Raw Force
        self.lines.efi = bt.indicators.EMA(raw_force, period=self.p.period)
        
    def next(self):
        # Zusätzliche Signallogik könnte hier implementiert werden
        pass
