import backtrader as bt

class DonchianVolatility(bt.Indicator):
    """
    Donchian Volatility Indicator
    
    Misst die Volatilität basierend auf der Donchian Channel Breite.
    Kann als Alternative zu traditionellen Volatilitätsindikatoren verwendet werden.
    
    Formel:
    1. Channel Width = Upper Channel - Lower Channel
    2. Volatility = (Channel Width / Middle Channel) × 100
    
    Parameter:
    - period (20): Periode für Donchian Channels
    - smoothing_period (10): Glättungsperiode für Volatilität
    """
    
    lines = ('volatility', 'smooth_volatility')
    params = (
        ('period', 20),
        ('smoothing_period', 10)
    )
    
    plotlines = dict(
        volatility=dict(_plotskip=True),
        smooth_volatility=dict(color='darkred', _name='Donchian Vol')
    )
    
    def __init__(self):
        # Donchian Channel Komponenten
        highest_high = bt.indicators.Highest(self.data.high, period=self.p.period)
        lowest_low = bt.indicators.Lowest(self.data.low, period=self.p.period)
        middle_channel = (highest_high + lowest_low) / 2.0
        
        # Channel Breite
        channel_width = highest_high - lowest_low
        
        # Volatilität als Prozentsatz des mittleren Channels
        self.lines.volatility = (channel_width / middle_channel) * 100
        
        # Geglättete Volatilität
        self.lines.smooth_volatility = bt.indicators.EMA(
            self.lines.volatility,
            period=self.p.smoothing_period
        )
        
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Volatilitätsausbrüche oder Mean Reversion
        pass
