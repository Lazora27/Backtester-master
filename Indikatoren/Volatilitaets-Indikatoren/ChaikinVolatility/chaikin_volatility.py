import backtrader as bt

class ChaikinVolatility(bt.Indicator):
    """
    Chaikin Volatility Indicator
    
    Misst die Volatilität als Rate der Veränderung des High-Low Ranges.
    Steigende Werte zeigen zunehmende Volatilität an, fallende Werte abnehmende.
    
    Formel:
    1. High-Low Range = High - Low
    2. Range MA = EMA(High-Low Range, n)
    3. ROC = ((Current Range MA - Range MA n periods ago) / Range MA n periods ago) × 100
    
    Parameter:
    - ema_period (10): Periode für den EMA des Ranges
    - roc_period (10): Periode für Rate of Change
    - movav (EMA): Typ des gleitenden Durchschnitts
    """
    
    lines = ('cv',)
    params = (
        ('ema_period', 10),
        ('roc_period', 10),
        ('movav', bt.indicators.EMA)
    )
    
    plotlines = dict(
        cv=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # High-Low Range
        hl_range = self.data.high - self.data.low
        
        # Geglätteter Range
        range_ma = self.p.movav(hl_range, period=self.p.ema_period)
        
        # Rate of Change des geglätteten Ranges
        range_ma_ago = range_ma(-self.p.roc_period)
        
        # Chaikin Volatility
        self.lines.cv = bt.If(
            range_ma_ago != 0,
            ((range_ma - range_ma_ago) / range_ma_ago) * 100,
            0.0
        )
