import backtrader as bt
import numpy as np

class AbsoluteBreadthIndex(bt.Indicator):
    """
    Absolute Breadth Index (ABI)
    
    Ein Marktbreiten-Indikator, der die absolute Differenz zwischen
    Advancing und Declining Issues misst.
    
    Features:
    - Marktbreiten-Analyse
    - Trendstärkeberechnung
    - Divergenzanalyse
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - smooth_period (10): Glättungsperiode
    - threshold (0.5): Signalschwelle
    """
    
    lines = ('abi', 'smoothed_abi',
             'trend_strength', 'divergence',
             'signal')
             
    params = (
        ('period', 20),
        ('smooth_period', 10),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        abi=dict(color='blue', _name='ABI'),
        smoothed_abi=dict(color='red', _name='Smoothed ABI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        divergence=dict(color='purple', _name='Divergence'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(AbsoluteBreadthIndex, self).__init__()
        
        # Historie
        self.abi_history = []
        self.price_history = []
        
    def calculate_abi(self):
        """
        Berechnet den Absolute Breadth Index.
        """
        if len(self.data) < 2:
            return 0
            
        advances = sum(1 for i in range(len(self.data[0]))
                      if self.data.close[0][i] >
                         self.data.close[-1][i])
        declines = sum(1 for i in range(len(self.data[0]))
                      if self.data.close[0][i] <
                         self.data.close[-1][i])
                         
        total_issues = len(self.data[0])
        
        return abs(advances - declines) / total_issues
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.abi_history) < 2:
            return 0
            
        return (
            self.abi_history[-1] -
            self.abi_history[-2]
        )
        
    def calculate_divergence(self):
        """
        Berechnet die Divergenz zwischen Preis und ABI.
        """
        if len(self.abi_history) < self.p.period or \
           len(self.price_history) < self.p.period:
            return 0
            
        abi_change = (
            self.abi_history[-1] -
            self.abi_history[-self.p.period]
        )
        price_change = (
            self.price_history[-1] -
            self.price_history[-self.p.period]
        )
        
        if price_change != 0:
            return abi_change / price_change
        return 0
        
    def next(self):
        # ABI berechnen
        abi = self.calculate_abi()
        self.abi_history.append(abi)
        self.lines.abi[0] = abi
        
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Geglätteter ABI
        if len(self.abi_history) >= self.p.smooth_period:
            self.lines.smoothed_abi[0] = np.mean(
                self.abi_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_abi[0] = abi
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.calculate_divergence()
        
        # Signal
        if abs(self.lines.divergence[0]) > self.p.threshold:
            if (self.lines.divergence[0] > self.p.threshold and
                self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.lines.divergence[0] < -self.p.threshold and
                  self.lines.trend_strength[0] < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.abi_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'abi': {
                'value': self.lines.abi[0],
                'smoothed': self.lines.smoothed_abi[0],
                'trend': (
                    'increasing'
                    if self.lines.abi[0] >
                       self.lines.smoothed_abi[0]
                    else 'decreasing'
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
            'divergence': {
                'value': self.lines.divergence[0],
                'significance': (
                    'high'
                    if abs(self.lines.divergence[0]) >
                       self.p.threshold
                    else 'low'
                ),
                'type': (
                    'positive'
                    if self.lines.divergence[0] > 0
                    else 'negative'
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
                    abs(self.lines.trend_strength[0]) *
                    abs(self.lines.divergence[0])
                    if abs(self.lines.divergence[0]) <=
                       2 * self.p.threshold
                    else 0
                )
            },
            'market_state': {
                'breadth': (
                    'wide' if self.lines.abi[0] > 0.7
                    else 'narrow' if self.lines.abi[0] < 0.3
                    else 'normal'
                ),
                'trend_confirmation': (
                    'confirmed'
                    if (self.lines.trend_strength[0] > 0 and
                        self.lines.divergence[0] > 0) or
                       (self.lines.trend_strength[0] < 0 and
                        self.lines.divergence[0] < 0)
                    else 'divergent'
                ),
                'market_quality': (
                    'healthy'
                    if self.lines.abi[0] > 0.5 and
                       abs(self.lines.divergence[0]) <
                       self.p.threshold
                    else 'weak'
                )
            }
        }
