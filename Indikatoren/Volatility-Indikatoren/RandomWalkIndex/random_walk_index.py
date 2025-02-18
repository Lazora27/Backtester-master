import backtrader as bt
import numpy as np

class RandomWalkIndex(bt.Indicator):
    """
    Random Walk Index (RWI)
    
    Ein Volatilitätsindikator, der die Wahrscheinlichkeit eines
    Random Walks in der Preisbewegung misst.
    
    Features:
    - Random Walk Analyse
    - Trendstärkeberechnung
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - high_low_period (10): High-Low Analyseperiode
    - threshold (0.5): Signalschwelle
    """
    
    lines = ('rwi_high', 'rwi_low',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('high_low_period', 10),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        rwi_high=dict(color='blue', _name='RWI High'),
        rwi_low=dict(color='red', _name='RWI Low'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(RandomWalkIndex, self).__init__()
        
        # Historie
        self.high_history = []
        self.low_history = []
        self.rwi_history = []
        
    def calculate_rwi_high(self):
        """
        Berechnet den RWI für Hochs.
        """
        if len(self.high_history) < self.p.high_low_period:
            return 0
            
        highest = max(self.high_history[-self.p.high_low_period:])
        lowest = min(self.low_history[-self.p.high_low_period:])
        
        if highest == lowest:
            return 0
            
        atr = np.mean([
            self.high_history[i] - self.low_history[i]
            for i in range(-self.p.high_low_period, 0)
        ])
        
        if atr == 0:
            return 0
            
        return (highest - self.low_history[-self.p.high_low_period]) / (
            atr * np.sqrt(self.p.high_low_period)
        )
        
    def calculate_rwi_low(self):
        """
        Berechnet den RWI für Tiefs.
        """
        if len(self.low_history) < self.p.high_low_period:
            return 0
            
        highest = max(self.high_history[-self.p.high_low_period:])
        lowest = min(self.low_history[-self.p.high_low_period:])
        
        if highest == lowest:
            return 0
            
        atr = np.mean([
            self.high_history[i] - self.low_history[i]
            for i in range(-self.p.high_low_period, 0)
        ])
        
        if atr == 0:
            return 0
            
        return (self.high_history[-self.p.high_low_period] - lowest) / (
            atr * np.sqrt(self.p.high_low_period)
        )
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.rwi_history) < 2:
            return 0
            
        return (
            self.rwi_history[-1] -
            self.rwi_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.high_history) < self.p.period:
            return 1.0
            
        current_range = np.mean([
            self.high_history[i] - self.low_history[i]
            for i in range(-5, 0)
        ])
        
        historical_range = np.mean([
            self.high_history[i] - self.low_history[i]
            for i in range(-self.p.period, 0)
        ])
        
        return (
            current_range / historical_range
            if historical_range != 0 else 1.0
        )
        
    def next(self):
        # Historie aktualisieren
        self.high_history.append(self.data.high[0])
        self.low_history.append(self.data.low[0])
        
        # RWI berechnen
        self.lines.rwi_high[0] = self.calculate_rwi_high()
        self.lines.rwi_low[0] = self.calculate_rwi_low()
        
        # RWI Historie
        self.rwi_history.append(
            max(self.lines.rwi_high[0],
                self.lines.rwi_low[0])
        )
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.rwi_high[0] > self.p.threshold and
            self.lines.trend_strength[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.rwi_low[0] > self.p.threshold and
              self.lines.trend_strength[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(self.p.period, self.p.high_low_period)
        for hist in [self.high_history, self.low_history,
                    self.rwi_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'rwi': {
                'high': self.lines.rwi_high[0],
                'low': self.lines.rwi_low[0],
                'spread': (
                    self.lines.rwi_high[0] -
                    self.lines.rwi_low[0]
                ),
                'strength': max(
                    self.lines.rwi_high[0],
                    self.lines.rwi_low[0]
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 1
                )
            },
            'volatility': {
                'ratio': self.lines.volatility_ratio[0],
                'state': (
                    'increasing' if self.lines.volatility_ratio[0] > 1
                    else 'decreasing'
                ),
                'relative_level': (
                    'high' if self.lines.volatility_ratio[0] > 1.5
                    else 'low' if self.lines.volatility_ratio[0] < 0.5
                    else 'normal'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    max(self.lines.rwi_high[0],
                        self.lines.rwi_low[0]) *
                    abs(self.lines.trend_strength[0])
                )
            },
            'risk': {
                'rwi_risk': (
                    1 - max(self.lines.rwi_high[0],
                           self.lines.rwi_low[0])
                    if max(self.lines.rwi_high[0],
                          self.lines.rwi_low[0]) <= 1
                    else 0
                ),
                'trend_risk': (
                    1 - abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 0
                ),
                'volatility_risk': (
                    self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 1
                    else 1 / self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 0
                    else 1
                )
            }
        }
