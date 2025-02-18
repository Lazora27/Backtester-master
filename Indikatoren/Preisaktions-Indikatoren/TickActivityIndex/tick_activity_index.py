import backtrader as bt
import numpy as np
from collections import defaultdict

class TickActivityIndex(bt.Indicator):
    """
    Tick Activity Index
    
    Ein fortgeschrittener Indikator zur Analyse der
    Tick-Aktivität und Marktdynamik.
    
    Features:
    - Tick-Aktivitätsanalyse
    - Impulsberechnung
    - Aktivitätsmuster
    - Signalgenerierung
    
    Parameter:
    - activity_period (20): Aktivitätsperiode
    - impulse_threshold (0.6): Impulsschwelle
    - pattern_length (5): Musterlänge
    """
    
    lines = ('tick_activity', 'tick_impulse',
             'activity_pattern', 'activity_strength',
             'signal')
             
    params = (
        ('activity_period', 20),
        ('impulse_threshold', 0.6),
        ('pattern_length', 5)
    )
    
    plotlines = dict(
        tick_activity=dict(color='blue', _name='Tick Activity'),
        tick_impulse=dict(color='red', _name='Tick Impulse'),
        activity_pattern=dict(color='green', _name='Activity Pattern'),
        activity_strength=dict(color='purple', _name='Activity Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TickActivityIndex, self).__init__()
        
        # Aktivitäts-Tracking
        self.tick_history = []
        self.price_history = []
        self.activity_history = []
        self.impulse_history = []
        
    def calculate_tick_activity(self):
        """
        Berechnet die Tick-Aktivität.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Aktivität basierend auf Preisänderungen
        price_changes = np.diff(
            self.price_history[-self.p.activity_period:]
        )
        
        activity = np.sum(np.abs(price_changes))
        self.activity_history.append(activity)
        
        return activity
        
    def calculate_tick_impulse(self):
        """
        Berechnet den Tick-Impuls.
        """
        if len(self.activity_history) < self.p.pattern_length:
            return 0
            
        # Impuls über Aktivitätswerte
        recent_activity = self.activity_history[
            -self.p.pattern_length:
        ]
        weights = np.linspace(1, 2, len(recent_activity))
        
        impulse = sum(
            w * a for w, a in zip(weights, recent_activity)
        )
        
        self.impulse_history.append(impulse)
        return impulse / sum(weights)
        
    def detect_activity_pattern(self):
        """
        Erkennt Aktivitätsmuster.
        """
        if len(self.activity_history) < self.p.pattern_length:
            return 0
            
        # Muster in der Aktivität
        pattern = np.diff(
            self.activity_history[-self.p.pattern_length:]
        )
        pattern = np.sign(pattern)
        
        # Musterstärke berechnen
        consecutive = 0
        max_consecutive = 0
        current_sign = pattern[0]
        
        for sign in pattern:
            if sign == current_sign:
                consecutive += 1
                max_consecutive = max(
                    max_consecutive,
                    consecutive
                )
            else:
                consecutive = 1
                current_sign = sign
                
        return max_consecutive / len(pattern)
        
    def calculate_activity_strength(self):
        """
        Berechnet die Aktivitätsstärke.
        """
        if len(self.activity_history) < self.p.activity_period:
            return 0
            
        recent_activity = self.activity_history[
            -self.p.activity_period:
        ]
        
        if not recent_activity:
            return 0
            
        avg_activity = np.mean(recent_activity)
        if avg_activity == 0:
            return 0
            
        current_activity = recent_activity[-1]
        return current_activity / avg_activity
        
    def next(self):
        # Preis speichern
        price = self.data.close[0]
        self.price_history.append(price)
        
        # Tick-Metriken berechnen
        tick_activity = self.calculate_tick_activity()
        tick_impulse = self.calculate_tick_impulse()
        activity_pattern = self.detect_activity_pattern()
        activity_strength = self.calculate_activity_strength()
        
        # Tick aufzeichnen
        self.tick_history.append({
            'price': price,
            'activity': tick_activity,
            'impulse': tick_impulse,
            'pattern': activity_pattern
        })
        
        # Linien aktualisieren
        self.lines.tick_activity[0] = tick_activity
        self.lines.tick_impulse[0] = tick_impulse
        self.lines.activity_pattern[0] = activity_pattern
        self.lines.activity_strength[0] = activity_strength
        
        # Signal
        if activity_strength > 1.0:
            if (tick_impulse > self.p.impulse_threshold and
                activity_pattern > 0.6):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (tick_impulse < -self.p.impulse_threshold and
                  activity_pattern > 0.6):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.activity_period,
            self.p.pattern_length
        )
        for hist in [self.price_history,
                    self.activity_history,
                    self.impulse_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        if len(self.tick_history) > max_period:
            self.tick_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'tick_metrics': {
                'activity': self.lines.tick_activity[0],
                'impulse': self.lines.tick_impulse[0],
                'pattern': self.lines.activity_pattern[0],
                'strength': self.lines.activity_strength[0]
            },
            'activity_analysis': {
                'state': (
                    'high'
                    if self.lines.tick_activity[0] >
                       np.mean(self.activity_history) * 1.2
                    else 'normal'
                    if self.lines.tick_activity[0] >
                       np.mean(self.activity_history) * 0.8
                    else 'low'
                ),
                'trend': (
                    'increasing'
                    if len(self.activity_history) > 1 and
                    self.activity_history[-1] >
                    self.activity_history[-2]
                    else 'decreasing'
                ),
                'consistency': (
                    'consistent'
                    if self.lines.activity_pattern[0] > 0.7
                    else 'inconsistent'
                )
            },
            'impulse_analysis': {
                'direction': (
                    'bullish'
                    if self.lines.tick_impulse[0] > 0
                    else 'bearish'
                    if self.lines.tick_impulse[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.tick_impulse[0]),
                'quality': (
                    'high'
                    if abs(self.lines.tick_impulse[0]) >
                       self.p.impulse_threshold
                    else 'low'
                )
            },
            'pattern_analysis': {
                'type': (
                    'trending'
                    if self.lines.activity_pattern[0] > 0.7
                    else 'ranging'
                    if self.lines.activity_pattern[0] > 0.4
                    else 'choppy'
                ),
                'strength': self.lines.activity_pattern[0],
                'reliability': (
                    'high'
                    if self.lines.activity_strength[0] > 1.2
                    else 'moderate'
                    if self.lines.activity_strength[0] > 0.8
                    else 'low'
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
                    self.lines.activity_strength[0] *
                    self.lines.activity_pattern[0]
                )
            },
            'market_conditions': {
                'activity_quality': (
                    'high'
                    if self.lines.activity_strength[0] > 1.2
                    else 'moderate'
                    if self.lines.activity_strength[0] > 0.8
                    else 'low'
                ),
                'pattern_quality': (
                    'clear'
                    if self.lines.activity_pattern[0] > 0.6
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.activity_strength[0] > 1.0 and
                        self.lines.activity_pattern[0] > 0.6)
                    else 'unfavorable'
                )
            }
        }
