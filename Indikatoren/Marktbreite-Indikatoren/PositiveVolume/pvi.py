import backtrader as bt

class PositiveVolumeIndex(bt.Indicator):
    """
    Positive Volume Index (PVI)
    
    Ein Indikator, der Preisänderungen nur an Tagen mit steigendem Volumen
    berücksichtigt. Basiert auf der Theorie, dass die breite Masse an Tagen mit
    hohem Volumen aktiv ist.
    
    Formel:
    Wenn Volume > Volume(-1):
        PVI = PVI(-1) + ((Close - Close(-1)) / Close(-1)) × 100
    Sonst:
        PVI = PVI(-1)
        
    Parameter:
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (255): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('pvi', 'ma')
    params = (
        ('moving_average', True),
        ('ma_period', 255)
    )
    
    plotlines = dict(
        pvi=dict(color='darkblue', _name='PVI'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        self.addminperiod(2)
        
        # Preisänderung in Prozent
        self.pct_change = self.data0.close / self.data0.close(-1) - 1.0
        
        # Volumenänderung
        self.vol_increase = self.data0.volume > self.data0.volume(-1)
        
        # Startwert
        self.pvi = 1000.0
        
    def next(self):
        if self.vol_increase[0]:
            # Aktualisiere PVI nur bei steigendem Volumen
            self.pvi *= (1.0 + self.pct_change[0])
            
        self.lines.pvi[0] = self.pvi
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.pvi,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
class PVINVIComparison(bt.Indicator):
    """
    PVI/NVI Vergleich
    
    Vergleicht PVI und NVI, um die relative Stärke von "Smart Money" vs.
    "Crowd" zu messen.
    
    Parameter:
    - ma_period (20): Glättungsperiode für das Verhältnis
    """
    
    lines = ('ratio', 'ma')
    params = (('ma_period', 20),)
    
    plotlines = dict(
        ratio=dict(color='darkgreen', _name='PVI/NVI'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # PVI und NVI berechnen
        pvi = PositiveVolumeIndex(self.data0)
        nvi = NegativeVolumeIndex(self.data0)
        
        # Verhältnis berechnen
        self.lines.ratio = bt.indicators.DivByZero(
            pvi.pvi, nvi.nvi,
            zero=1.0
        )
        
        # Gleitender Durchschnitt
        self.lines.ma = bt.indicators.EMA(
            self.lines.ratio,
            period=self.p.ma_period
        )
