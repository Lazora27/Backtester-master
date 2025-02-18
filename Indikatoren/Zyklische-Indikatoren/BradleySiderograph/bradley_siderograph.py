import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class BradleySiderograph(bt.Indicator):
    """
    Bradley Siderograph Indicator
    
    Ein zyklischer Indikator, der planetare Zyklen verwendet,
    um potenzielle Wendepunkte im Markt zu identifizieren.
    
    Features:
    - Planetare Zyklusanalyse
    - Trendwendepunktberechnung
    - Zyklische Musteranalyse
    - Signalgenerierung
    
    Parameter:
    - period (360): Analysezeitraum (Tage)
    - cycle_weight (0.5): Gewichtung der Zyklen
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('siderograph', 'smoothed_sid',
             'cycle_strength', 'turning_points',
             'signal')
             
    params = (
        ('period', 360),
        ('cycle_weight', 0.5),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        siderograph=dict(color='blue', _name='Siderograph'),
        smoothed_sid=dict(color='red', _name='Smoothed Siderograph'),
        cycle_strength=dict(color='green', _name='Cycle Strength'),
        turning_points=dict(color='purple', _name='Turning Points'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(BradleySiderograph, self).__init__()
        
        # Historie
        self.sid_history = []
        self.date_history = []
        
    def calculate_planetary_cycle(self, days):
        """
        Berechnet den planetaren Zyklus.
        """
        # Vereinfachte Implementierung der planetaren Zyklen
        jupiter_cycle = np.sin(2 * np.pi * days / 4333)  # ~11.86 Jahre
        saturn_cycle = np.sin(2 * np.pi * days / 10759)  # ~29.46 Jahre
        uranus_cycle = np.sin(2 * np.pi * days / 30687)  # ~84.01 Jahre
        
        return (
            jupiter_cycle * 0.4 +
            saturn_cycle * 0.35 +
            uranus_cycle * 0.25
        )
        
    def calculate_siderograph(self):
        """
        Berechnet den Siderograph-Wert.
        """
        if not self.date_history:
            return 0
            
        days_since_start = (
            self.date_history[-1] -
            self.date_history[0]
        ).days
        
        cycle_value = self.calculate_planetary_cycle(
            days_since_start
        )
        
        return cycle_value * self.p.cycle_weight
        
    def calculate_cycle_strength(self):
        """
        Berechnet die Zyklusstärke.
        """
        if len(self.sid_history) < 2:
            return 0
            
        return (
            self.sid_history[-1] -
            self.sid_history[-2]
        )
        
    def detect_turning_points(self):
        """
        Erkennt Wendepunkte im Zyklus.
        """
        if len(self.sid_history) < 3:
            return 0
            
        # Lokale Maxima und Minima
        if (self.sid_history[-2] > self.sid_history[-1] and
            self.sid_history[-2] > self.sid_history[-3]):
            return 1  # Lokales Maximum
        elif (self.sid_history[-2] < self.sid_history[-1] and
              self.sid_history[-2] < self.sid_history[-3]):
            return -1  # Lokales Minimum
            
        return 0
        
    def next(self):
        # Datum speichern
        current_date = self.data.datetime.date()
        self.date_history.append(current_date)
        
        # Siderograph berechnen
        sid = self.calculate_siderograph()
        self.sid_history.append(sid)
        self.lines.siderograph[0] = sid
        
        # Geglätteter Siderograph
        if len(self.sid_history) >= self.p.smooth_period:
            self.lines.smoothed_sid[0] = np.mean(
                self.sid_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_sid[0] = sid
            
        # Zyklusstärke
        self.lines.cycle_strength[0] = self.calculate_cycle_strength()
        
        # Wendepunkte
        self.lines.turning_points[0] = self.detect_turning_points()
        
        # Signal
        if self.lines.turning_points[0] != 0:
            if (self.lines.turning_points[0] > 0 and
                self.lines.cycle_strength[0] < 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.lines.turning_points[0] < 0 and
                  self.lines.cycle_strength[0] > 0):
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
        for hist in [self.sid_history,
                    self.date_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'siderograph': {
                'value': self.lines.siderograph[0],
                'smoothed': self.lines.smoothed_sid[0],
                'trend': (
                    'rising'
                    if self.lines.siderograph[0] >
                       self.lines.smoothed_sid[0]
                    else 'falling'
                )
            },
            'cycle': {
                'strength': self.lines.cycle_strength[0],
                'direction': (
                    'up' if self.lines.cycle_strength[0] > 0
                    else 'down'
                ),
                'phase': (
                    'peak' if self.lines.turning_points[0] > 0
                    else 'trough'
                    if self.lines.turning_points[0] < 0
                    else 'transition'
                )
            },
            'turning_points': {
                'current': self.lines.turning_points[0],
                'type': (
                    'maximum'
                    if self.lines.turning_points[0] > 0
                    else 'minimum'
                    if self.lines.turning_points[0] < 0
                    else 'none'
                ),
                'significance': (
                    abs(self.lines.cycle_strength[0])
                    if abs(self.lines.cycle_strength[0]) <= 1
                    else 1
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
                    abs(self.lines.turning_points[0]) *
                    abs(self.lines.cycle_strength[0])
                    if abs(self.lines.cycle_strength[0]) <= 1
                    else abs(self.lines.turning_points[0])
                )
            },
            'market_state': {
                'cycle_position': (
                    'top' if self.lines.siderograph[0] > 0.7
                    else 'bottom'
                    if self.lines.siderograph[0] < -0.7
                    else 'middle'
                ),
                'trend_alignment': (
                    'aligned'
                    if (self.lines.cycle_strength[0] > 0 and
                        self.lines.siderograph[0] > 0) or
                       (self.lines.cycle_strength[0] < 0 and
                        self.lines.siderograph[0] < 0)
                    else 'divergent'
                ),
                'cycle_quality': (
                    'strong'
                    if abs(self.lines.cycle_strength[0]) > 0.7
                    else 'weak'
                )
            }
        }
