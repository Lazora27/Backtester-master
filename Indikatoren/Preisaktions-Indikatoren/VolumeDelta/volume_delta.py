import backtrader as bt
import numpy as np
from collections import defaultdict

class VolumeDelta(bt.Indicator):
    """
    Volume Delta Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    Volumendifferenzen und -flüsse.
    
    Features:
    - Volumendelta-Analyse
    - Flussberechnung
    - Deltacluster
    - Signalgenerierung
    
    Parameter:
    - delta_period (20): Delta-Berechnungsperiode
    - flow_threshold (0.6): Flussschwelle
    - cluster_size (5): Clustergröße
    """
    
    lines = ('volume_delta', 'delta_flow',
             'delta_cluster', 'delta_strength',
             'signal')
             
    params = (
        ('delta_period', 20),
        ('flow_threshold', 0.6),
        ('cluster_size', 5)
    )
    
    plotlines = dict(
        volume_delta=dict(color='blue', _name='Volume Delta'),
        delta_flow=dict(color='red', _name='Delta Flow'),
        delta_cluster=dict(color='green', _name='Delta Cluster'),
        delta_strength=dict(color='purple', _name='Delta Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(VolumeDelta, self).__init__()
        
        # Delta Tracking
        self.volume_history = []
        self.price_history = []
        self.delta_history = []
        self.flow_history = []
        
    def calculate_volume_delta(self):
        """
        Berechnet das Volumendelta.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Delta basierend auf Preis und Volumen
        price_change = (
            self.price_history[-1] -
            self.price_history[-2]
        )
        volume = self.volume_history[-1]
        
        delta = price_change * volume
        self.delta_history.append(delta)
        
        return delta
        
    def calculate_delta_flow(self):
        """
        Berechnet den Deltafluss.
        """
        if len(self.delta_history) < self.p.cluster_size:
            return 0
            
        # Fluss über Deltahistorie
        recent_delta = self.delta_history[
            -self.p.cluster_size:
        ]
        
        if not recent_delta:
            return 0
            
        # Gewichteter Fluss
        weights = np.linspace(1, 2, len(recent_delta))
        flow = sum(
            w * d for w, d in zip(weights, recent_delta)
        )
        
        self.flow_history.append(flow)
        return flow / sum(weights)
        
    def detect_delta_cluster(self):
        """
        Erkennt Deltacluster.
        """
        if len(self.delta_history) < self.p.cluster_size:
            return 0
            
        # Cluster über Deltahistorie
        recent_delta = self.delta_history[
            -self.p.cluster_size:
        ]
        
        if not recent_delta:
            return 0
            
        # Clusterstärke
        avg_delta = np.mean(recent_delta)
        cluster_strength = sum(
            1 for d in recent_delta
            if abs(d) > abs(avg_delta) * self.p.flow_threshold
        )
        
        return cluster_strength / self.p.cluster_size
        
    def calculate_delta_strength(self):
        """
        Berechnet die Deltastärke.
        """
        if len(self.delta_history) < self.p.delta_period:
            return 0
            
        recent_delta = self.delta_history[
            -self.p.delta_period:
        ]
        
        if not recent_delta:
            return 0
            
        total_volume = sum(
            self.volume_history[-self.p.delta_period:]
        )
        if total_volume == 0:
            return 0
            
        return abs(sum(recent_delta)) / total_volume
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Delta-Metriken berechnen
        volume_delta = self.calculate_volume_delta()
        delta_flow = self.calculate_delta_flow()
        delta_cluster = self.detect_delta_cluster()
        delta_strength = self.calculate_delta_strength()
        
        # Linien aktualisieren
        self.lines.volume_delta[0] = volume_delta
        self.lines.delta_flow[0] = delta_flow
        self.lines.delta_cluster[0] = delta_cluster
        self.lines.delta_strength[0] = delta_strength
        
        # Signal
        if delta_strength > self.p.flow_threshold:
            if (delta_flow > 0 and
                delta_cluster > 0.6):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (delta_flow < 0 and
                  delta_cluster > 0.6):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.delta_period,
            self.p.cluster_size
        )
        for hist in [self.price_history,
                    self.volume_history,
                    self.delta_history,
                    self.flow_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'delta_metrics': {
                'volume_delta': self.lines.volume_delta[0],
                'flow': self.lines.delta_flow[0],
                'cluster': self.lines.delta_cluster[0],
                'strength': self.lines.delta_strength[0]
            },
            'flow_analysis': {
                'direction': (
                    'bullish'
                    if self.lines.delta_flow[0] > 0
                    else 'bearish'
                    if self.lines.delta_flow[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.delta_flow[0]),
                'consistency': (
                    'consistent'
                    if len(self.flow_history) > 1 and
                    all(f * self.flow_history[-1] > 0
                        for f in self.flow_history[-3:])
                    else 'inconsistent'
                )
            },
            'cluster_analysis': {
                'strength': self.lines.delta_cluster[0],
                'quality': (
                    'high'
                    if self.lines.delta_cluster[0] > 0.7
                    else 'moderate'
                    if self.lines.delta_cluster[0] > 0.4
                    else 'low'
                ),
                'trend': (
                    'forming'
                    if self.lines.delta_cluster[0] >
                       self.p.flow_threshold
                    else 'dissolving'
                )
            },
            'delta_analysis': {
                'type': (
                    'accumulation'
                    if self.lines.delta_flow[0] > 0 and
                    self.lines.delta_cluster[0] > 0.6
                    else 'distribution'
                    if self.lines.delta_flow[0] < 0 and
                    self.lines.delta_cluster[0] > 0.6
                    else 'neutral'
                ),
                'strength': self.lines.delta_strength[0],
                'reliability': (
                    self.lines.delta_cluster[0] *
                    abs(self.lines.delta_flow[0])
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
                    self.lines.delta_strength[0] *
                    self.lines.delta_cluster[0]
                )
            },
            'market_conditions': {
                'delta_quality': (
                    'high'
                    if self.lines.delta_strength[0] >
                       self.p.flow_threshold * 1.2
                    else 'moderate'
                    if self.lines.delta_strength[0] >
                       self.p.flow_threshold
                    else 'low'
                ),
                'cluster_clarity': (
                    'clear'
                    if self.lines.delta_cluster[0] > 0.6
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.delta_strength[0] >
                        self.p.flow_threshold and
                        self.lines.delta_cluster[0] > 0.6)
                    else 'unfavorable'
                )
            }
        }
