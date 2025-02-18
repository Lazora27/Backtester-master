import backtrader as bt
import numpy as np
from collections import deque
from enum import Enum

class TrendType(Enum):
    """Trend-Typen Enumeration"""
    UPTREND = "Uptrend"
    DOWNTREND = "Downtrend"
    SIDEWAYS = "Sideways"

class AutoFibonacci(bt.Indicator):
    """
    Auto Fibonacci Retracement Indicator
    
    Ein automatischer Indikator zur Erkennung und
    Analyse von Fibonacci-Retracements.
    
    Features:
    - Automatische Swing-Erkennung
    - Fibonacci-Level-Berechnung
    - Trendanalyse
    - Qualitätsmetrik
    
    Parameter:
    - swing_threshold (0.02): Swing-Schwelle
    - trend_period (20): Trendperiode
    - quality_threshold (0.7): Qualitätsschwelle
    """
    
    lines = ('fib_level', 'swing_strength',
             'trend_quality', 'retracement_level',
             'signal')
             
    params = (
        ('swing_threshold', 0.02),
        ('trend_period', 20),
        ('quality_threshold', 0.7)
    )
    
    plotlines = dict(
        fib_level=dict(color='blue', _name='Fibonacci Level'),
        swing_strength=dict(color='green', _name='Swing Strength'),
        trend_quality=dict(color='red', _name='Trend Quality'),
        retracement_level=dict(color='purple', _name='Retracement Level'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(AutoFibonacci, self).__init__()
        
        # Fibonacci Levels
        self.fib_levels = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
        
        # Swing Tracking
        self.price_history = deque(maxlen=self.p.trend_period)
        self.swing_history = deque(maxlen=self.p.trend_period)
        self.level_history = []
        
        # Aktuelle Swing-Punkte
        self.swing_high = None
        self.swing_low = None
        self.current_trend = None
        
    def detect_swing(self, price_data):
        """
        Erkennt Swing-Punkte im Preischart.
        """
        if len(price_data) < 3:
            return None, 0
            
        # Lokale Maxima und Minima
        middle_idx = len(price_data) // 2
        middle_price = price_data[middle_idx]
        
        is_high = all(
            middle_price >= p
            for i, p in enumerate(price_data)
            if i != middle_idx
        )
        
        is_low = all(
            middle_price <= p
            for i, p in enumerate(price_data)
            if i != middle_idx
        )
        
        if is_high:
            return 'high', middle_price
        elif is_low:
            return 'low', middle_price
        else:
            return None, 0
            
    def calculate_fibonacci_levels(self, high, low):
        """
        Berechnet Fibonacci-Retracement-Level.
        """
        range_size = high - low
        levels = {}
        
        for fib in self.fib_levels:
            if self.current_trend == TrendType.UPTREND:
                level = high - (range_size * fib)
            else:
                level = low + (range_size * fib)
                
            levels[fib] = level
            
        return levels
        
    def find_nearest_level(self, price, levels):
        """
        Findet das nächste Fibonacci-Level.
        """
        if not levels:
            return None, None
            
        distances = {
            fib: abs(level - price)
            for fib, level in levels.items()
        }
        
        nearest_fib = min(
            distances.keys(),
            key=lambda x: distances[x]
        )
        
        return nearest_fib, levels[nearest_fib]
        
    def analyze_trend(self):
        """
        Analysiert den aktuellen Trend.
        """
        if len(self.price_history) < self.p.trend_period:
            return TrendType.SIDEWAYS, 0
            
        prices = np.array(self.price_history)
        trend = np.polyfit(
            range(len(prices)),
            prices,
            1
        )[0]
        
        trend_strength = abs(trend)
        
        if trend_strength < 0.001:
            return TrendType.SIDEWAYS, trend_strength
        elif trend > 0:
            return TrendType.UPTREND, trend_strength
        else:
            return TrendType.DOWNTREND, trend_strength
            
    def calculate_swing_strength(self, swing_type, price):
        """
        Berechnet die Stärke eines Swings.
        """
        if not self.swing_history:
            return 0
            
        # Relative Swing-Größe
        prev_swings = [
            s[1] for s in self.swing_history
            if s[0] == swing_type
        ]
        
        if not prev_swings:
            return 0
            
        avg_swing = np.mean(prev_swings)
        if avg_swing == 0:
            return 0
            
        return abs(price - avg_swing) / avg_swing
        
    def next(self):
        price = self.data.close[0]
        
        # Historie aktualisieren
        self.price_history.append(price)
        
        # Trend analysieren
        trend_type, trend_strength = self.analyze_trend()
        self.current_trend = trend_type
        
        # Swing-Erkennung
        if len(self.price_history) >= 3:
            swing_type, swing_price = self.detect_swing(
                list(self.price_history)[-3:]
            )
            
            if swing_type:
                swing_strength = self.calculate_swing_strength(
                    swing_type,
                    swing_price
                )
                
                if swing_strength > self.p.swing_threshold:
                    self.swing_history.append(
                        (swing_type, swing_price)
                    )
                    
                    if swing_type == 'high':
                        self.swing_high = swing_price
                    else:
                        self.swing_low = swing_price
                        
        # Fibonacci-Level berechnen
        if (self.swing_high is not None and
            self.swing_low is not None):
            fib_levels = self.calculate_fibonacci_levels(
                self.swing_high,
                self.swing_low
            )
            
            # Nächstes Level finden
            nearest_fib, level = self.find_nearest_level(
                price,
                fib_levels
            )
            
            if nearest_fib is not None:
                # Qualität berechnen
                level_quality = 1 - (
                    abs(price - level) /
                    (self.swing_high - self.swing_low)
                )
                
                # Level speichern
                self.level_history.append({
                    'fib': nearest_fib,
                    'level': level,
                    'quality': level_quality
                })
                
                # Linien aktualisieren
                self.lines.fib_level[0] = level
                self.lines.swing_strength[0] = (
                    self.calculate_swing_strength(
                        'high' if price > level else 'low',
                        price
                    )
                )
                self.lines.trend_quality[0] = trend_strength
                self.lines.retracement_level[0] = nearest_fib
                
                # Trading Signal
                if level_quality > self.p.quality_threshold:
                    if (nearest_fib <= 0.382 and
                        trend_type == TrendType.UPTREND):
                        self.lines.signal[0] = 1  # Kaufsignal
                    elif (nearest_fib >= 0.618 and
                          trend_type == TrendType.DOWNTREND):
                        self.lines.signal[0] = -1  # Verkaufssignal
                    else:
                        self.lines.signal[0] = 0
                else:
                    self.lines.signal[0] = 0
            else:
                # Standardwerte
                self.lines.fib_level[0] = price
                self.lines.swing_strength[0] = 0
                self.lines.trend_quality[0] = trend_strength
                self.lines.retracement_level[0] = 0
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.fib_level[0] = price
            self.lines.swing_strength[0] = 0
            self.lines.trend_quality[0] = trend_strength
            self.lines.retracement_level[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_history = max(
            self.p.trend_period,
            len(self.data)
        )
        if len(self.level_history) > max_history:
            self.level_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'fibonacci_metrics': {
                'level': self.lines.fib_level[0],
                'retracement': self.lines.retracement_level[0],
                'swing_strength': self.lines.swing_strength[0],
                'trend_quality': self.lines.trend_quality[0]
            },
            'level_analysis': {
                'current_level': (
                    f"{self.lines.retracement_level[0]:.3f}"
                    if self.lines.retracement_level[0]
                    else "None"
                ),
                'strength': (
                    'strong'
                    if self.lines.swing_strength[0] >
                       self.p.swing_threshold * 2
                    else 'moderate'
                    if self.lines.swing_strength[0] >
                       self.p.swing_threshold
                    else 'weak'
                ),
                'quality': (
                    'high'
                    if self.lines.trend_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.trend_quality[0] > 0.4
                    else 'low'
                )
            },
            'trend_analysis': {
                'type': (
                    self.current_trend.value
                    if self.current_trend
                    else "Unknown"
                ),
                'strength': self.lines.trend_quality[0],
                'stability': (
                    'stable'
                    if len(self.swing_history) > 2 and
                    all(s[1] * self.swing_history[-1][1] > 0
                        for s in self.swing_history[-3:])
                    else 'unstable'
                )
            },
            'swing_analysis': {
                'high': (
                    f"{self.swing_high:.2f}"
                    if self.swing_high is not None
                    else "None"
                ),
                'low': (
                    f"{self.swing_low:.2f}"
                    if self.swing_low is not None
                    else "None"
                ),
                'range': (
                    self.swing_high - self.swing_low
                    if (self.swing_high is not None and
                        self.swing_low is not None)
                    else 0
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
                    self.lines.trend_quality[0] *
                    self.lines.swing_strength[0]
                )
            },
            'market_conditions': {
                'retracement_quality': (
                    'optimal'
                    if (0.382 <= self.lines.retracement_level[0] <= 0.618)
                    else 'suboptimal'
                ),
                'trend_clarity': (
                    'clear'
                    if self.lines.trend_quality[0] > 0.5
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.trend_quality[0] > 0.5 and
                        self.lines.swing_strength[0] >
                        self.p.swing_threshold)
                    else 'unfavorable'
                )
            }
        }
