import backtrader as bt

class PutCallRatio(bt.Indicator):
    """
    Put-Call Ratio (PCR)
    
    Ein Sentiment-Indikator, der das Verhältnis von Put- zu Call-Optionsvolumen
    misst. Hohe Werte deuten auf bearishes Sentiment hin, niedrige auf bullishes.
    
    Formel:
    PCR = Put Volume / Call Volume
    
    Parameter:
    - period (1): Glättungsperiode
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('pcr', 'ma')
    params = (
        ('period', 1),
        ('moving_average', True),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        pcr=dict(color='darkblue', _name='PCR'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # Put-Call Ratio berechnen
        self.lines.pcr = bt.indicators.DivByZero(
            self.data0,  # Put Volume
            self.data1,  # Call Volume
            zero=1.0
        )
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.pcr,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Extremwerte oder Trendwenden im Sentiment
        pass
        
class WeightedPutCallRatio(bt.Indicator):
    """
    Weighted Put-Call Ratio
    
    Eine erweiterte Version des PCR, die das Optionsvolumen nach dem
    Strike-Preis gewichtet.
    
    Formel:
    WPCR = (Put Volume × Put Strike) / (Call Volume × Call Strike)
    
    Parameter:
    - period (1): Glättungsperiode
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('wpcr', 'ma')
    params = (
        ('period', 1),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        wpcr=dict(color='darkgreen', _name='WPCR'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # Gewichtetes Put-Volume
        weighted_puts = self.data0 * self.data2  # Volume × Strike
        
        # Gewichtetes Call-Volume
        weighted_calls = self.data1 * self.data3  # Volume × Strike
        
        # Weighted PCR berechnen
        self.lines.wpcr = bt.indicators.DivByZero(
            weighted_puts,
            weighted_calls,
            zero=1.0
        )
        
        # Gleitender Durchschnitt
        self.lines.ma = bt.indicators.EMA(
            self.lines.wpcr,
            period=self.p.ma_period
        )
