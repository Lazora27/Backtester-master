import backtrader as bt
import numpy as np
from collections import defaultdict

class TapeReading(bt.Indicator):
    """
    Tape Reading Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Markt-Tapes und Handelsflusses.
    
    Features:
    - Tape-Analyse
    - Handelsfluss-Erkennung
    - Momentum-Berechnung
    - Signalgenerierung
    
    Parameter:
    - tape_period (20): Tape-Analyseperiode
    - flow_threshold (0.6): Flussschwelle
    - momentum_length (5): Momentumlänge
    """
    
    lines = ('tape_flow', 'trade_momentum',
             'flow_strength', 'tape_quality',
             'signal')
             
    params = (
        ('tape_period', 20),
        ('flow_threshold', 0.6),
        ('momentum_length', 5)
    )
    
    plotlines = dict(
        tape_flow=dict(color='blue', _name='Tape Flow'),
        trade_momentum=dict(color='red', _name='Trade Momentum'),
        flow_strength=dict(color='green', _name='Flow Strength'),
        tape_quality=dict(color='purple', _name='Tape Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TapeReading, self).__init__()
        
        # Tape Tracking
        self.price_history = []
        self.volume_history = []
        self.trade_history = []
        self.flow_history = []
        self.momentum_history = []
        
    def analyze_tape_flow(self):
        """
        Analysiert den Tape-Fluss.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Fluss basierend auf Preis und Volumen
        price_changes = np.diff(
            self.price_history[-self.p.tape_period:]
        )
        volumes = self.volume_history[-self.p.tape_period + 1:]
        
        flow = sum(
            p * v for p, v in zip(price_changes, volumes)
        )
        
        self.flow_history.append(flow)
        return flow
        
    def calculate_trade_momentum(self):
        """
        Berechnet das Handelsmomentum.
        """
        if len(self.flow_history) < self.p.momentum_length:
            return 0
            
        # Momentum über Flusswerte
        recent_flow = self.flow_history[-self.p.momentum_length:]
        weights = np.linspace(1, 2, len(recent_flow))
        
        momentum = sum(
            w * f for w, f in zip(weights, recent_flow)
        )
        
        self.momentum_history.append(momentum)
        return momentum / sum(weights)
        
    def calculate_flow_strength(self):
        """
        Berechnet die Flussstärke.
        """
        if len(self.flow_history) < self.p.tape_period:
            return 0
            
        # Stärke basierend auf Flusshistorie
        recent_flow = self.flow_history[-self.p.tape_period:]
        total_volume = sum(
            self.volume_history[-self.p.tape_period:]
        )
        
        if total_volume == 0:
            return 0
            
        return abs(sum(recent_flow)) / total_volume
        
    def analyze_tape_quality(self):
        """
        Analysiert die Tape-Qualität.
        """
        if len(self.price_history) < self.p.tape_period:
            return 0
            
        # Qualität basierend auf Preiskontinuität
        prices = np.array(
            self.price_history[-self.p.tape_period:]
        )
        returns = np.diff(prices) / prices[:-1]
        
        # Kontinuitätsmaß
        continuity = 1 - np.std(returns)
        volume_consistency = 1 - (
            np.std(self.volume_history[-self.p.tape_period:]) /
            np.mean(self.volume_history[-self.p.tape_period:])
        )
        
        return (continuity + volume_consistency) / 2
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Tape-Metriken berechnen
        tape_flow = self.analyze_tape_flow()
        trade_momentum = self.calculate_trade_momentum()
        flow_strength = self.calculate_flow_strength()
        tape_quality = self.analyze_tape_quality()
        
        # Trade aufzeichnen
        self.trade_history.append({
            'price': price,
            'volume': volume,
            'flow': tape_flow,
            'momentum': trade_momentum
        })
        
        # Linien aktualisieren
        self.lines.tape_flow[0] = tape_flow
        self.lines.trade_momentum[0] = trade_momentum
        self.lines.flow_strength[0] = flow_strength
        self.lines.tape_quality[0] = tape_quality
        
        # Signal
        if flow_strength > self.p.flow_threshold:
            if (trade_momentum > 0 and
                tape_quality > 0.5):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (trade_momentum < 0 and
                  tape_quality > 0.5):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.tape_period,
            self.p.momentum_length
        )
        for hist in [self.price_history,
                    self.volume_history,
                    self.flow_history,
                    self.momentum_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        if len(self.trade_history) > max_period:
            self.trade_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'tape_metrics': {
                'flow': self.lines.tape_flow[0],
                'momentum': self.lines.trade_momentum[0],
                'strength': self.lines.flow_strength[0],
                'quality': self.lines.tape_quality[0]
            },
            'flow_analysis': {
                'direction': (
                    'bullish'
                    if self.lines.tape_flow[0] > 0
                    else 'bearish'
                    if self.lines.tape_flow[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.tape_flow[0]),
                'consistency': (
                    'consistent'
                    if len(self.flow_history) > 1 and
                    all(f * self.flow_history[-1] > 0
                        for f in self.flow_history[-3:])
                    else 'inconsistent'
                )
            },
            'momentum_analysis': {
                'state': (
                    'accelerating'
                    if len(self.momentum_history) > 1 and
                    abs(self.momentum_history[-1]) >
                    abs(self.momentum_history[-2])
                    else 'decelerating'
                ),
                'strength': abs(self.lines.trade_momentum[0]),
                'quality': (
                    'high'
                    if self.lines.tape_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.tape_quality[0] > 0.4
                    else 'low'
                )
            },
            'trade_analysis': {
                'recent_trades': len(self.trade_history),
                'volume_profile': {
                    'average': np.mean(
                        [t['volume'] for t in self.trade_history]
                    ),
                    'trend': (
                        'increasing'
                        if len(self.volume_history) > 1 and
                        self.volume_history[-1] >
                        self.volume_history[-2]
                        else 'decreasing'
                    )
                }
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    self.lines.flow_strength[0] *
                    self.lines.tape_quality[0]
                )
            },
            'market_conditions': {
                'tape_quality': (
                    'high'
                    if self.lines.tape_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.tape_quality[0] > 0.4
                    else 'low'
                ),
                'flow_quality': (
                    'strong'
                    if self.lines.flow_strength[0] >
                       self.p.flow_threshold
                    else 'weak'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.flow_strength[0] >
                        self.p.flow_threshold and
                        self.lines.tape_quality[0] > 0.5)
                    else 'unfavorable'
                )
            }
        }
