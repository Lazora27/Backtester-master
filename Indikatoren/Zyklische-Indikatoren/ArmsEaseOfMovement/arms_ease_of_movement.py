import backtrader as bt
import numpy as np

class ArmsEaseOfMovement(bt.Indicator):
    """
    Arms Ease of Movement (EMV)
    
    Ein Indikator, der die Beziehung zwischen Preis und Volumen
    analysiert, um die "Leichtigkeit der Bewegung" zu messen.
    
    Features:
    - Volumen-Preis-Analyse
    - Trendstärkeberechnung
    - Momentum-Analyse
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - volume_factor (10000): Volumenfaktor
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('emv', 'smoothed_emv',
             'trend_strength', 'momentum',
             'signal')
             
    params = (
        ('period', 14),
        ('volume_factor', 10000),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        emv=dict(color='blue', _name='EMV'),
        smoothed_emv=dict(color='red', _name='Smoothed EMV'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        momentum=dict(color='purple', _name='Momentum'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ArmsEaseOfMovement, self).__init__()
        
        # Historie
        self.emv_history = []
        self.midpoint_history = []
        
    def calculate_midpoint_move(self):
        """
        Berechnet die Midpoint-Bewegung.
        """
        if len(self.data) < 2:
            return 0
            
        current_midpoint = (
            self.data.high[0] +
            self.data.low[0]
        ) / 2
        prev_midpoint = (
            self.data.high[-1] +
            self.data.low[-1]
        ) / 2
        
        return current_midpoint - prev_midpoint
        
    def calculate_box_ratio(self):
        """
        Berechnet das Box Ratio.
        """
        if self.data.volume[0] == 0:
            return 0
            
        box_ratio = (
            self.data.volume[0] /
            self.p.volume_factor
        ) / (
            self.data.high[0] -
            self.data.low[0]
            if self.data.high[0] != self.data.low[0]
            else 1
        )
        
        return box_ratio
        
    def calculate_emv(self):
        """
        Berechnet den Ease of Movement.
        """
        midpoint_move = self.calculate_midpoint_move()
        box_ratio = self.calculate_box_ratio()
        
        if box_ratio == 0:
            return 0
            
        return midpoint_move / box_ratio
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.emv_history) < 2:
            return 0
            
        return (
            self.emv_history[-1] -
            self.emv_history[-2]
        )
        
    def calculate_momentum(self):
        """
        Berechnet das Momentum.
        """
        if len(self.midpoint_history) < self.p.period:
            return 0
            
        return (
            self.midpoint_history[-1] -
            self.midpoint_history[-self.p.period]
        )
        
    def next(self):
        # EMV berechnen
        emv = self.calculate_emv()
        self.emv_history.append(emv)
        self.lines.emv[0] = emv
        
        # Midpoint speichern
        midpoint = (
            self.data.high[0] +
            self.data.low[0]
        ) / 2
        self.midpoint_history.append(midpoint)
        
        # Geglätteter EMV
        if len(self.emv_history) >= self.p.smooth_period:
            self.lines.smoothed_emv[0] = np.mean(
                self.emv_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_emv[0] = emv
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Signal
        if (self.lines.emv[0] > 0 and
            self.lines.trend_strength[0] > 0 and
            self.lines.momentum[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.emv[0] < 0 and
              self.lines.trend_strength[0] < 0 and
              self.lines.momentum[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.emv_history,
                    self.midpoint_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'emv': {
                'value': self.lines.emv[0],
                'smoothed': self.lines.smoothed_emv[0],
                'trend': (
                    'increasing'
                    if self.lines.emv[0] >
                       self.lines.smoothed_emv[0]
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
            'momentum': {
                'value': self.lines.momentum[0],
                'direction': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.momentum[0])
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
                    abs(self.lines.momentum[0])
                    if abs(self.lines.momentum[0]) <= 1
                    else abs(self.lines.trend_strength[0])
                )
            },
            'market_state': {
                'ease_of_movement': (
                    'high' if self.lines.emv[0] > 0.5
                    else 'low' if self.lines.emv[0] < -0.5
                    else 'normal'
                ),
                'trend_confirmation': (
                    'confirmed'
                    if (self.lines.trend_strength[0] > 0 and
                        self.lines.momentum[0] > 0) or
                       (self.lines.trend_strength[0] < 0 and
                        self.lines.momentum[0] < 0)
                    else 'divergent'
                ),
                'movement_quality': (
                    'efficient'
                    if abs(self.lines.emv[0]) > 0.7
                    else 'inefficient'
                )
            }
        }
