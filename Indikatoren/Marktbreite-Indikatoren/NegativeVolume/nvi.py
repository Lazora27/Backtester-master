import backtrader as bt

class NegativeVolumeIndex(bt.Indicator):
    """
    Negative Volume Index (NVI)
    
    Ein Indikator, der Preisänderungen nur an Tagen mit sinkendem Volumen
    berücksichtigt. Basiert auf der Theorie, dass "Smart Money" an Tagen mit
    niedrigem Volumen aktiv ist.
    
    Formel:
    Wenn Volume < Volume(-1):
        NVI = NVI(-1) + ((Close - Close(-1)) / Close(-1)) × 100
    Sonst:
        NVI = NVI(-1)
        
    Parameter:
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (255): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('nvi', 'ma')
    params = (
        ('moving_average', True),
        ('ma_period', 255)
    )
    
    plotlines = dict(
        nvi=dict(color='darkgreen', _name='NVI'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        self.addminperiod(2)
        
        # Preisänderung in Prozent
        self.pct_change = self.data0.close / self.data0.close(-1) - 1.0
        
        # Volumenänderung
        self.vol_decrease = self.data0.volume < self.data0.volume(-1)
        
        # Startwert
        self.nvi = 1000.0
        
    def next(self):
        if self.vol_decrease[0]:
            # Aktualisiere NVI nur bei sinkendem Volumen
            self.nvi *= (1.0 + self.pct_change[0])
            
        self.lines.nvi[0] = self.nvi
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.nvi,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
class NVISignals(bt.Indicator):
    """
    NVI Signale
    
    Generiert Handelssignale basierend auf dem NVI und seinem gleitenden
    Durchschnitt.
    
    Parameter:
    - ma_period (255): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('signal',)
    params = (('ma_period', 255),)
    
    plotlines = dict(
        signal=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        nvi = NegativeVolumeIndex(self.data0)
        self.lines.signal = nvi.nvi - nvi.ma
