import backtrader as bt

class VolumeOscillator(bt.Indicator):
    """
    Volume Oscillator
    
    Vergleicht zwei gleitende Durchschnitte des Volumens unterschiedlicher Länge.
    Zeigt Zu- und Abnahme der Handelsaktivität an.
    
    Formel:
    VO = ((Schneller MA - Langsamer MA) / Langsamer MA) × 100
    
    Parameter:
    - fast_period (12): Periode für schnellen MA
    - slow_period (26): Periode für langsamen MA
    - movav (SMA): Typ des gleitenden Durchschnitts
    """
    
    lines = ('vo',)
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('movav', bt.indicators.SMA)
    )
    
    plotlines = dict(
        vo=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Berechne schnellen und langsamen MA des Volumens
        fast_ma = self.p.movav(self.data.volume, period=self.p.fast_period)
        slow_ma = self.p.movav(self.data.volume, period=self.p.slow_period)
        
        # Berechne Oszillator als Prozentsatz
        self.lines.vo = ((fast_ma - slow_ma) / slow_ma) * 100
        
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Divergenzen oder Kreuzungen der Nulllinie
        pass
