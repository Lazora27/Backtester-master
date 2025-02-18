import backtrader as bt
import numpy as np
from collections import defaultdict
from datetime import datetime, timedelta

class TimeSalesVolume(bt.Indicator):
    """
    Time & Sales Volume Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Handelsvolumens über Zeit.
    
    Features:
    - Volumenanalyse über Zeit
    - Zeitbasierte Muster
    - Volumencluster
    - Signalgenerierung
    
    Parameter:
    - time_window (20): Zeitfenster in Perioden
    - volume_threshold (0.7): Volumenschwelle
    - cluster_size (5): Clustergröße
    """
    
    lines = ('time_volume', 'volume_cluster',
             'time_pattern', 'volume_intensity',
             'signal')
             
    params = (
        ('time_window', 20),
        ('volume_threshold', 0.7),
        ('cluster_size', 5)
    )
    
    plotlines = dict(
        time_volume=dict(color='blue', _name='Time Volume'),
        volume_cluster=dict(color='red', _name='Volume Cluster'),
        time_pattern=dict(color='green', _name='Time Pattern'),
        volume_intensity=dict(color='purple', _name='Volume Intensity'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TimeSalesVolume, self).__init__()
        
        # Volumen-Tracking
        self.volume_history = []
        self.time_history = []
        self.cluster_history = []
        self.pattern_history = []
        
    def analyze_time_volume(self):
        """
        Analysiert das Volumen über Zeit.
        """
        if len(self.volume_history) < 2:
            return 0
            
        # Volumen im Zeitfenster
        recent_volume = self.volume_history[
            -self.p.time_window:
        ]
        
        if not recent_volume:
            return 0
            
        # Gewichtetes Volumen
        weights = np.linspace(1, 2, len(recent_volume))
        weighted_volume = sum(
            w * v for w, v in zip(weights, recent_volume)
        )
        
        return weighted_volume / sum(weights)
        
    def detect_volume_cluster(self):
        """
        Erkennt Volumencluster.
        """
        if len(self.volume_history) < self.p.cluster_size:
            return 0
            
        # Cluster über Zeitfenster
        recent_volume = self.volume_history[
            -self.p.cluster_size:
        ]
        
        if not recent_volume:
            return 0
            
        avg_volume = np.mean(recent_volume)
        cluster_strength = sum(
            1 for v in recent_volume
            if v > avg_volume * self.p.volume_threshold
        )
        
        self.cluster_history.append(cluster_strength)
        return cluster_strength / self.p.cluster_size
        
    def analyze_time_pattern(self):
        """
        Analysiert zeitbasierte Muster.
        """
        if len(self.volume_history) < self.p.time_window:
            return 0
            
        # Muster im Volumen
        volume_changes = np.diff(
            self.volume_history[-self.p.time_window:]
        )
        pattern = np.sign(volume_changes)
        
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
                
        self.pattern_history.append(max_consecutive)
        return max_consecutive / len(pattern)
        
    def calculate_volume_intensity(self):
        """
        Berechnet die Volumenintensität.
        """
        if len(self.volume_history) < self.p.time_window:
            return 0
            
        recent_volume = self.volume_history[
            -self.p.time_window:
        ]
        
        if not recent_volume:
            return 0
            
        avg_volume = np.mean(recent_volume)
        if avg_volume == 0:
            return 0
            
        current_volume = recent_volume[-1]
        return current_volume / avg_volume
        
    def next(self):
        # Volumen und Zeit speichern
        volume = self.data.volume[0]
        current_time = len(self.data)
        
        self.volume_history.append(volume)
        self.time_history.append(current_time)
        
        # Volumen-Metriken berechnen
        time_volume = self.analyze_time_volume()
        volume_cluster = self.detect_volume_cluster()
        time_pattern = self.analyze_time_pattern()
        volume_intensity = self.calculate_volume_intensity()
        
        # Linien aktualisieren
        self.lines.time_volume[0] = time_volume
        self.lines.volume_cluster[0] = volume_cluster
        self.lines.time_pattern[0] = time_pattern
        self.lines.volume_intensity[0] = volume_intensity
        
        # Signal
        if volume_intensity > 1.2:
            if (volume_cluster > self.p.volume_threshold and
                time_pattern > 0.6):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (volume_cluster < self.p.volume_threshold and
                  time_pattern > 0.6):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.time_window,
            self.p.cluster_size
        )
        for hist in [self.volume_history,
                    self.time_history,
                    self.cluster_history,
                    self.pattern_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volume_metrics': {
                'time_volume': self.lines.time_volume[0],
                'cluster': self.lines.volume_cluster[0],
                'pattern': self.lines.time_pattern[0],
                'intensity': self.lines.volume_intensity[0]
            },
            'time_analysis': {
                'period_count': len(self.time_history),
                'volume_distribution': (
                    'clustered'
                    if self.lines.volume_cluster[0] >
                       self.p.volume_threshold
                    else 'dispersed'
                ),
                'pattern_quality': (
                    'high'
                    if self.lines.time_pattern[0] > 0.7
                    else 'moderate'
                    if self.lines.time_pattern[0] > 0.4
                    else 'low'
                )
            },
            'cluster_analysis': {
                'strength': self.lines.volume_cluster[0],
                'consistency': (
                    'consistent'
                    if len(self.cluster_history) > 1 and
                    all(c > self.p.volume_threshold
                        for c in self.cluster_history[-3:])
                    else 'inconsistent'
                ),
                'trend': (
                    'forming'
                    if self.lines.volume_cluster[0] >
                       self.p.volume_threshold
                    else 'dissolving'
                )
            },
            'pattern_analysis': {
                'type': (
                    'accumulation'
                    if self.lines.time_pattern[0] > 0.7 and
                    self.lines.volume_intensity[0] > 1.2
                    else 'distribution'
                    if self.lines.time_pattern[0] > 0.7 and
                    self.lines.volume_intensity[0] < 0.8
                    else 'neutral'
                ),
                'strength': self.lines.time_pattern[0],
                'reliability': (
                    self.lines.volume_cluster[0] *
                    self.lines.time_pattern[0]
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
                    self.lines.volume_intensity[0] *
                    self.lines.volume_cluster[0]
                )
            },
            'market_conditions': {
                'volume_quality': (
                    'high'
                    if self.lines.volume_intensity[0] > 1.2
                    else 'moderate'
                    if self.lines.volume_intensity[0] > 0.8
                    else 'low'
                ),
                'pattern_clarity': (
                    'clear'
                    if self.lines.time_pattern[0] > 0.6
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.volume_intensity[0] > 1.2 and
                        self.lines.volume_cluster[0] >
                        self.p.volume_threshold)
                    else 'unfavorable'
                )
            }
        }
