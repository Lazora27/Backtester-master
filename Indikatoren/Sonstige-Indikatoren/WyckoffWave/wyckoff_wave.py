import backtrader as bt
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional

class WaveType(Enum):
    """Wyckoff Wave Typen"""
    THRUST = "Thrust"
    REACTION = "Reaction"
    NEUTRAL = "Neutral"

class TrendPhase(Enum):
    """Trend Phasen"""
    ACCUMULATION = "Accumulation"
    MARKUP = "Markup"
    DISTRIBUTION = "Distribution"
    MARKDOWN = "Markdown"
    NEUTRAL = "Neutral"

@dataclass
class WavePoint:
    """Repräsentiert einen Punkt in der Wyckoff Wave"""
    price: float
    volume: float
    time: int
    wave_type: WaveType
    strength: float

class WyckoffWaveIndicator(bt.Indicator):
    """
    Wyckoff Wave Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    Wyckoff Waves und deren Charakteristiken.
    
    Features:
    - Wave-Identifikation
    - Trend-Analyse
    - Volumenanalyse
    - Wellenstärke-Berechnung
    
    Parameter:
    - wave_threshold (0.02): Wellenschwelle
    - volume_factor (1.5): Volumenfaktor
    - lookback (20): Rückblickperiode
    """
    
    lines = ('wave_type', 'trend_phase', 'strength',
             'momentum')
    params = (
        ('wave_threshold', 0.02),
        ('volume_factor', 1.5),
        ('lookback', 20),
    )
    
    plotlines = dict(
        wave_type=dict(color='blue', _name='Wave'),
        trend_phase=dict(color='red', _name='Trend'),
        strength=dict(color='green', _name='Strength'),
        momentum=dict(color='purple', _name='Momentum')
    )
    
    def __init__(self):
        super(WyckoffWaveIndicator, self).__init__()
        
        # Wave-Punkte
        self.wave_points: List[WavePoint] = []
        
        # Preispuffer
        self.price_buffer = []
        self.volume_buffer = []
        
        # Trend-Analyse
        self.current_trend = TrendPhase.NEUTRAL
        self.trend_data = {}
        
        # Momentum-Daten
        self.momentum_data = []
        
    def identify_wave(self, current_price: float,
                     prev_price: float) -> WaveType:
        """Identifiziert den Wave-Typ"""
        if len(self.price_buffer) < 2:
            return WaveType.NEUTRAL
            
        price_change = (current_price - prev_price) / prev_price
        
        if abs(price_change) < self.p.wave_threshold:
            return WaveType.NEUTRAL
        elif price_change > 0:
            return WaveType.THRUST
        else:
            return WaveType.REACTION
            
    def calculate_wave_strength(self, wave_type: WaveType,
                              price_change: float,
                              volume: float) -> float:
        """Berechnet die Wellenstärke"""
        if wave_type == WaveType.NEUTRAL:
            return 0.0
            
        # Volumenanalyse
        volume_strength = (
            volume / np.mean(self.volume_buffer)
            if self.volume_buffer else 1.0
        )
        
        # Preisstärke
        price_strength = abs(price_change)
        
        # Kombinierte Stärke
        strength = (
            volume_strength * 0.6 +
            price_strength * 0.4
        )
        
        return min(1.0, strength)
        
    def analyze_trend(self) -> TrendPhase:
        """Analysiert die aktuelle Trendphase"""
        if len(self.wave_points) < self.p.lookback:
            return TrendPhase.NEUTRAL
            
        recent_points = self.wave_points[-self.p.lookback:]
        
        # Thrust/Reaction Verhältnis
        thrust_count = sum(
            1 for p in recent_points
            if p.wave_type == WaveType.THRUST
        )
        reaction_count = sum(
            1 for p in recent_points
            if p.wave_type == WaveType.REACTION
        )
        
        # Preisbewegung
        price_change = (
            recent_points[-1].price -
            recent_points[0].price
        )
        
        # Volumenprofil
        volume_trend = np.mean([
            p.volume for p in recent_points[-5:]
        ]) / np.mean([
            p.volume for p in recent_points
        ])
        
        # Trendbestimmung
        if thrust_count > reaction_count * 1.5:
            if volume_trend > self.p.volume_factor:
                return TrendPhase.MARKUP
            else:
                return TrendPhase.ACCUMULATION
        elif reaction_count > thrust_count * 1.5:
            if volume_trend > self.p.volume_factor:
                return TrendPhase.MARKDOWN
            else:
                return TrendPhase.DISTRIBUTION
                
        return self.current_trend
        
    def calculate_momentum(self) -> float:
        """Berechnet das Momentum der Welle"""
        if len(self.wave_points) < 5:
            return 0.0
            
        recent_points = self.wave_points[-5:]
        
        # Preismomentum
        price_momentum = sum(
            1 if p.wave_type == WaveType.THRUST else
            -1 if p.wave_type == WaveType.REACTION else 0
            for p in recent_points
        ) / 5
        
        # Stärkemomentum
        strength_momentum = np.mean([
            p.strength for p in recent_points
        ])
        
        return (price_momentum + strength_momentum) / 2
        
    def next(self):
        current_price = self.data.close[0]
        current_volume = self.data.volume[0]
        
        # Puffer aktualisieren
        self.price_buffer.append(current_price)
        self.volume_buffer.append(current_volume)
        
        if len(self.price_buffer) > self.p.lookback * 2:
            self.price_buffer.pop(0)
            self.volume_buffer.pop(0)
            
        # Wave-Typ identifizieren
        wave_type = self.identify_wave(
            current_price,
            self.price_buffer[-2] if len(self.price_buffer) > 1
            else current_price
        )
        
        # Wellenstärke berechnen
        price_change = (
            (current_price - self.price_buffer[-2]) /
            self.price_buffer[-2]
            if len(self.price_buffer) > 1 else 0
        )
        
        strength = self.calculate_wave_strength(
            wave_type,
            price_change,
            current_volume
        )
        
        # Neuen Wave-Punkt erstellen
        new_point = WavePoint(
            price=current_price,
            volume=current_volume,
            time=len(self.wave_points),
            wave_type=wave_type,
            strength=strength
        )
        
        self.wave_points.append(new_point)
        if len(self.wave_points) > self.p.lookback * 2:
            self.wave_points.pop(0)
            
        # Trend analysieren
        self.current_trend = self.analyze_trend()
        
        # Momentum berechnen
        momentum = self.calculate_momentum()
        self.momentum_data.append(momentum)
        if len(self.momentum_data) > self.p.lookback:
            self.momentum_data.pop(0)
            
        # Linien aktualisieren
        self.lines.wave_type[0] = wave_type.value
        self.lines.trend_phase[0] = self.current_trend.value
        self.lines.strength[0] = strength
        self.lines.momentum[0] = momentum
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.wave_points:
            return None
            
        current_point = self.wave_points[-1]
        
        return {
            'wave_analysis': {
                'current_type': current_point.wave_type.value,
                'strength': current_point.strength,
                'momentum': self.lines.momentum[0],
                'consistency': (
                    'high'
                    if (len(self.wave_points) > 5 and
                        len(set(p.wave_type for p in
                               self.wave_points[-5:])) == 1)
                    else 'moderate'
                    if (len(self.wave_points) > 5 and
                        len(set(p.wave_type for p in
                               self.wave_points[-5:])) <= 2)
                    else 'low'
                )
            },
            'trend_analysis': {
                'current_phase': self.current_trend.value,
                'strength': (
                    'strong'
                    if (self.current_trend != TrendPhase.NEUTRAL and
                        current_point.strength > 0.7)
                    else 'moderate'
                    if (self.current_trend != TrendPhase.NEUTRAL and
                        current_point.strength > 0.4)
                    else 'weak'
                ),
                'momentum': (
                    'increasing'
                    if (len(self.momentum_data) > 1 and
                        self.momentum_data[-1] >
                        np.mean(self.momentum_data[:-1]))
                    else 'decreasing'
                    if (len(self.momentum_data) > 1 and
                        self.momentum_data[-1] <
                        np.mean(self.momentum_data[:-1]))
                    else 'stable'
                )
            },
            'volume_analysis': {
                'current_relative': (
                    current_point.volume /
                    np.mean(self.volume_buffer)
                    if self.volume_buffer else 1
                ),
                'trend': (
                    'increasing'
                    if (len(self.volume_buffer) > 1 and
                        np.mean(self.volume_buffer[-5:]) >
                        np.mean(self.volume_buffer[:-5]))
                    else 'decreasing'
                    if (len(self.volume_buffer) > 1 and
                        np.mean(self.volume_buffer[-5:]) <
                        np.mean(self.volume_buffer[:-5]))
                    else 'stable'
                ),
                'quality': (
                    'high'
                    if (current_point.volume >
                        np.mean(self.volume_buffer) *
                        self.p.volume_factor)
                    else 'moderate'
                    if (current_point.volume >
                        np.mean(self.volume_buffer))
                    else 'low'
                )
            },
            'wave_statistics': {
                'thrust_ratio': (
                    sum(1 for p in self.wave_points[-10:]
                        if p.wave_type == WaveType.THRUST) / 10
                    if len(self.wave_points) >= 10 else 0
                ),
                'reaction_ratio': (
                    sum(1 for p in self.wave_points[-10:]
                        if p.wave_type == WaveType.REACTION) / 10
                    if len(self.wave_points) >= 10 else 0
                ),
                'average_strength': np.mean([
                    p.strength for p in self.wave_points[-10:]
                ]) if len(self.wave_points) >= 10 else 0
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (self.current_trend == TrendPhase.ACCUMULATION
                        and current_point.strength > 0.7
                        and self.lines.momentum[0] > 0.5)
                    else 'buy'
                    if (self.current_trend == TrendPhase.MARKUP
                        and current_point.strength > 0.5)
                    else 'strong_sell'
                    if (self.current_trend == TrendPhase.DISTRIBUTION
                        and current_point.strength > 0.7
                        and self.lines.momentum[0] < -0.5)
                    else 'sell'
                    if (self.current_trend == TrendPhase.MARKDOWN
                        and current_point.strength > 0.5)
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if current_point.strength > 0.7
                    else 'moderate'
                    if current_point.strength > 0.4
                    else 'low'
                ),
                'timing': (
                    'optimal'
                    if (abs(self.lines.momentum[0]) > 0.7 and
                        current_point.strength > 0.7)
                    else 'suboptimal'
                    if (abs(self.lines.momentum[0]) > 0.4 and
                        current_point.strength > 0.4)
                    else 'poor'
                )
            },
            'risk_assessment': {
                'trend_reliability': (
                    'high'
                    if (self.current_trend != TrendPhase.NEUTRAL and
                        len(self.wave_points) >= 10 and
                        all(p.strength > 0.5
                            for p in self.wave_points[-5:]))
                    else 'moderate'
                    if (self.current_trend != TrendPhase.NEUTRAL and
                        len(self.wave_points) >= 5 and
                        any(p.strength > 0.5
                            for p in self.wave_points[-5:]))
                    else 'low'
                ),
                'momentum_stability': (
                    'high'
                    if (len(self.momentum_data) >= 5 and
                        np.std(self.momentum_data[-5:]) < 0.2)
                    else 'moderate'
                    if (len(self.momentum_data) >= 5 and
                        np.std(self.momentum_data[-5:]) < 0.4)
                    else 'low'
                ),
                'reversal_risk': (
                    'high'
                    if (current_point.strength < 0.3 and
                        abs(self.lines.momentum[0]) > 0.7)
                    else 'moderate'
                    if (current_point.strength < 0.5 or
                        abs(self.lines.momentum[0]) > 0.5)
                    else 'low'
                )
            }
        }
