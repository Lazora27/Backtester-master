import backtrader as bt
import numpy as np
from collections import defaultdict

class PriceDelta(bt.Indicator):
    """
    Price Delta Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    Preisänderungen und deren Auswirkungen.
    
    Features:
    - Delta-Analyse
    - Preis-Impuls
    - Momentum-Berechnung
    - Signalgenerierung
    
    Parameter:
    - delta_period (20): Delta-Berechnungsperiode
    - momentum_threshold (0.2): Momentum-Schwelle
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('price_delta', 'delta_momentum',
             'price_impulse', 'delta_strength',
             'signal')
             
    params = (
        ('delta_period', 20),
        ('momentum_threshold', 0.2),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        price_delta=dict(color='blue', _name='Price Delta'),
        delta_momentum=dict(color='red', _name='Delta Momentum'),
        price_impulse=dict(color='green', _name='Price Impulse'),
        delta_strength=dict(color='purple', _name='Delta Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(PriceDelta, self).__init__()
        
        # Delta Tracking
        self.delta_history = []
        self.price_history = []
        self.volume_history = []
        self.momentum_history = []
        
    def calculate_price_delta(self):
        """
        Berechnet den Preis-Delta.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Preisänderung gewichtet mit Volumen
        price_change = (
            self.price_history[-1] -
            self.price_history[-2]
        )
        volume = self.volume_history[-1]
        
        return price_change * volume
        
    def calculate_delta_momentum(self):
        """
        Berechnet das Delta-Momentum.
        """
        if len(self.delta_history) < self.p.smooth_period:
            return 0
            
        recent_deltas = self.delta_history[
            -self.p.smooth_period:
        ]
        
        # Gewichtetes Momentum
        weights = np.linspace(1, 2, len(recent_deltas))
        momentum = sum(
            w * d for w, d in zip(weights, recent_deltas)
        )
        
        return momentum / sum(weights)
        
    def calculate_price_impulse(self):
        """
        Berechnet den Preis-Impuls.
        """
        if len(self.price_history) < self.p.delta_period:
            return 0
            
        # Impuls über Periode
        start_price = self.price_history[
            -self.p.delta_period
        ]
        end_price = self.price_history[-1]
        
        price_change = end_price - start_price
        volume_sum = sum(
            self.volume_history[-self.p.delta_period:]
        )
        
        if volume_sum == 0:
            return 0
            
        return price_change / volume_sum
        
    def calculate_delta_strength(self):
        """
        Berechnet die Delta-Stärke.
        """
        if len(self.delta_history) < self.p.delta_period:
            return 0
            
        recent_deltas = self.delta_history[
            -self.p.delta_period:
        ]
        
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
        
        # Delta berechnen
        price_delta = self.calculate_price_delta()
        self.delta_history.append(price_delta)
        
        # Weitere Metriken
        delta_momentum = self.calculate_delta_momentum()
        price_impulse = self.calculate_price_impulse()
        delta_strength = self.calculate_delta_strength()
        
        self.momentum_history.append(delta_momentum)
        
        # Linien aktualisieren
        self.lines.price_delta[0] = price_delta
        self.lines.delta_momentum[0] = delta_momentum
        self.lines.price_impulse[0] = price_impulse
        self.lines.delta_strength[0] = delta_strength
        
        # Signal
        if delta_strength > 0.1:
            if (delta_momentum > self.p.momentum_threshold and
                price_impulse > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (delta_momentum < -self.p.momentum_threshold and
                  price_impulse < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.delta_period,
            self.p.smooth_period
        )
        for hist in [self.delta_history,
                    self.price_history,
                    self.volume_history,
                    self.momentum_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'delta': {
                'current': self.lines.price_delta[0],
                'momentum': self.lines.delta_momentum[0],
                'impulse': self.lines.price_impulse[0],
                'strength': self.lines.delta_strength[0]
            },
            'momentum_analysis': {
                'trend': (
                    'bullish'
                    if self.lines.delta_momentum[0] >
                       self.p.momentum_threshold
                    else 'bearish'
                    if self.lines.delta_momentum[0] <
                       -self.p.momentum_threshold
                    else 'neutral'
                ),
                'strength': abs(self.lines.delta_momentum[0]),
                'consistency': (
                    'consistent'
                    if len(self.momentum_history) > 1 and
                    all(m * self.momentum_history[-1] > 0
                        for m in self.momentum_history[-3:])
                    else 'inconsistent'
                )
            },
            'impulse_analysis': {
                'direction': (
                    'up' if self.lines.price_impulse[0] > 0
                    else 'down'
                    if self.lines.price_impulse[0] < 0
                    else 'flat'
                ),
                'magnitude': abs(self.lines.price_impulse[0]),
                'quality': (
                    'strong'
                    if abs(self.lines.price_impulse[0]) > 0.001
                    else 'weak'
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
                    abs(self.lines.delta_momentum[0])
                )
            },
            'market_conditions': {
                'delta_quality': (
                    'high'
                    if self.lines.delta_strength[0] > 0.15
                    else 'low'
                ),
                'momentum_state': (
                    'strong'
                    if abs(self.lines.delta_momentum[0]) >
                       self.p.momentum_threshold
                    else 'weak'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.delta_strength[0] > 0.1 and
                        abs(self.lines.delta_momentum[0]) >
                        self.p.momentum_threshold * 0.8)
                    else 'unfavorable'
                )
            }
        }
