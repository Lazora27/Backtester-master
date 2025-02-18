import backtrader as bt
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class WaveType(Enum):
    """Wolfe Wave Muster Typen"""
    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NONE = "None"

@dataclass
class WavePoint:
    """Repräsentiert einen Punkt im Wolfe Wave Muster"""
    price: float
    time: int
    point_type: int  # 1-5 für die Punkte des Musters

class WolfeWaveIndicator(bt.Indicator):
    """
    Wolfe Wave Pattern Indicator
    
    Ein fortgeschrittener Indikator zur Erkennung von
    Wolfe Wave Mustern im Preischart.
    
    Features:
    - Automatische Mustererkennung
    - Preisziel-Berechnung
    - Zeitziel-Berechnung
    - Musterqualitäts-Bewertung
    
    Parameter:
    - min_pattern_bars (20): Minimale Balkenzahl
    - max_pattern_bars (100): Maximale Balkenzahl
    - symmetry_threshold (0.2): Symmetrie-Schwelle
    - time_factor (1.618): Zeitfaktor
    """
    
    lines = ('pattern_type', 'target_price', 'target_time',
             'quality')
    params = (
        ('min_pattern_bars', 20),
        ('max_pattern_bars', 100),
        ('symmetry_threshold', 0.2),
        ('time_factor', 1.618),
    )
    
    plotlines = dict(
        pattern_type=dict(color='blue', _name='Pattern'),
        target_price=dict(color='red', _name='Target Price'),
        target_time=dict(color='green', _name='Target Time'),
        quality=dict(color='purple', _name='Quality')
    )
    
    def __init__(self):
        super(WolfeWaveIndicator, self).__init__()
        
        # Preispuffer
        self.price_buffer = []
        self.time_buffer = []
        
        # Aktuelle Welle
        self.current_wave: List[WavePoint] = []
        
        # Musterstatistiken
        self.pattern_stats = {}
        
        # Letzte erkannte Muster
        self.last_patterns = []
        
    def is_pivot_high(self, idx: int, window: int = 5) -> bool:
        """Prüft auf lokales Maximum"""
        if len(self.price_buffer) < window * 2 + 1:
            return False
            
        center = self.price_buffer[idx]
        left = self.price_buffer[max(0, idx-window):idx]
        right = self.price_buffer[idx+1:min(len(self.price_buffer),
                                          idx+window+1)]
                                          
        return (all(x < center for x in left) and
                all(x < center for x in right))
                
    def is_pivot_low(self, idx: int, window: int = 5) -> bool:
        """Prüft auf lokales Minimum"""
        if len(self.price_buffer) < window * 2 + 1:
            return False
            
        center = self.price_buffer[idx]
        left = self.price_buffer[max(0, idx-window):idx]
        right = self.price_buffer[idx+1:min(len(self.price_buffer),
                                          idx+window+1)]
                                          
        return (all(x > center for x in left) and
                all(x > center for x in right))
                
    def check_wave_symmetry(self, points: List[WavePoint]) -> float:
        """Prüft die Symmetrie des Musters"""
        if len(points) != 5:
            return 0.0
            
        # Zeit-Symmetrie
        time_13 = points[2].time - points[0].time
        time_35 = points[4].time - points[2].time
        time_symmetry = min(time_13, time_35) / max(time_13, time_35)
        
        # Preis-Symmetrie
        price_13 = abs(points[2].price - points[0].price)
        price_35 = abs(points[4].price - points[2].price)
        price_symmetry = min(price_13, price_35) / max(price_13,
                                                      price_35)
                                                      
        return (time_symmetry + price_symmetry) / 2
        
    def calculate_target(self, points: List[WavePoint]) -> tuple:
        """Berechnet Preis- und Zeitziel"""
        if len(points) != 5:
            return None, None
            
        # Preisziel basierend auf 1-3-5 Projektion
        price_13 = points[2].price - points[0].price
        price_35 = points[4].price - points[2].price
        target_price = points[4].price + (price_13 + price_35) / 2
        
        # Zeitziel basierend auf Fibonacci
        time_13 = points[2].time - points[0].time
        time_35 = points[4].time - points[2].time
        target_time = (points[4].time +
                      ((time_13 + time_35) / 2) *
                      self.p.time_factor)
                      
        return target_price, target_time
        
    def identify_pattern(self) -> Optional[WaveType]:
        """Identifiziert Wolfe Wave Muster"""
        if len(self.current_wave) != 5:
            return None
            
        points = self.current_wave
        
        # Grundlegende Musterregeln prüfen
        if not (points[1].price > points[0].price and
                points[2].price < points[1].price and
                points[3].price > points[2].price and
                points[4].price < points[3].price):
            return None
            
        # Symmetrie prüfen
        symmetry = self.check_wave_symmetry(points)
        if symmetry < self.p.symmetry_threshold:
            return None
            
        # Mustertyp bestimmen
        if (points[4].price > points[0].price and
            points[3].price > points[1].price):
            return WaveType.BULLISH
        elif (points[4].price < points[0].price and
              points[3].price < points[1].price):
            return WaveType.BEARISH
            
        return None
        
    def calculate_pattern_quality(self) -> float:
        """Berechnet die Qualität des Musters"""
        if len(self.current_wave) != 5:
            return 0.0
            
        # Symmetrie
        symmetry = self.check_wave_symmetry(self.current_wave)
        
        # Trend-Stärke
        trend_strength = abs(
            self.current_wave[4].price -
            self.current_wave[0].price
        ) / (max(p.price for p in self.current_wave) -
             min(p.price for p in self.current_wave))
             
        # Zeit-Verhältnis
        time_ratio = min(
            self.current_wave[2].time - self.current_wave[0].time,
            self.current_wave[4].time - self.current_wave[2].time
        ) / max(
            self.current_wave[2].time - self.current_wave[0].time,
            self.current_wave[4].time - self.current_wave[2].time
        )
        
        # Kombinierte Qualität
        quality = (
            symmetry * 0.4 +
            trend_strength * 0.3 +
            time_ratio * 0.3
        )
        
        return min(1.0, quality)
        
    def next(self):
        # Preisdaten sammeln
        self.price_buffer.append(self.data.close[0])
        self.time_buffer.append(len(self.price_buffer))
        
        if len(self.price_buffer) > self.p.max_pattern_bars:
            self.price_buffer.pop(0)
            self.time_buffer.pop(0)
            
        # Pivot-Punkte suchen
        current_idx = len(self.price_buffer) - 1
        
        if (self.is_pivot_high(current_idx) or
            self.is_pivot_low(current_idx)):
            # Neuen Punkt hinzufügen
            new_point = WavePoint(
                price=self.price_buffer[current_idx],
                time=self.time_buffer[current_idx],
                point_type=len(self.current_wave) + 1
            )
            
            self.current_wave.append(new_point)
            
            # Alte Punkte entfernen
            if len(self.current_wave) > 5:
                self.current_wave.pop(0)
                
        # Muster analysieren
        pattern_type = WaveType.NONE
        target_price = self.data.close[0]
        target_time = len(self.price_buffer)
        quality = 0.0
        
        if len(self.current_wave) == 5:
            pattern_type = self.identify_pattern()
            if pattern_type:
                target_price, target_time = self.calculate_target(
                    self.current_wave
                )
                quality = self.calculate_pattern_quality()
                
                # Muster speichern
                self.last_patterns.append({
                    'type': pattern_type,
                    'points': self.current_wave.copy(),
                    'target_price': target_price,
                    'target_time': target_time,
                    'quality': quality
                })
                
                if len(self.last_patterns) > 10:
                    self.last_patterns.pop(0)
                    
        # Linien aktualisieren
        self.lines.pattern_type[0] = (
            pattern_type.value if pattern_type else WaveType.NONE.value
        )
        self.lines.target_price[0] = target_price
        self.lines.target_time[0] = target_time
        self.lines.quality[0] = quality
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.last_patterns:
            return None
            
        current_pattern = self.last_patterns[-1]
        current_price = self.data.close[0]
        
        return {
            'pattern_analysis': {
                'type': current_pattern['type'].value,
                'quality': current_pattern['quality'],
                'completion': len(self.current_wave) / 5
            },
            'target_analysis': {
                'price': current_pattern['target_price'],
                'time': current_pattern['target_time'],
                'price_distance': (
                    (current_pattern['target_price'] -
                     current_price) / current_price
                ),
                'time_distance': (
                    current_pattern['target_time'] -
                    len(self.price_buffer)
                )
            },
            'pattern_statistics': {
                'recent_patterns': len(self.last_patterns),
                'success_rate': sum(
                    1 for p in self.last_patterns
                    if p['quality'] > 0.7
                ) / max(1, len(self.last_patterns)),
                'average_quality': np.mean([
                    p['quality'] for p in self.last_patterns
                ])
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (current_pattern['type'] == WaveType.BULLISH
                        and current_pattern['quality'] > 0.8)
                    else 'buy'
                    if (current_pattern['type'] == WaveType.BULLISH
                        and current_pattern['quality'] > 0.6)
                    else 'strong_sell'
                    if (current_pattern['type'] == WaveType.BEARISH
                        and current_pattern['quality'] > 0.8)
                    else 'sell'
                    if (current_pattern['type'] == WaveType.BEARISH
                        and current_pattern['quality'] > 0.6)
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if current_pattern['quality'] > 0.8
                    else 'moderate'
                    if current_pattern['quality'] > 0.6
                    else 'low'
                ),
                'timing': (
                    'optimal'
                    if len(self.current_wave) == 5
                    else 'developing'
                    if len(self.current_wave) >= 3
                    else 'early'
                )
            },
            'risk_assessment': {
                'invalidation_price': (
                    min(p.price for p in self.current_wave)
                    if current_pattern['type'] == WaveType.BULLISH
                    else max(p.price for p in self.current_wave)
                ),
                'risk_reward_ratio': abs(
                    (current_pattern['target_price'] - current_price) /
                    (current_price - self.current_wave[0].price)
                    if len(self.current_wave) > 0 else 0
                ),
                'pattern_reliability': (
                    'high'
                    if (current_pattern['quality'] > 0.8 and
                        len(self.last_patterns) > 5)
                    else 'moderate'
                    if (current_pattern['quality'] > 0.6 and
                        len(self.last_patterns) > 3)
                    else 'low'
                )
            }
        }
