import backtrader as bt

class TickIndex(bt.Indicator):
    """
    Tick Index
    
    Ein kurzfristiger Marktbreiten-Indikator, der das Verhältnis von Upticks zu
    Downticks misst. Wird oft für intraday Trading verwendet.
    
    Formel:
    Tick Index = ((Upticks - Downticks) / (Upticks + Downticks)) × 100
    
    Parameter:
    - period (1): Glättungsperiode
    - moving_average (True): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('tick_index', 'ma')
    params = (
        ('period', 1),
        ('moving_average', True),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        tick_index=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        ma=dict(color='blue', _name='MA')
    )
    
    def __init__(self):
        # Gesamtzahl der Ticks
        total_ticks = self.data0 + self.data1  # Upticks + Downticks
        
        # Tick Index berechnen
        self.lines.tick_index = ((self.data0 - self.data1) / total_ticks) * 100
        
        # Optional: Gleitender Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.tick_index,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
class TickVolume(bt.Indicator):
    """
    Tick Volume
    
    Ergänzender Indikator zum Tick Index, der das Gesamtvolumen der Ticks
    analysiert.
    
    Parameter:
    - ma_period (10): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('volume', 'ma')
    params = (('ma_period', 10),)
    
    plotlines = dict(
        volume=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            color='darkgray'
        ),
        ma=dict(color='red', _name='MA')
    )
    
    def __init__(self):
        # Gesamtvolumen
        self.lines.volume = self.data0 + self.data1
        
        # Gleitender Durchschnitt
        self.lines.ma = bt.indicators.EMA(
            self.lines.volume,
            period=self.p.ma_period
        )
