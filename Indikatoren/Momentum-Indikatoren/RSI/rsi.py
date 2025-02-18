import backtrader as bt

class RelativeStrengthIndex(bt.Indicator):
    """
    Relative Strength Index (RSI)
    
    Der RSI misst die Stärke eines Trends und identifiziert überkaufte/überverkaufte 
    Marktbedingungen. Werte über 70 deuten auf überkaufte, Werte unter 30 auf 
    überverkaufte Bedingungen hin.
    
    Parameter:
    - period (14): Periode für die Berechnung
    """
    
    lines = ('rsi',)
    params = (('period', 14),)
    
    plotlines = dict(
        rsi=dict(color='navy', _name='RSI')
    )
    
    def __init__(self):
        # Berechne Preisänderungen
        price_change = self.data - self.data(-1)
        
        # Positive und negative Preisänderungen
        gains = price_change.clip(min=0.0)
        losses = (-price_change).clip(min=0.0)
        
        # Exponentiell geglättete Durchschnitte
        avg_gains = bt.indicators.ExponentialMovingAverage(gains, period=self.p.period)
        avg_losses = bt.indicators.ExponentialMovingAverage(losses, period=self.p.period)
        
        # Relative Strength
        rs = avg_gains / avg_losses
        
        # RSI Berechnung
        self.lines.rsi = 100.0 - (100.0 / (1.0 + rs))
