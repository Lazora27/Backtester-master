import backtrader as bt

class CumulativeVolumeIndex(bt.Indicator):
    """
    Cumulative Volume Index (CVI)
    
    Ein Volumen-basierter Marktbreiten-Indikator, der das kumulative Verhältnis
    von Up-Volume zu Down-Volume misst.
    
    Formel:
    Wenn Close > Close(-1):
        CVI = CVI(-1) + Up Volume
    Sonst:
        CVI = CVI(-1) - Down Volume
        
    Parameter:
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (20): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('cvi', 'ma')
    params = (
        ('moving_average', True),
        ('ma_period', 20)
    )
    
    plotlines = dict(
        cvi=dict(color='darkblue', _name='CVI'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        self.addminperiod(2)
        self.cumsum = 0
        
    def next(self):
        # Prüfe Preisrichtung
        if self.data0[0] > self.data0[-1]:  # Steigender Preis
            self.cumsum += self.data1[0]  # Addiere Up-Volume
        else:
            self.cumsum -= self.data2[0]  # Subtrahiere Down-Volume
            
        self.lines.cvi[0] = self.cumsum
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.cvi,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
class CVIRatio(bt.Indicator):
    """
    CVI Ratio
    
    Eine normalisierte Version des CVI, die das Verhältnis von Up- zu Down-Volume
    als Prozentsatz ausdrückt.
    
    Formel:
    CVI Ratio = (Up Volume / (Up Volume + Down Volume)) × 100
    
    Parameter:
    - period (10): Glättungsperiode
    """
    
    lines = ('ratio',)
    params = (('period', 10),)
    
    plotlines = dict(
        ratio=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_50=0.0, color='green'),
            _fill_lt=dict(_50=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Gesamtvolumen
        total_volume = self.data1 + self.data2
        
        # Ratio berechnen
        self.lines.ratio = bt.indicators.DivByZero(
            self.data1,  # Up Volume
            total_volume,
            zero=0.5
        ) * 100
