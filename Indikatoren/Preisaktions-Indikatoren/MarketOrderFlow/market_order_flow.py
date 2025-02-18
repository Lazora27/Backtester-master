import backtrader as bt
import numpy as np
from collections import defaultdict

class MarketOrderFlow(bt.Indicator):
    """
    Market Order Flow Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Markt-Order-Flows.
    
    Features:
    - Order Flow Analyse
    - Aggressive Flow Erkennung
    - Flow Imbalance Berechnung
    - Signalgenerierung
    
    Parameter:
    - flow_period (20): Flow-Berechnungsperiode
    - volume_threshold (1000): Volumenschwelle
    - aggression_threshold (0.6): Aggressionsschwelle
    """
    
    lines = ('flow_strength', 'aggression_ratio',
             'flow_imbalance', 'order_momentum',
             'signal')
             
    params = (
        ('flow_period', 20),
        ('volume_threshold', 1000),
        ('aggression_threshold', 0.6)
    )
    
    plotlines = dict(
        flow_strength=dict(color='blue', _name='Flow Strength'),
        aggression_ratio=dict(color='red', _name='Aggression Ratio'),
        flow_imbalance=dict(color='green', _name='Flow Imbalance'),
        order_momentum=dict(color='purple', _name='Order Momentum'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(MarketOrderFlow, self).__init__()
        
        # Flow Tracking
        self.buy_flow = defaultdict(float)
        self.sell_flow = defaultdict(float)
        self.aggressive_flow = []
        self.price_history = []
        
    def update_flow(self, price, volume, is_aggressive):
        """
        Aktualisiert die Flow-Daten.
        """
        time_bucket = len(self.data) // 5
        is_buying = price > self.price_history[-1] if self.price_history else True
        
        if is_buying:
            self.buy_flow[time_bucket] += volume
        else:
            self.sell_flow[time_bucket] += volume
            
        if is_aggressive:
            self.aggressive_flow.append((
                volume,
                1 if is_buying else -1
            ))
            
    def calculate_flow_strength(self):
        """
        Berechnet die Flow-Stärke.
        """
        if not (self.buy_flow and self.sell_flow):
            return 0
            
        recent_buys = sum(
            v for k, v in self.buy_flow.items()
            if k >= len(self.data) // 5 - 4
        )
        recent_sells = sum(
            v for k, v in self.sell_flow.items()
            if k >= len(self.data) // 5 - 4
        )
        
        total_flow = recent_buys + recent_sells
        if total_flow == 0:
            return 0
            
        return (recent_buys - recent_sells) / total_flow
        
    def calculate_aggression_ratio(self):
        """
        Berechnet das Aggressionsverhältnis.
        """
        if not self.aggressive_flow:
            return 0
            
        recent_flow = self.aggressive_flow[
            -self.p.flow_period:
        ]
        
        total_volume = sum(vol for vol, _ in recent_flow)
        if total_volume == 0:
            return 0
            
        weighted_aggression = sum(
            vol * direction
            for vol, direction in recent_flow
        )
        
        return weighted_aggression / total_volume
        
    def calculate_flow_imbalance(self):
        """
        Berechnet das Flow-Ungleichgewicht.
        """
        if not (self.buy_flow and self.sell_flow):
            return 0
            
        current_bucket = len(self.data) // 5
        
        # Kurzfristiges Ungleichgewicht
        short_buys = self.buy_flow.get(
            current_bucket,
            0
        )
        short_sells = self.sell_flow.get(
            current_bucket,
            0
        )
        
        if short_buys + short_sells == 0:
            return 0
            
        return (short_buys - short_sells) / (
            short_buys + short_sells
        )
        
    def calculate_order_momentum(self):
        """
        Berechnet das Order-Momentum.
        """
        if len(self.aggressive_flow) < 2:
            return 0
            
        recent_flow = self.aggressive_flow[
            -self.p.flow_period:
        ]
        
        # Gewichtetes Momentum
        weights = np.linspace(1, 2, len(recent_flow))
        momentum = sum(
            w * vol * direction
            for w, (vol, direction)
            in zip(weights, recent_flow)
        )
        
        return momentum / sum(weights)
        
    def next(self):
        # Preis speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        
        # Flow aktualisieren
        is_aggressive = (
            abs(price - self.price_history[-2]) > 0.001
            if len(self.price_history) > 1
            else False
        )
        self.update_flow(price, volume, is_aggressive)
        
        # Metriken berechnen
        flow_strength = self.calculate_flow_strength()
        aggression_ratio = self.calculate_aggression_ratio()
        flow_imbalance = self.calculate_flow_imbalance()
        order_momentum = self.calculate_order_momentum()
        
        # Linien aktualisieren
        self.lines.flow_strength[0] = flow_strength
        self.lines.aggression_ratio[0] = aggression_ratio
        self.lines.flow_imbalance[0] = flow_imbalance
        self.lines.order_momentum[0] = order_momentum
        
        # Signal
        if abs(flow_strength) > 0.3:
            if (aggression_ratio > self.p.aggression_threshold and
                flow_imbalance > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (aggression_ratio < -self.p.aggression_threshold and
                  flow_imbalance < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.price_history) > self.p.flow_period:
            self.price_history.pop(0)
            
        if len(self.aggressive_flow) > self.p.flow_period:
            self.aggressive_flow.pop(0)
            
        # Flow-Daten periodisch bereinigen
        if len(self.data) % 100 == 0:
            current_bucket = len(self.data) // 5
            self.buy_flow = defaultdict(
                float,
                {k: v for k, v in self.buy_flow.items()
                 if k >= current_bucket - 4}
            )
            self.sell_flow = defaultdict(
                float,
                {k: v for k, v in self.sell_flow.items()
                 if k >= current_bucket - 4}
            )
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'flow': {
                'strength': self.lines.flow_strength[0],
                'aggression': self.lines.aggression_ratio[0],
                'imbalance': self.lines.flow_imbalance[0],
                'momentum': self.lines.order_momentum[0]
            },
            'order_analysis': {
                'aggressive_count': len(self.aggressive_flow),
                'recent_direction': (
                    'buying'
                    if self.lines.flow_strength[0] > 0
                    else 'selling'
                ),
                'aggression_state': (
                    'aggressive'
                    if abs(self.lines.aggression_ratio[0]) >
                       self.p.aggression_threshold
                    else 'passive'
                )
            },
            'flow_characteristics': {
                'type': (
                    'directional'
                    if abs(self.lines.flow_strength[0]) > 0.3
                    else 'choppy'
                ),
                'momentum_quality': (
                    'strong'
                    if abs(self.lines.order_momentum[0]) >
                       self.p.volume_threshold
                    else 'weak'
                ),
                'balance': (
                    'balanced'
                    if abs(self.lines.flow_imbalance[0]) < 0.2
                    else 'imbalanced'
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
                    abs(self.lines.flow_strength[0]) *
                    abs(self.lines.aggression_ratio[0])
                )
            },
            'market_conditions': {
                'flow_quality': (
                    'high'
                    if abs(self.lines.flow_strength[0]) > 0.3
                    else 'low'
                ),
                'aggression_level': (
                    'high'
                    if abs(self.lines.aggression_ratio[0]) >
                       self.p.aggression_threshold
                    else 'low'
                ),
                'trading_environment': (
                    'favorable'
                    if (abs(self.lines.flow_strength[0]) > 0.25 and
                        abs(self.lines.aggression_ratio[0]) >
                        self.p.aggression_threshold * 0.8)
                    else 'unfavorable'
                )
            }
        }
