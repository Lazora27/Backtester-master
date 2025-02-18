import backtrader as bt

class VolumeRateOfChange(bt.Indicator):
    """
    Volume Rate of Change (VROC)
    
    Misst die prozentuale Änderung des Volumens über eine bestimmte Periode.
    Hilft bei der Identifizierung von Volumentrends und möglichen Trendwenden.
    
    Formel:
    VROC = ((Current Volume - Volume n periods ago) / Volume n periods ago) * 100
    
    Parameter:
    - period (25): Lookback-Periode für die Berechnung
    """
    
    lines = ('vroc',)
    params = (('period', 25),)
    
    plotlines = dict(
        vroc=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Hole Volumen vor n Perioden
        volume_n_periods_ago = self.data.volume(-self.p.period)
        
        # Berechne VROC
        self.lines.vroc = ((self.data.volume - volume_n_periods_ago) / 
                          volume_n_periods_ago) * 100
        
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Divergenzen zwischen VROC und Preis
        pass
