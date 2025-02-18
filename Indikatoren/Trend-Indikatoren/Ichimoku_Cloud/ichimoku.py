import backtrader as bt

class IchimokuCloud(bt.Indicator):
    """
    Ichimoku Cloud (Ichimoku Kinko Hyo)
    
    Ein komplexer Indikator, der mehrere Komponenten kombiniert:
    - Tenkan-sen (Conversion Line)
    - Kijun-sen (Base Line)
    - Senkou Span A (Leading Span A)
    - Senkou Span B (Leading Span B)
    - Chikou Span (Lagging Span)
    
    Parameter:
    - tenkan (9): Periode für Tenkan-sen
    - kijun (26): Periode für Kijun-sen
    - senkou (52): Periode für Senkou Span B
    - displacement (26): Verschiebung für die Cloud
    """
    
    lines = ('tenkan', 'kijun', 'senkou_a', 'senkou_b', 'chikou')
    params = (
        ('tenkan', 9),
        ('kijun', 26),
        ('senkou', 52),
        ('displacement', 26)
    )
    
    plotinfo = dict(subplot=False)
    plotlines = dict(
        tenkan=dict(linestyle='-'),
        kijun=dict(linestyle='-'),
        senkou_a=dict(fill_gt=('senkou_b', '#00ff0020'),
                     fill_lt=('senkou_b', '#ff000020')),
        senkou_b=dict(),
        chikou=dict(linestyle='--')
    )
    
    def __init__(self):
        super(IchimokuCloud, self).__init__()
        
        # Tenkan-sen (Conversion Line)
        high_tenkan = bt.indicators.Highest(self.data.high, period=self.p.tenkan)
        low_tenkan = bt.indicators.Lowest(self.data.low, period=self.p.tenkan)
        self.lines.tenkan = (high_tenkan + low_tenkan) / 2.0
        
        # Kijun-sen (Base Line)
        high_kijun = bt.indicators.Highest(self.data.high, period=self.p.kijun)
        low_kijun = bt.indicators.Lowest(self.data.low, period=self.p.kijun)
        self.lines.kijun = (high_kijun + low_kijun) / 2.0
        
        # Senkou Span A (Leading Span A)
        self.lines.senkou_a = ((self.lines.tenkan + self.lines.kijun) / 2.0).shift(self.p.displacement)
        
        # Senkou Span B (Leading Span B)
        high_senkou = bt.indicators.Highest(self.data.high, period=self.p.senkou)
        low_senkou = bt.indicators.Lowest(self.data.low, period=self.p.senkou)
        self.lines.senkou_b = ((high_senkou + low_senkou) / 2.0).shift(self.p.displacement)
        
        # Chikou Span (Lagging Span)
        self.lines.chikou = self.data.close(-self.p.displacement)
