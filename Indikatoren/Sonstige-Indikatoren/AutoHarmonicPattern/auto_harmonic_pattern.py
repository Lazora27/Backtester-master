import backtrader as bt
import numpy as np
from enum import Enum
from collections import deque

class PatternType(Enum):
    """Harmonische Pattern-Typen"""
    GARTLEY = "Gartley"
    BUTTERFLY = "Butterfly"
    BAT = "Bat"
    CRAB = "Crab"
    SHARK = "Shark"
    CYPHER = "Cypher"

class AutoHarmonicPattern(bt.Indicator):
    """
    Auto Harmonic Pattern Finder
    
    Ein fortgeschrittener Indikator zur Erkennung
    harmonischer Preismuster.
    
    Features:
    - Automatische Pattern-Erkennung
    - Fibonacci-Ratios
    - Qualitätsanalyse
    - Multi-Pattern-Support
    
    Parameter:
    - pattern_threshold (0.02): Pattern-Schwelle
    - quality_threshold (0.7): Qualitätsschwelle
    - lookback_period (50): Rückblickperiode
    """
    
    lines = ('pattern_signal', 'pattern_quality',
             'completion_level', 'potential_reward',
             'signal')
             
    params = (
        ('pattern_threshold', 0.02),
        ('quality_threshold', 0.7),
        ('lookback_period', 50)
    )
    
    plotlines = dict(
        pattern_signal=dict(color='blue', _name='Pattern Signal'),
        pattern_quality=dict(color='green', _name='Pattern Quality'),
        completion_level=dict(color='red', _name='Completion Level'),
        potential_reward=dict(color='purple', _name='Potential Reward'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(AutoHarmonicPattern, self).__init__()
        
        # Pattern-Definitionen
        self.patterns = {
            PatternType.GARTLEY: {
                'XA': 1.0,
                'AB': 0.618,
                'BC': 0.386,
                'CD': 1.272
            },
            PatternType.BUTTERFLY: {
                'XA': 1.0,
                'AB': 0.786,
                'BC': 0.382,
                'CD': 1.618
            },
            PatternType.BAT: {
                'XA': 1.0,
                'AB': 0.382,
                'BC': 0.886,
                'CD': 2.618
            },
            PatternType.CRAB: {
                'XA': 1.0,
                'AB': 0.382,
                'BC': 0.886,
                'CD': 3.618
            },
            PatternType.SHARK: {
                'XA': 1.0,
                'AB': 1.13,
                'BC': 1.618,
                'CD': 0.886
            },
            PatternType.CYPHER: {
                'XA': 1.0,
                'AB': 0.382,
                'BC': 1.272,
                'CD': 0.786
            }
        }
        
        # Pattern Tracking
        self.price_history = deque(maxlen=self.p.lookback_period)
        self.swing_points = []
        self.current_pattern = None
        
    def calculate_ratio(self, start_price, end_price):
        """
        Berechnet das Ratio zwischen zwei Preispunkten.
        """
        if start_price == 0:
            return 0
        return abs(end_price - start_price) / abs(start_price)
        
    def find_swing_points(self, prices, window=5):
        """
        Findet Swing-Punkte im Preischart.
        """
        if len(prices) < window * 2 + 1:
            return []
            
        swing_points = []
        for i in range(window, len(prices) - window):
            left_prices = prices[i-window:i]
            right_prices = prices[i+1:i+window+1]
            current_price = prices[i]
            
            # Swing High
            if (current_price > max(left_prices) and
                current_price > max(right_prices)):
                swing_points.append(('high', i, current_price))
                
            # Swing Low
            elif (current_price < min(left_prices) and
                  current_price < min(right_prices)):
                swing_points.append(('low', i, current_price))
                
        return swing_points
        
    def identify_pattern(self, points):
        """
        Identifiziert harmonische Muster.
        """
        if len(points) < 5:
            return None, 0
            
        # Letzte 5 Punkte für XABCD
        x, a, b, c, d = points[-5:]
        
        # Ratios berechnen
        xa_ratio = self.calculate_ratio(x[2], a[2])
        ab_ratio = self.calculate_ratio(a[2], b[2])
        bc_ratio = self.calculate_ratio(b[2], c[2])
        cd_ratio = self.calculate_ratio(c[2], d[2])
        
        best_match = None
        best_quality = 0
        
        # Pattern vergleichen
        for pattern_type, ratios in self.patterns.items():
            quality = 1.0
            
            # Ratio-Abweichungen
            quality *= (1 - abs(xa_ratio - ratios['XA']))
            quality *= (1 - abs(ab_ratio - ratios['AB']))
            quality *= (1 - abs(bc_ratio - ratios['BC']))
            quality *= (1 - abs(cd_ratio - ratios['CD']))
            
            if quality > best_quality:
                best_quality = quality
                best_match = pattern_type
                
        return best_match, best_quality
        
    def calculate_completion(self, points, pattern_type):
        """
        Berechnet den Fertigstellungsgrad eines Musters.
        """
        if not points or not pattern_type:
            return 0
            
        target_ratios = self.patterns[pattern_type]
        current_ratios = {
            'XA': self.calculate_ratio(points[-5][2], points[-4][2]),
            'AB': self.calculate_ratio(points[-4][2], points[-3][2]),
            'BC': self.calculate_ratio(points[-3][2], points[-2][2]),
            'CD': self.calculate_ratio(points[-2][2], points[-1][2])
        }
        
        completion = sum(
            1 - abs(current_ratios[leg] - target_ratios[leg])
            for leg in ['XA', 'AB', 'BC', 'CD']
        ) / 4
        
        return completion
        
    def estimate_reward_potential(self, points, pattern_type):
        """
        Schätzt das potenzielle Reward eines Musters.
        """
        if not points or not pattern_type:
            return 0
            
        # Muster-spezifische Projektion
        d_price = points[-1][2]
        c_price = points[-2][2]
        price_range = abs(d_price - c_price)
        
        # Projektion basierend auf Pattern-Typ
        if pattern_type in [PatternType.GARTLEY,
                           PatternType.BUTTERFLY]:
            return price_range * 1.27
        elif pattern_type in [PatternType.BAT,
                            PatternType.CRAB]:
            return price_range * 1.618
        else:
            return price_range
            
    def next(self):
        price = self.data.close[0]
        
        # Historie aktualisieren
        self.price_history.append(price)
        
        if len(self.price_history) >= self.p.lookback_period:
            # Swing-Punkte finden
            prices = list(self.price_history)
            new_swings = self.find_swing_points(prices)
            
            if new_swings:
                self.swing_points.extend(new_swings)
                
                # Auf letzte 5 Punkte beschränken
                if len(self.swing_points) > 5:
                    self.swing_points = self.swing_points[-5:]
                    
                # Pattern identifizieren
                pattern_type, quality = self.identify_pattern(
                    self.swing_points
                )
                
                if (pattern_type and
                    quality > self.p.quality_threshold):
                    self.current_pattern = pattern_type
                    
                    # Metriken berechnen
                    completion = self.calculate_completion(
                        self.swing_points,
                        pattern_type
                    )
                    
                    reward = self.estimate_reward_potential(
                        self.swing_points,
                        pattern_type
                    )
                    
                    # Linien aktualisieren
                    self.lines.pattern_signal[0] = (
                        1 if self.swing_points[-1][0] == 'low'
                        else -1 if self.swing_points[-1][0] == 'high'
                        else 0
                    )
                    self.lines.pattern_quality[0] = quality
                    self.lines.completion_level[0] = completion
                    self.lines.potential_reward[0] = reward
                    
                    # Trading Signal
                    if completion > 0.8:  # Pattern fast komplett
                        if (self.lines.pattern_signal[0] > 0 and
                            reward > price * self.p.pattern_threshold):
                            self.lines.signal[0] = 1  # Kaufsignal
                        elif (self.lines.pattern_signal[0] < 0 and
                              reward > price * self.p.pattern_threshold):
                            self.lines.signal[0] = -1  # Verkaufssignal
                        else:
                            self.lines.signal[0] = 0
                    else:
                        self.lines.signal[0] = 0
                else:
                    # Standardwerte
                    self.lines.pattern_signal[0] = 0
                    self.lines.pattern_quality[0] = 0
                    self.lines.completion_level[0] = 0
                    self.lines.potential_reward[0] = 0
                    self.lines.signal[0] = 0
            else:
                # Standardwerte
                self.lines.pattern_signal[0] = 0
                self.lines.pattern_quality[0] = 0
                self.lines.completion_level[0] = 0
                self.lines.potential_reward[0] = 0
                self.lines.signal[0] = 0
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'pattern_metrics': {
                'type': (
                    self.current_pattern.value
                    if self.current_pattern
                    else "None"
                ),
                'quality': self.lines.pattern_quality[0],
                'completion': self.lines.completion_level[0],
                'reward': self.lines.potential_reward[0]
            },
            'pattern_analysis': {
                'status': (
                    'complete'
                    if self.lines.completion_level[0] > 0.8
                    else 'forming'
                    if self.lines.completion_level[0] > 0.3
                    else 'initiating'
                ),
                'strength': (
                    'strong'
                    if self.lines.pattern_quality[0] > 0.8
                    else 'moderate'
                    if self.lines.pattern_quality[0] > 0.6
                    else 'weak'
                ),
                'reliability': (
                    'high'
                    if (self.lines.pattern_quality[0] > 0.8 and
                        self.lines.completion_level[0] > 0.8)
                    else 'moderate'
                    if (self.lines.pattern_quality[0] > 0.6 and
                        self.lines.completion_level[0] > 0.6)
                    else 'low'
                )
            },
            'reward_analysis': {
                'potential': (
                    'high'
                    if self.lines.potential_reward[0] >
                       self.data.close[0] * 0.02
                    else 'moderate'
                    if self.lines.potential_reward[0] >
                       self.data.close[0] * 0.01
                    else 'low'
                ),
                'risk_reward': (
                    self.lines.potential_reward[0] /
                    (self.data.close[0] * self.p.pattern_threshold)
                    if self.p.pattern_threshold > 0
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
                'confidence': (
                    self.lines.pattern_quality[0] *
                    self.lines.completion_level[0]
                )
            },
            'market_conditions': {
                'pattern_clarity': (
                    'clear'
                    if self.lines.pattern_quality[0] > 0.7
                    else 'unclear'
                ),
                'completion_status': (
                    'actionable'
                    if self.lines.completion_level[0] > 0.8
                    else 'developing'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.pattern_quality[0] > 0.7 and
                        self.lines.completion_level[0] > 0.8 and
                        self.lines.potential_reward[0] >
                        self.data.close[0] * 0.02)
                    else 'unfavorable'
                )
            }
        }
