import backtrader as bt

class HighLowIndex(bt.Indicator):
    """
    High-Low Index
    
    Ein Marktbreiten-Indikator, der das Verhältnis von neuen Hochs zu neuen Tiefs
    misst. Wird oft verwendet, um die Stärke eines Trends zu bestätigen.
    
    Formel:
    High-Low Index = (New Highs / (New Highs + New Lows)) × 100
    
    Parameter:
    - period (10): Glättungsperiode
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('hl_index', 'ma')
    params = (
        ('period', 10),
        ('moving_average', True),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        hl_index=dict(color='darkgreen', _name='HL Index'),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # High-Low Index berechnen
        total = self.data0 + self.data1  # New Highs + New Lows
        
        # Verhältnis berechnen und in Prozent umwandeln
        self.lines.hl_index = bt.indicators.DivByZero(
            self.data0, total,
            zero=0.5
        ) * 100
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.hl_index,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Trendbestätigung oder Divergenzanalyse
        pass
        
class HighLowDifference(bt.Indicator):
    """
    High-Low Difference
    
    Alternative Version des High-Low Index, die die absolute Differenz zwischen
    neuen Hochs und neuen Tiefs berechnet.
    
    Formel:
    HL Difference = New Highs - New Lows
    
    Parameter:
    - normalize (True): Ob die Differenz als Prozentsatz ausgegeben werden soll
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('diff', 'ma')
    params = (
        ('normalize', True),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        diff=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        ma=dict(color='blue', _name='MA')
    )
    
    def __init__(self):
        # Differenz berechnen
        self.lines.diff = self.data0 - self.data1
        
        if self.p.normalize:
            # Als Prozentsatz der Gesamtzahl
            total = self.data0 + self.data1
            self.lines.diff = (self.lines.diff / total) * 100
            
        # Gleitender Durchschnitt
        self.lines.ma = bt.indicators.EMA(
            self.lines.diff,
            period=self.p.ma_period
        )
