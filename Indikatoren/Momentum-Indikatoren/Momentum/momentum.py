import backtrader as bt

class MomentumIndicator(bt.Indicator):
    """
    Momentum Indicator
    
    Misst die absolute Preisänderung über eine bestimmte Periode.
    Ein positiver Wert zeigt aufwärts Momentum an, ein negativer Wert abwärts Momentum.
    
    Formel: Momentum = Aktueller Preis - Preis vor n Perioden
    
    Parameter:
    - period (10): Anzahl der Perioden für die Berechnung
    - smoothing (3): Glättungsperiode für das Signal (optional)
    """
    
    lines = ('momentum', 'signal')
    params = (
        ('period', 10),
        ('smoothing', 3)
    )
    
    plotlines = dict(
        momentum=dict(color='blue', _name='Momentum'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # Berechne Momentum
        self.lines.momentum = self.data - self.data(-self.p.period)
        
        # Berechne geglättete Signal-Linie
        self.lines.signal = bt.indicators.SMA(self.lines.momentum, period=self.p.smoothing)
