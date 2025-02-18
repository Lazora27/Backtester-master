import backtrader as bt
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional

class WyckoffPhase(Enum):
    """Wyckoff Phasen"""
    PHASE_A = "Phase A (Accumulation)"
    PHASE_B = "Phase B (Markup)"
    PHASE_C = "Phase C (Distribution)"
    PHASE_D = "Phase D (Markdown)"
    NONE = "None"

class MarketCondition(Enum):
    """Marktzustände"""
    ACCUMULATION = "Accumulation"
    DISTRIBUTION = "Distribution"
    NEUTRAL = "Neutral"

@dataclass
class VolumePoint:
    """Repräsentiert einen Volumen-Datenpunkt"""
    price: float
    volume: float
    time: int
    condition: MarketCondition

class WyckoffAccumulationDistributionIndicator(bt.Indicator):
    """
    Wyckoff Accumulation Distribution Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    Wyckoff Akkumulations- und Distributionsphasen.
    
    Features:
    - Phasenerkennung
    - Volumenprofile
    - Effort vs. Result
    - Marktstrukturanalyse
    
    Parameter:
    - volume_threshold (1.5): Volumenschwelle
    - phase_length (20): Phasenlänge
    - effort_threshold (0.7): Effort-Schwelle
    """
    
    lines = ('phase', 'condition', 'effort', 'result')
    params = (
        ('volume_threshold', 1.5),
        ('phase_length', 20),
        ('effort_threshold', 0.7),
    )
    
    plotlines = dict(
        phase=dict(color='blue', _name='Phase'),
        condition=dict(color='green', _name='Condition'),
        effort=dict(color='red', _name='Effort'),
        result=dict(color='purple', _name='Result')
    )
    
    def __init__(self):
        super(WyckoffAccumulationDistributionIndicator, self).__init__()
        
        # Preispuffer
        self.price_buffer = []
        self.volume_buffer = []
        
        # Volumen-Datenpunkte
        self.volume_points: List[VolumePoint] = []
        
        # Phasenanalyse
        self.current_phase = WyckoffPhase.NONE
        self.phase_data: Dict = {}
        
        # Effort-Result Analyse
        self.effort_data = []
        self.result_data = []
        
    def analyze_volume_condition(self, price: float,
                               volume: float) -> MarketCondition:
        """Analysiert den Volumenzustand"""
        if len(self.volume_buffer) < 10:
            return MarketCondition.NEUTRAL
            
        # Volumen-Analyse
        avg_volume = np.mean(self.volume_buffer[-10:])
        volume_ratio = volume / avg_volume
        
        # Preisbewegung
        price_change = (
            price - self.price_buffer[-2]
            if len(self.price_buffer) > 1
            else 0
        )
        
        if volume_ratio > self.p.volume_threshold:
            if price_change > 0:
                return MarketCondition.ACCUMULATION
            elif price_change < 0:
                return MarketCondition.DISTRIBUTION
                
        return MarketCondition.NEUTRAL
        
    def analyze_effort_result(self) -> tuple:
        """Analysiert Effort vs. Result"""
        if len(self.volume_points) < self.p.phase_length:
            return 0, 0
            
        recent_points = self.volume_points[-self.p.phase_length:]
        
        # Effort (Volumen)
        volume_effort = sum(
            p.volume
            for p in recent_points
        ) / len(recent_points)
        
        # Result (Preisbewegung)
        price_result = abs(
            recent_points[-1].price -
            recent_points[0].price
        )
        
        # Normalisierung
        max_effort = max(p.volume for p in recent_points)
        max_result = max(
            abs(p.price - recent_points[0].price)
            for p in recent_points
        )
        
        normalized_effort = (
            volume_effort / max_effort
            if max_effort > 0 else 0
        )
        normalized_result = (
            price_result / max_result
            if max_result > 0 else 0
        )
        
        return normalized_effort, normalized_result
        
    def determine_phase(self) -> WyckoffPhase:
        """Bestimmt die aktuelle Wyckoff-Phase"""
        if len(self.volume_points) < self.p.phase_length:
            return WyckoffPhase.NONE
            
        recent_points = self.volume_points[-self.p.phase_length:]
        
        # Akkumulation/Distribution zählen
        acc_count = sum(
            1 for p in recent_points
            if p.condition == MarketCondition.ACCUMULATION
        )
        dist_count = sum(
            1 for p in recent_points
            if p.condition == MarketCondition.DISTRIBUTION
        )
        
        # Preisbewegung
        price_change = (
            recent_points[-1].price -
            recent_points[0].price
        )
        
        # Effort vs. Result
        effort, result = self.analyze_effort_result()
        
        # Phasenbestimmung
        if acc_count > dist_count:
            if price_change > 0:
                if effort > self.p.effort_threshold:
                    return WyckoffPhase.PHASE_B
                else:
                    return WyckoffPhase.PHASE_A
            else:
                return WyckoffPhase.PHASE_A
        elif dist_count > acc_count:
            if price_change < 0:
                if effort > self.p.effort_threshold:
                    return WyckoffPhase.PHASE_D
                else:
                    return WyckoffPhase.PHASE_C
            else:
                return WyckoffPhase.PHASE_C
                
        return self.current_phase
        
    def next(self):
        current_price = self.data.close[0]
        current_volume = self.data.volume[0]
        
        # Puffer aktualisieren
        self.price_buffer.append(current_price)
        self.volume_buffer.append(current_volume)
        
        if len(self.price_buffer) > self.p.phase_length * 2:
            self.price_buffer.pop(0)
            self.volume_buffer.pop(0)
            
        # Volumenzustand analysieren
        condition = self.analyze_volume_condition(
            current_price,
            current_volume
        )
        
        # Neuen Punkt hinzufügen
        new_point = VolumePoint(
            price=current_price,
            volume=current_volume,
            time=len(self.volume_points),
            condition=condition
        )
        self.volume_points.append(new_point)
        
        if len(self.volume_points) > self.p.phase_length * 2:
            self.volume_points.pop(0)
            
        # Phase bestimmen
        self.current_phase = self.determine_phase()
        
        # Effort vs. Result
        effort, result = self.analyze_effort_result()
        
        # Linien aktualisieren
        self.lines.phase[0] = self.current_phase.value
        self.lines.condition[0] = condition.value
        self.lines.effort[0] = effort
        self.lines.result[0] = result
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.volume_points:
            return None
            
        effort, result = self.analyze_effort_result()
        
        return {
            'phase_analysis': {
                'current_phase': self.current_phase.value,
                'strength': (
                    effort if self.current_phase in
                    [WyckoffPhase.PHASE_B, WyckoffPhase.PHASE_D]
                    else result
                ),
                'duration': sum(
                    1 for p in self.volume_points
                    if p.condition != MarketCondition.NEUTRAL
                )
            },
            'volume_analysis': {
                'accumulation_strength': sum(
                    1 for p in self.volume_points[-10:]
                    if p.condition == MarketCondition.ACCUMULATION
                ) / 10,
                'distribution_strength': sum(
                    1 for p in self.volume_points[-10:]
                    if p.condition == MarketCondition.DISTRIBUTION
                ) / 10,
                'volume_trend': (
                    'increasing'
                    if (len(self.volume_buffer) > 1 and
                        np.mean(self.volume_buffer[-5:]) >
                        np.mean(self.volume_buffer[-10:-5]))
                    else 'decreasing'
                    if (len(self.volume_buffer) > 1 and
                        np.mean(self.volume_buffer[-5:]) <
                        np.mean(self.volume_buffer[-10:-5]))
                    else 'neutral'
                )
            },
            'effort_result_analysis': {
                'effort': effort,
                'result': result,
                'efficiency': (
                    result / effort if effort > 0 else 0
                ),
                'divergence': (
                    'positive'
                    if effort > result * 1.2
                    else 'negative'
                    if result > effort * 1.2
                    else 'none'
                )
            },
            'market_structure': {
                'condition': (
                    'strong_accumulation'
                    if (self.current_phase == WyckoffPhase.PHASE_A and
                        effort > self.p.effort_threshold)
                    else 'weak_accumulation'
                    if self.current_phase == WyckoffPhase.PHASE_A
                    else 'strong_distribution'
                    if (self.current_phase == WyckoffPhase.PHASE_C and
                        effort > self.p.effort_threshold)
                    else 'weak_distribution'
                    if self.current_phase == WyckoffPhase.PHASE_C
                    else 'markup'
                    if self.current_phase == WyckoffPhase.PHASE_B
                    else 'markdown'
                    if self.current_phase == WyckoffPhase.PHASE_D
                    else 'neutral'
                ),
                'strength': (
                    'high'
                    if effort > self.p.effort_threshold
                    else 'moderate'
                    if effort > self.p.effort_threshold * 0.7
                    else 'low'
                ),
                'sustainability': (
                    'high'
                    if (effort > self.p.effort_threshold and
                        abs(effort - result) < 0.2)
                    else 'moderate'
                    if abs(effort - result) < 0.3
                    else 'low'
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (self.current_phase == WyckoffPhase.PHASE_A and
                        effort > self.p.effort_threshold)
                    else 'buy'
                    if self.current_phase == WyckoffPhase.PHASE_B
                    else 'strong_sell'
                    if (self.current_phase == WyckoffPhase.PHASE_C and
                        effort > self.p.effort_threshold)
                    else 'sell'
                    if self.current_phase == WyckoffPhase.PHASE_D
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if effort > self.p.effort_threshold
                    else 'moderate'
                    if effort > self.p.effort_threshold * 0.7
                    else 'low'
                ),
                'timing': (
                    'optimal'
                    if abs(effort - result) < 0.2
                    else 'suboptimal'
                    if abs(effort - result) < 0.3
                    else 'poor'
                )
            }
        }
