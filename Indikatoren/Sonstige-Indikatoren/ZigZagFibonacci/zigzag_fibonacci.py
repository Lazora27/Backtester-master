import backtrader as bt
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple

class ZigZagType(Enum):
    """ZigZag Punkt Typen"""
    HIGH = "High"
    LOW = "Low"
    NONE = "None"

class FibLevel(Enum):
    """Fibonacci Level Typen"""
    LEVEL_0 = 0.0
    LEVEL_236 = 0.236
    LEVEL_382 = 0.382
    LEVEL_500 = 0.500
    LEVEL_618 = 0.618
    LEVEL_786 = 0.786
    LEVEL_1000 = 1.000

@dataclass
class ZigZagPoint:
    """Repräsentiert einen ZigZag-Punkt"""
    price: float
    time: int
    type: ZigZagType
    fib_levels: Dict[FibLevel, float]

class ZigZagFibonacciIndicator(bt.Indicator):
    """
    ZigZag Fibonacci Auto Levels Indicator
    
    Ein fortgeschrittener Indikator zur automatischen
    Erkennung von Fibonacci-Levels basierend auf
    ZigZag-Wendepunkten.
    
    Features:
    - Automatische ZigZag-Erkennung
    - Dynamische Fibonacci-Levels
    - Trendanalyse
    - Unterstützungs-/Widerstandszonen
    
    Parameter:
    - deviation (5.0): Abweichungsschwelle in %
    - depth (10): Minimale Balkenzahl zwischen Punkten
    - backtrack (3): Rückverfolgungstiefe
    """
    
    lines = ('zigzag', 'fib_236', 'fib_382', 'fib_500',
             'fib_618', 'fib_786')
    params = (
        ('deviation', 5.0),
        ('depth', 10),
        ('backtrack', 3),
    )
    
    plotlines = dict(
        zigzag=dict(color='blue', _name='ZigZag'),
        fib_236=dict(color='red', _name='23.6%'),
        fib_382=dict(color='green', _name='38.2%'),
        fib_500=dict(color='purple', _name='50.0%'),
        fib_618=dict(color='orange', _name='61.8%'),
        fib_786=dict(color='brown', _name='78.6%')
    )
    
    def __init__(self):
        super(ZigZagFibonacciIndicator, self).__init__()
        
        # ZigZag-Punkte
        self.zigzag_points: List[ZigZagPoint] = []
        
        # Preispuffer
        self.price_buffer = []
        self.time_buffer = []
        
        # Aktuelle Fibonacci-Levels
        self.current_fib_levels = {}
        
        # Support/Resistance Zonen
        self.support_zones = []
        self.resistance_zones = []
        
    def calculate_deviation(self, price1: float,
                          price2: float) -> float:
        """Berechnet die prozentuale Abweichung"""
        return abs(price1 - price2) / price1 * 100
        
    def is_valid_reversal(self, idx: int,
                         window: int = 5) -> Optional[ZigZagType]:
        """Prüft auf gültigen Wendepunkt"""
        if len(self.price_buffer) < window * 2 + 1:
            return None
            
        center = self.price_buffer[idx]
        left = self.price_buffer[max(0, idx-window):idx]
        right = self.price_buffer[idx+1:min(len(self.price_buffer),
                                          idx+window+1)]
                                          
        # Hoch
        if (all(x < center for x in left) and
            all(x < center for x in right)):
            return ZigZagType.HIGH
            
        # Tief
        if (all(x > center for x in left) and
            all(x > center for x in right)):
            return ZigZagType.LOW
            
        return None
        
    def calculate_fib_levels(self, start: float,
                           end: float) -> Dict[FibLevel, float]:
        """Berechnet Fibonacci-Levels"""
        diff = end - start
        
        return {
            FibLevel.LEVEL_0: start,
            FibLevel.LEVEL_236: start + diff * 0.236,
            FibLevel.LEVEL_382: start + diff * 0.382,
            FibLevel.LEVEL_500: start + diff * 0.500,
            FibLevel.LEVEL_618: start + diff * 0.618,
            FibLevel.LEVEL_786: start + diff * 0.786,
            FibLevel.LEVEL_1000: end
        }
        
    def update_support_resistance(self):
        """Aktualisiert Support/Resistance Zonen"""
        if len(self.zigzag_points) < 2:
            return
            
        # Aktuelle Zonen löschen
        self.support_zones.clear()
        self.resistance_zones.clear()
        
        # Neue Zonen aus Fibonacci-Levels
        current_price = self.price_buffer[-1]
        
        for point in self.zigzag_points[-2:]:
            for level, price in point.fib_levels.items():
                # Zone um Level
                zone_width = abs(price) * 0.01  # 1% Zone
                
                if price < current_price:
                    self.support_zones.append((
                        price - zone_width,
                        price + zone_width
                    ))
                else:
                    self.resistance_zones.append((
                        price - zone_width,
                        price + zone_width
                    ))
                    
    def next(self):
        current_price = self.data.close[0]
        
        # Puffer aktualisieren
        self.price_buffer.append(current_price)
        self.time_buffer.append(len(self.price_buffer))
        
        if len(self.price_buffer) > self.p.depth * 2:
            self.price_buffer.pop(0)
            self.time_buffer.pop(0)
            
        # Wendepunkt suchen
        current_idx = len(self.price_buffer) - 1
        reversal_type = self.is_valid_reversal(current_idx)
        
        if reversal_type:
            # Abweichung prüfen
            if self.zigzag_points:
                last_point = self.zigzag_points[-1]
                deviation = self.calculate_deviation(
                    last_point.price,
                    current_price
                )
                
                if deviation < self.p.deviation:
                    reversal_type = None
                    
        if reversal_type:
            # Fibonacci-Levels berechnen
            fib_levels = {}
            if len(self.zigzag_points) >= 1:
                fib_levels = self.calculate_fib_levels(
                    self.zigzag_points[-1].price,
                    current_price
                )
                
            # Neuen Punkt hinzufügen
            new_point = ZigZagPoint(
                price=current_price,
                time=self.time_buffer[-1],
                type=reversal_type,
                fib_levels=fib_levels
            )
            
            self.zigzag_points.append(new_point)
            
            # Alte Punkte entfernen
            if len(self.zigzag_points) > self.p.backtrack:
                self.zigzag_points.pop(0)
                
            # Support/Resistance aktualisieren
            self.update_support_resistance()
            
        # Linien aktualisieren
        self.lines.zigzag[0] = (
            current_price
            if reversal_type
            else float('nan')
        )
        
        if self.zigzag_points and self.zigzag_points[-1].fib_levels:
            levels = self.zigzag_points[-1].fib_levels
            self.lines.fib_236[0] = levels[FibLevel.LEVEL_236]
            self.lines.fib_382[0] = levels[FibLevel.LEVEL_382]
            self.lines.fib_500[0] = levels[FibLevel.LEVEL_500]
            self.lines.fib_618[0] = levels[FibLevel.LEVEL_618]
            self.lines.fib_786[0] = levels[FibLevel.LEVEL_786]
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.zigzag_points:
            return None
            
        current_price = self.price_buffer[-1]
        
        # Aktuelle Fibonacci-Levels
        current_levels = (
            self.zigzag_points[-1].fib_levels
            if self.zigzag_points[-1].fib_levels
            else {}
        )
        
        # Nächste Levels finden
        next_support = None
        next_resistance = None
        
        for level, price in current_levels.items():
            if price < current_price:
                if (next_support is None or
                    price > next_support[1]):
                    next_support = (level, price)
            else:
                if (next_resistance is None or
                    price < next_resistance[1]):
                    next_resistance = (level, price)
                    
        return {
            'zigzag_analysis': {
                'current_type': (
                    self.zigzag_points[-1].type.value
                    if self.zigzag_points else None
                ),
                'last_reversal_price': (
                    self.zigzag_points[-1].price
                    if self.zigzag_points else None
                ),
                'trend': (
                    'uptrend'
                    if (len(self.zigzag_points) >= 2 and
                        self.zigzag_points[-1].price >
                        self.zigzag_points[-2].price)
                    else 'downtrend'
                    if (len(self.zigzag_points) >= 2 and
                        self.zigzag_points[-1].price <
                        self.zigzag_points[-2].price)
                    else 'neutral'
                )
            },
            'fibonacci_analysis': {
                'current_levels': {
                    level.value: price
                    for level, price in current_levels.items()
                },
                'next_support': (
                    {
                        'level': next_support[0].value,
                        'price': next_support[1],
                        'distance': (
                            (current_price - next_support[1]) /
                            current_price * 100
                        )
                    }
                    if next_support else None
                ),
                'next_resistance': (
                    {
                        'level': next_resistance[0].value,
                        'price': next_resistance[1],
                        'distance': (
                            (next_resistance[1] - current_price) /
                            current_price * 100
                        )
                    }
                    if next_resistance else None
                )
            },
            'zone_analysis': {
                'support_zones': [
                    {
                        'lower': zone[0],
                        'upper': zone[1],
                        'strength': (
                            'strong'
                            if any(
                                abs(current_price - z[0]) < z[1] - z[0]
                                for z in self.support_zones
                            )
                            else 'moderate'
                            if any(
                                abs(current_price - z[0]) <
                                (z[1] - z[0]) * 2
                                for z in self.support_zones
                            )
                            else 'weak'
                        )
                    }
                    for zone in self.support_zones
                ],
                'resistance_zones': [
                    {
                        'lower': zone[0],
                        'upper': zone[1],
                        'strength': (
                            'strong'
                            if any(
                                abs(current_price - z[0]) < z[1] - z[0]
                                for z in self.resistance_zones
                            )
                            else 'moderate'
                            if any(
                                abs(current_price - z[0]) <
                                (z[1] - z[0]) * 2
                                for z in self.resistance_zones
                            )
                            else 'weak'
                        )
                    }
                    for zone in self.resistance_zones
                ]
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (next_support and
                        abs(current_price - next_support[1]) <
                        current_price * 0.01)
                    else 'buy'
                    if (next_support and
                        abs(current_price - next_support[1]) <
                        current_price * 0.02)
                    else 'strong_sell'
                    if (next_resistance and
                        abs(current_price - next_resistance[1]) <
                        current_price * 0.01)
                    else 'sell'
                    if (next_resistance and
                        abs(current_price - next_resistance[1]) <
                        current_price * 0.02)
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if (len(self.zigzag_points) >= 3 and
                        all(p.type != ZigZagType.NONE
                            for p in self.zigzag_points[-3:]))
                    else 'moderate'
                    if len(self.zigzag_points) >= 2
                    else 'low'
                ),
                'support_resistance_quality': (
                    'high'
                    if (len(self.support_zones) +
                        len(self.resistance_zones) >= 4)
                    else 'moderate'
                    if (len(self.support_zones) +
                        len(self.resistance_zones) >= 2)
                    else 'low'
                )
            },
            'risk_assessment': {
                'price_position': (
                    'strong_support'
                    if any(
                        current_price >= zone[0] and
                        current_price <= zone[1]
                        for zone in self.support_zones
                    )
                    else 'near_support'
                    if any(
                        abs(current_price - zone[0]) <
                        (zone[1] - zone[0]) * 2
                        for zone in self.support_zones
                    )
                    else 'strong_resistance'
                    if any(
                        current_price >= zone[0] and
                        current_price <= zone[1]
                        for zone in self.resistance_zones
                    )
                    else 'near_resistance'
                    if any(
                        abs(current_price - zone[0]) <
                        (zone[1] - zone[0]) * 2
                        for zone in self.resistance_zones
                    )
                    else 'neutral'
                ),
                'reversal_probability': (
                    'high'
                    if (len(self.zigzag_points) >= 3 and
                        self.zigzag_points[-1].type !=
                        self.zigzag_points[-2].type)
                    else 'moderate'
                    if len(self.zigzag_points) >= 2
                    else 'low'
                ),
                'level_confluence': (
                    'high'
                    if (len(self.support_zones) >= 2 or
                        len(self.resistance_zones) >= 2)
                    else 'moderate'
                    if (len(self.support_zones) +
                        len(self.resistance_zones) >= 2)
                    else 'low'
                )
            }
        }
