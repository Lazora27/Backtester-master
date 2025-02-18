import backtrader as bt

class AdvanceDeclineLine(bt.Indicator):
    """
    Advance/Decline Line (A/D Line)
    
    Ein kumulativer Indikator, der die Differenz zwischen steigenden und fallenden
    Aktien über die Zeit aufaddiert. Zeigt die Marktbreite und potenzielle
    Divergenzen zum Hauptindex.
    
    Formel:
    A/D Line(heute) = A/D Line(gestern) + (Advances - Declines)
    
    Parameter:
    - advances_data: Datenquelle für steigende Aktien
    - declines_data: Datenquelle für fallende Aktien
    """
    
    lines = ('ad_line',)
    
    plotlines = dict(
        ad_line=dict(color='darkblue', _name='A/D Line')
    )
    
    def __init__(self):
        self.addminperiod(1)
        self.cumsum = 0
        
    def next(self):
        # Berechne tägliche Differenz (Advances - Declines)
        daily_diff = self.data0[0] - self.data1[0]
        
        # Addiere zur kumulativen Summe
        self.cumsum += daily_diff
        
        # Setze A/D Line
        self.lines.ad_line[0] = self.cumsum
        
class AdvanceDeclineRatio(bt.Indicator):
    """
    Advance/Decline Ratio
    
    Verhältnis von steigenden zu fallenden Aktien. Werte über 1 zeigen mehr
    steigende als fallende Aktien an.
    
    Formel:
    A/D Ratio = Advances / Declines
    
    Parameter:
    - period (1): Glättungsperiode für das Verhältnis
    - moving_average (False): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (20): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('ratio', 'ma')
    params = (
        ('period', 1),
        ('moving_average', False),
        ('ma_period', 20)
    )
    
    plotlines = dict(
        ratio=dict(color='green', _name='A/D Ratio'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # Verhältnis berechnen (mit Schutz vor Division durch Null)
        self.lines.ratio = bt.indicators.DivByZero(
            self.data0, self.data1, zero=1.0
        )
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.ratio,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
