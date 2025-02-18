import backtrader as bt
import numpy as np

class FibonacciExtensions(bt.Indicator):
    """
    Fibonacci Extensions
    
    Berechnet Fibonacci-Extension-Levels über/unter einem Trend.
    Die klassischen Extension-Levels sind: 127.2%, 161.8%, 261.8% und 423.6%.
    
    Der Indikator:
    - Identifiziert potenzielle Kursziele
    - Berechnet Extensions für Aufwärts- und Abwärtstrends
    - Unterstützt manuelle Level-Eingabe
    
    Parameter:
    - period (20): Periode für Swing-Punkt Identifikation
    - levels (None): Manuelle High/Low/Retracement Levels
    - trend_mode ('auto'): 'up', 'down' oder 'auto'
    """
    
    lines = ('ext_1272', 'ext_1618', 'ext_2618', 'ext_4236')
    params = (
        ('period', 20),
        ('levels', None),  # (high, low, retracement) Tuple
        ('trend_mode', 'auto')
    )
    
    plotlines = dict(
        ext_1272=dict(color='darkblue', _name='127.2%'),
        ext_1618=dict(color='blue', _name='161.8%'),
        ext_2618=dict(color='green', _name='261.8%'),
        ext_4236=dict(color='red', _name='423.6%')
    )
    
    def __init__(self):
        super(FibonacciExtensions, self).__init__()
        
        # Extension Ratios
        self.ext_ratios = [1.272, 1.618, 2.618, 4.236]
        
        if self.p.levels is not None:
            self.high, self.low, self.retracement = self.p.levels
        else:
            # Automatische Swing-Punkt Identifikation
            self.high = bt.indicators.Highest(
                self.data.high,
                period=self.p.period
            )
            self.low = bt.indicators.Lowest(
                self.data.low,
                period=self.p.period
            )
            self.retracement = self.data.close
            
    def next(self):
        trend_range = self.high[0] - self.low[0]
        retracement_range = self.high[0] - self.retracement[0]
        
        if self.p.trend_mode == 'auto':
            # Trendrichtung automatisch bestimmen
            is_uptrend = self.data.close[0] > self.data.close[-self.p.period]
        else:
            is_uptrend = self.p.trend_mode == 'up'
            
        if is_uptrend:
            # Aufwärtstrend Extensions
            self.lines.ext_1272[0] = self.high[0] + trend_range * 0.272
            self.lines.ext_1618[0] = self.high[0] + trend_range * 0.618
            self.lines.ext_2618[0] = self.high[0] + trend_range * 1.618
            self.lines.ext_4236[0] = self.high[0] + trend_range * 3.236
        else:
            # Abwärtstrend Extensions
            self.lines.ext_1272[0] = self.low[0] - trend_range * 0.272
            self.lines.ext_1618[0] = self.low[0] - trend_range * 0.618
            self.lines.ext_2618[0] = self.low[0] - trend_range * 1.618
            self.lines.ext_4236[0] = self.low[0] - trend_range * 3.236
            
class ExtensionProjections(bt.Indicator):
    """
    Extension Projections
    
    Berechnet Wahrscheinlichkeitszonen für Kursziele basierend auf
    Fibonacci-Extensions.
    
    Parameter:
    - period (20): Basisperiode
    - confidence (0.95): Konfidenzintervall
    """
    
    lines = ('projection', 'upper', 'lower')
    params = (
        ('period', 20),
        ('confidence', 0.95)
    )
    
    plotlines = dict(
        projection=dict(color='darkgreen', _name='Projection'),
        upper=dict(color='red', _name='Upper'),
        lower=dict(color='red', _name='Lower')
    )
    
    def __init__(self):
        # Extensions
        self.ext = FibonacciExtensions(
            self.data,
            period=self.p.period
        )
        
        # Mittlere Extension
        self.lines.projection = (self.ext.ext_1618 + self.ext.ext_2618) / 2
        
        # Konfidenzintervall
        std = bt.indicators.StandardDeviation(
            self.data.close,
            period=self.p.period
        )
        
        z_score = 1.96  # 95% Konfidenzintervall
        
        self.lines.upper = self.lines.projection + z_score * std
        self.lines.lower = self.lines.projection - z_score * std
