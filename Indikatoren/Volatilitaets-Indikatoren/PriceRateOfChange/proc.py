import backtrader as bt

class PriceRateOfChange(bt.Indicator):
    """
    Price Rate of Change (PROC)
    
    Misst die prozentuale Preisänderung über eine bestimmte Periode.
    Kann als Momentum- und Volatilitätsindikator verwendet werden.
    
    Formel:
    PROC = ((Current Price - Price n periods ago) / Price n periods ago) × 100
    
    Parameter:
    - period (12): Berechnungsperiode
    - moving_average (False): Ob ein gleitender Durchschnitt berechnet werden soll
    - ma_period (9): Periode für den gleitenden Durchschnitt
    """
    
    lines = ('proc', 'ma')
    params = (
        ('period', 12),
        ('moving_average', False),
        ('ma_period', 9)
    )
    
    plotlines = dict(
        proc=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        ma=dict(color='blue', _name='MA')
    )
    
    def __init__(self):
        # Preis vor n Perioden
        price_n_periods_ago = self.data(-self.p.period)
        
        # Berechne PROC
        self.lines.proc = ((self.data - price_n_periods_ago) / 
                          price_n_periods_ago) * 100
        
        # Optional: Berechne gleitenden Durchschnitt
        if self.p.moving_average:
            self.lines.ma = bt.indicators.EMA(
                self.lines.proc,
                period=self.p.ma_period
            )
        else:
            self.lines.ma = bt.indicators.Zero()
            
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Momentum-basierte Handelssignale
        pass
