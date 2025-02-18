import backtrader as bt
import numpy as np
from collections import defaultdict

class OrderFlowCumulativeDelta(bt.Indicator):
    """
    Order Flow Cumulative Delta Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    kumulativen Order Flow Deltas.
    
    Features:
    - Kumulativer Delta
    - Delta Divergenz
    - Flow Impuls
    - Signalgenerierung
    
    Parameter:
    - delta_period (20): Delta-Berechnungsperiode
    - volume_threshold (1000): Volumenschwelle
    - divergence_lookback (5): Divergenz-Rückblick
    """
    
    lines = ('cumulative_delta', 'delta_momentum',
             'flow_divergence', 'delta_strength',
             'signal')
             
    params = (
        ('delta_period', 20),
        ('volume_threshold', 1000),
        ('divergence_lookback', 5)
    )
    
    plotlines = dict(
        cumulative_delta=dict(color='blue', _name='Cumulative Delta'),
        delta_momentum=dict(color='red', _name='Delta Momentum'),
        flow_divergence=dict(color='green', _name='Flow Divergence'),
        delta_strength=dict(color='purple', _name='Delta Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(OrderFlowCumulativeDelta, self).__init__()
        
        # Delta Tracking
        self.delta_history = []
        self.price_history = []
        self.volume_history = []
        self.cumulative_values = []
        
    def calculate_delta(self, price, volume):
        """
        Berechnet den Delta für einen Trade.
        """
        if not self.price_history:
            return volume
            
        # Delta basierend auf Preisänderung
        price_change = price - self.price_history[-1]
        
        if price_change > 0:
            return volume  # Buying pressure
        elif price_change < 0:
            return -volume  # Selling pressure
        return 0
        
    def update_cumulative_delta(self, delta):
        """
        Aktualisiert den kumulativen Delta.
        """
        if not self.cumulative_values:
            self.cumulative_values.append(delta)
        else:
            self.cumulative_values.append(
                self.cumulative_values[-1] + delta
            )
            
    def calculate_delta_momentum(self):
        """
        Berechnet das Delta-Momentum.
        """
        if len(self.delta_history) < 2:
            return 0
            
        recent_deltas = self.delta_history[
            -self.p.delta_period:
        ]
        
        # Gewichtetes Momentum
        weights = np.linspace(1, 2, len(recent_deltas))
        momentum = sum(
            w * d for w, d in zip(weights, recent_deltas)
        )
        
        return momentum / sum(weights)
        
    def detect_flow_divergence(self):
        """
        Erkennt Flow-Divergenzen.
        """
        if (len(self.price_history) <
            self.p.divergence_lookback or
            len(self.cumulative_values) <
            self.p.divergence_lookback):
            return 0
            
        # Preis- und Delta-Trends vergleichen
        price_change = (
            self.price_history[-1] -
            self.price_history[-self.p.divergence_lookback]
        )
        delta_change = (
            self.cumulative_values[-1] -
            self.cumulative_values[-self.p.divergence_lookback]
        )
        
        # Divergenz-Score
        if price_change * delta_change < 0:
            return -np.sign(price_change)
        return 0
        
    def calculate_delta_strength(self):
        """
        Berechnet die Delta-Stärke.
        """
        if not self.delta_history:
            return 0
            
        recent_deltas = self.delta_history[
            -self.p.delta_period:
        ]
        
        if not recent_deltas:
            return 0
            
        # Absolute Stärke
        total_volume = sum(
            self.volume_history[-self.p.delta_period:]
        )
        if total_volume == 0:
            return 0
            
        return abs(sum(recent_deltas)) / total_volume
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Delta berechnen und speichern
        delta = self.calculate_delta(price, volume)
        self.delta_history.append(delta)
        
        # Kumulativen Delta aktualisieren
        self.update_cumulative_delta(delta)
        
        # Metriken berechnen
        delta_momentum = self.calculate_delta_momentum()
        flow_divergence = self.detect_flow_divergence()
        delta_strength = self.calculate_delta_strength()
        
        # Linien aktualisieren
        self.lines.cumulative_delta[0] = (
            self.cumulative_values[-1]
            if self.cumulative_values
            else 0
        )
        self.lines.delta_momentum[0] = delta_momentum
        self.lines.flow_divergence[0] = flow_divergence
        self.lines.delta_strength[0] = delta_strength
        
        # Signal
        if delta_strength > 0.2:
            if (delta_momentum > self.p.volume_threshold and
                flow_divergence >= 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (delta_momentum < -self.p.volume_threshold and
                  flow_divergence <= 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_length = max(
            self.p.delta_period,
            self.p.divergence_lookback
        )
        for hist in [self.delta_history,
                    self.price_history,
                    self.volume_history]:
            if len(hist) > max_length:
                hist.pop(0)
                
        if len(self.cumulative_values) > max_length:
            self.cumulative_values = (
                self.cumulative_values[-max_length:]
            )
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'delta': {
                'current': (
                    self.delta_history[-1]
                    if self.delta_history
                    else 0
                ),
                'cumulative': (
                    self.cumulative_values[-1]
                    if self.cumulative_values
                    else 0
                ),
                'momentum': self.lines.delta_momentum[0],
                'strength': self.lines.delta_strength[0]
            },
            'flow_analysis': {
                'divergence': self.lines.flow_divergence[0],
                'direction': (
                    'accumulation'
                    if self.lines.delta_momentum[0] > 0
                    else 'distribution'
                    if self.lines.delta_momentum[0] < 0
                    else 'neutral'
                ),
                'strength_level': (
                    'strong'
                    if self.lines.delta_strength[0] > 0.3
                    else 'moderate'
                    if self.lines.delta_strength[0] > 0.1
                    else 'weak'
                )
            },
            'divergence_analysis': {
                'state': (
                    'bullish'
                    if self.lines.flow_divergence[0] > 0
                    else 'bearish'
                    if self.lines.flow_divergence[0] < 0
                    else 'none'
                ),
                'significance': (
                    'significant'
                    if abs(self.lines.flow_divergence[0]) > 0.5
                    else 'minor'
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
                    (1 - abs(self.lines.flow_divergence[0]))
                )
            },
            'market_conditions': {
                'delta_quality': (
                    'high'
                    if self.lines.delta_strength[0] > 0.2
                    else 'low'
                ),
                'momentum_state': (
                    'strong'
                    if abs(self.lines.delta_momentum[0]) >
                       self.p.volume_threshold
                    else 'weak'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.delta_strength[0] > 0.15 and
                        abs(self.lines.delta_momentum[0]) >
                        self.p.volume_threshold * 0.8)
                    else 'unfavorable'
                )
            }
        }
