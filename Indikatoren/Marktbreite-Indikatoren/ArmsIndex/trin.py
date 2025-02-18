import backtrader as bt

class ArmsIndex(bt.Indicator):
    """
    Arms Index (TRIN - TRading INdex)
    
    Ein Indikator, der das Verhältnis von steigenden zu fallenden Aktien mit dem
    Verhältnis der Volumina dieser Aktien vergleicht.
    
    Formel:
    TRIN = (Advances/Declines) / (Advance Volume/Decline Volume)
    
    Parameter:
    - period (1): Glättungsperiode
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('trin', 'ma')
    params = (
        ('period', 1),
        ('moving_average', True),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        trin=dict(color='darkblue', _name='TRIN'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # Verhältnis von Advances zu Declines
        ad_ratio = bt.indicators.DivByZero(
            self.data0, self.data1,
            zero=1.0
        )
        
        # Verhältnis von Advance Volume zu Decline Volume
        vol_ratio = bt.indicators.DivByZero(
            self.data2, self.data3,
            zero=1.0
        )
        
        # TRIN berechnen
        self.lines.trin = bt.indicators.DivByZero(
            ad_ratio, vol_ratio,
            zero=1.0
        )
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.trin,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Überverkauft/Überkauft-Levels
        pass
