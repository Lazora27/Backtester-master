import backtrader as bt
import numpy as np

class FibonacciRetracement(bt.Indicator):
    """
    Fibonacci Retracement
    
    Berechnet Fibonacci-Retracement-Levels basierend auf einem Hoch-Tief-Swing.
    Die klassischen Fibonacci-Levels sind: 23.6%, 38.2%, 50%, 61.8% und 78.6%.
    
    Der Indikator:
    - Identifiziert potenzielle Unterstützungs-/Widerstandslevels
    - Berechnet automatisch Swing High/Low
    - Unterstützt manuelle Level-Eingabe
    - Bietet zusätzliche Fibonacci-Extensions
    
    Parameter:
    - period (20): Periode für Swing High/Low Identifikation
    - levels (None): Manuelle High/Low Levels
    - use_extensions (False): Ob Extensions berechnet werden sollen
    """
    
    lines = ('level_236', 'level_382', 'level_500', 'level_618', 'level_786')
    params = (
        ('period', 20),
        ('levels', None),  # (high, low) Tuple
        ('use_extensions', False)
    )
    
    plotlines = dict(
        level_236=dict(color='darkblue', _name='23.6%'),
        level_382=dict(color='blue', _name='38.2%'),
        level_500=dict(color='darkgreen', _name='50.0%'),
        level_618=dict(color='green', _name='61.8%'),
        level_786=dict(color='red', _name='78.6%')
    )
    
    def __init__(self):
        super(FibonacciRetracement, self).__init__()
        
        # Fibonacci Ratios
        self.fib_ratios = [0.236, 0.382, 0.5, 0.618, 0.786]
        
        if self.p.levels is not None:
            self.high, self.low = self.p.levels
        else:
            # Automatische Swing High/Low Identifikation
            self.high = bt.indicators.Highest(
                self.data.high,
                period=self.p.period
            )
            self.low = bt.indicators.Lowest(
                self.data.low,
                period=self.p.period
            )
            
    def next(self):
        range_size = self.high[0] - self.low[0]
        
        # Retracement Levels berechnen
        self.lines.level_236[0] = self.high[0] - range_size * 0.236
        self.lines.level_382[0] = self.high[0] - range_size * 0.382
        self.lines.level_500[0] = self.high[0] - range_size * 0.500
        self.lines.level_618[0] = self.high[0] - range_size * 0.618
        self.lines.level_786[0] = self.high[0] - range_size * 0.786
        
class FibonacciZones(bt.Indicator):
    """
    Fibonacci Zonen
    
    Identifiziert Preiszonen zwischen Fibonacci-Levels und deren Stärke.
    
    Parameter:
    - period (20): Periode für die Berechnung
    - zone_threshold (0.1): Schwellenwert für Zonenstärke
    """
    
    lines = ('zone_strength',)
    params = (
        ('period', 20),
        ('zone_threshold', 0.1)
    )
    
    plotlines = dict(
        zone_strength=dict(
            _method='bar',
            alpha=0.5,
            width=0.7,
            color='gray'
        )
    )
    
    def __init__(self):
        # Fibonacci Retracements
        self.fib = FibonacciRetracement(
            self.data,
            period=self.p.period
        )
        
        # Preisabstand zu Fibonacci-Levels
        self.distances = []
        for line in [self.fib.level_236, self.fib.level_382,
                    self.fib.level_500, self.fib.level_618,
                    self.fib.level_786]:
            self.distances.append(
                abs(self.data.close - line) / self.data.close
            )
            
        # Zonenstärke
        self.lines.zone_strength = bt.indicators.Min(
            self.distances,
            period=1
        ) < self.p.zone_threshold
