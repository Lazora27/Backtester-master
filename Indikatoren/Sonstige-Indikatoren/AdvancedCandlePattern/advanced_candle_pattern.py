import backtrader as bt
import numpy as np
from enum import Enum
from collections import deque

class PatternType(Enum):
    """Pattern-Typen Enumeration"""
    DOJI = "Doji"
    HAMMER = "Hammer"
    SHOOTING_STAR = "Shooting Star"
    ENGULFING = "Engulfing"
    HARAMI = "Harami"
    MORNING_STAR = "Morning Star"
    EVENING_STAR = "Evening Star"
    THREE_WHITE_SOLDIERS = "Three White Soldiers"
    THREE_BLACK_CROWS = "Three Black Crows"
    PIERCING_LINE = "Piercing Line"
    DARK_CLOUD_COVER = "Dark Cloud Cover"

class AdvancedCandlePattern(bt.Indicator):
    """
    Advanced Candle Stick Pattern Indicator
    
    Ein fortgeschrittener Indikator zur Erkennung und
    Analyse von Candlestick-Mustern.
    
    Features:
    - Komplexe Mustererkennung
    - Qualitätsanalyse
    - Trendkontext
    - Volumenbestätigung
    
    Parameter:
    - pattern_threshold (0.7): Erkennungsschwelle
    - volume_factor (1.5): Volumenfaktor
    - trend_period (20): Trendperiode
    """
    
    lines = ('pattern_signal', 'pattern_strength',
             'trend_context', 'volume_confirmation',
             'signal')
             
    params = (
        ('pattern_threshold', 0.7),
        ('volume_factor', 1.5),
        ('trend_period', 20)
    )
    
    plotlines = dict(
        pattern_signal=dict(color='blue', _name='Pattern Signal'),
        pattern_strength=dict(color='green', _name='Pattern Strength'),
        trend_context=dict(color='red', _name='Trend Context'),
        volume_confirmation=dict(color='purple', _name='Volume Confirmation'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(AdvancedCandlePattern, self).__init__()
        
        # Pattern Tracking
        self.pattern_history = deque(maxlen=self.p.trend_period)
        self.volume_history = deque(maxlen=self.p.trend_period)
        self.trend_history = deque(maxlen=self.p.trend_period)
        
    def is_doji(self, open_price, close_price, high, low):
        """
        Erkennt Doji-Muster.
        """
        body = abs(close_price - open_price)
        total_range = high - low
        
        if total_range == 0:
            return False
            
        body_ratio = body / total_range
        return body_ratio < 0.1
        
    def is_hammer(self, open_price, close_price, high, low):
        """
        Erkennt Hammer-Muster.
        """
        body = abs(close_price - open_price)
        upper_shadow = high - max(open_price, close_price)
        lower_shadow = min(open_price, close_price) - low
        
        if body == 0:
            return False
            
        shadow_ratio = lower_shadow / body
        return (shadow_ratio > 2 and
                upper_shadow < body)
                
    def is_shooting_star(self, open_price, close_price, high, low):
        """
        Erkennt Shooting Star-Muster.
        """
        body = abs(close_price - open_price)
        upper_shadow = high - max(open_price, close_price)
        lower_shadow = min(open_price, close_price) - low
        
        if body == 0:
            return False
            
        shadow_ratio = upper_shadow / body
        return (shadow_ratio > 2 and
                lower_shadow < body)
                
    def is_engulfing(self, current, previous):
        """
        Erkennt Engulfing-Muster.
        """
        curr_body = abs(current['close'] - current['open'])
        prev_body = abs(previous['close'] - previous['open'])
        
        is_bullish = (
            current['close'] > current['open'] and
            previous['close'] < previous['open'] and
            current['close'] > previous['open'] and
            current['open'] < previous['close']
        )
        
        is_bearish = (
            current['close'] < current['open'] and
            previous['close'] > previous['open'] and
            current['close'] < previous['open'] and
            current['open'] > previous['close']
        )
        
        return (is_bullish or is_bearish,
                1 if is_bullish else -1 if is_bearish else 0)
                
    def calculate_pattern_strength(self, pattern_type, data):
        """
        Berechnet die Stärke eines Musters.
        """
        body = abs(data['close'] - data['open'])
        total_range = data['high'] - data['low']
        volume_ratio = (
            data['volume'] /
            np.mean(self.volume_history)
            if self.volume_history
            else 1
        )
        
        # Basisstärke
        if total_range == 0:
            return 0
            
        base_strength = body / total_range
        
        # Muster-spezifische Anpassungen
        if pattern_type == PatternType.DOJI:
            strength = 1 - base_strength
        elif pattern_type in [PatternType.HAMMER,
                            PatternType.SHOOTING_STAR]:
            strength = base_strength * 1.2
        elif pattern_type in [PatternType.ENGULFING,
                            PatternType.MORNING_STAR,
                            PatternType.EVENING_STAR]:
            strength = base_strength * 1.5
        else:
            strength = base_strength
            
        # Volumenbestätigung
        return strength * min(volume_ratio, 2.0)
        
    def analyze_trend_context(self):
        """
        Analysiert den Trendkontext.
        """
        if len(self.trend_history) < self.p.trend_period:
            return 0
            
        # Trendrichtung
        trend = np.polyfit(
            range(len(self.trend_history)),
            self.trend_history,
            1
        )[0]
        
        return trend
        
    def confirm_with_volume(self, current_volume):
        """
        Bestätigt Muster mit Volumen.
        """
        if not self.volume_history:
            return False
            
        avg_volume = np.mean(self.volume_history)
        return current_volume > avg_volume * self.p.volume_factor
        
    def next(self):
        # Aktuelle Candlestick-Daten
        current = {
            'open': self.data.open[0],
            'high': self.data.high[0],
            'low': self.data.low[0],
            'close': self.data.close[0],
            'volume': self.data.volume[0]
        }
        
        if len(self.data) > 1:
            previous = {
                'open': self.data.open[-1],
                'high': self.data.high[-1],
                'low': self.data.low[-1],
                'close': self.data.close[-1],
                'volume': self.data.volume[-1]
            }
        else:
            previous = current
            
        # Pattern-Erkennung
        pattern_signal = 0
        pattern_type = None
        
        # Doji
        if self.is_doji(
            current['open'],
            current['close'],
            current['high'],
            current['low']
        ):
            pattern_type = PatternType.DOJI
            pattern_signal = 0  # Neutral
            
        # Hammer
        elif self.is_hammer(
            current['open'],
            current['close'],
            current['high'],
            current['low']
        ):
            pattern_type = PatternType.HAMMER
            pattern_signal = 1  # Bullish
            
        # Shooting Star
        elif self.is_shooting_star(
            current['open'],
            current['close'],
            current['high'],
            current['low']
        ):
            pattern_type = PatternType.SHOOTING_STAR
            pattern_signal = -1  # Bearish
            
        # Engulfing
        else:
            is_engulfing, engulfing_signal = self.is_engulfing(
                current,
                previous
            )
            if is_engulfing:
                pattern_type = PatternType.ENGULFING
                pattern_signal = engulfing_signal
                
        # Pattern-Stärke
        if pattern_type:
            pattern_strength = self.calculate_pattern_strength(
                pattern_type,
                current
            )
        else:
            pattern_strength = 0
            
        # Trend-Kontext
        trend_context = self.analyze_trend_context()
        
        # Volumenbestätigung
        volume_confirmation = (
            1 if self.confirm_with_volume(current['volume'])
            else 0
        )
        
        # Historie aktualisieren
        self.pattern_history.append(pattern_signal)
        self.volume_history.append(current['volume'])
        self.trend_history.append(current['close'])
        
        # Linien aktualisieren
        self.lines.pattern_signal[0] = pattern_signal
        self.lines.pattern_strength[0] = pattern_strength
        self.lines.trend_context[0] = trend_context
        self.lines.volume_confirmation[0] = volume_confirmation
        
        # Trading Signal
        if (pattern_strength > self.p.pattern_threshold and
            volume_confirmation):
            if (pattern_signal > 0 and
                trend_context > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (pattern_signal < 0 and
                  trend_context < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'pattern_metrics': {
                'signal': self.lines.pattern_signal[0],
                'strength': self.lines.pattern_strength[0],
                'trend': self.lines.trend_context[0],
                'volume': self.lines.volume_confirmation[0]
            },
            'pattern_analysis': {
                'type': (
                    'bullish'
                    if self.lines.pattern_signal[0] > 0
                    else 'bearish'
                    if self.lines.pattern_signal[0] < 0
                    else 'neutral'
                ),
                'strength': (
                    'strong'
                    if self.lines.pattern_strength[0] >
                       self.p.pattern_threshold
                    else 'weak'
                ),
                'reliability': (
                    'high'
                    if (self.lines.pattern_strength[0] >
                        self.p.pattern_threshold and
                        self.lines.volume_confirmation[0])
                    else 'low'
                )
            },
            'trend_analysis': {
                'direction': (
                    'upward'
                    if self.lines.trend_context[0] > 0
                    else 'downward'
                    if self.lines.trend_context[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.trend_context[0]),
                'context': (
                    'supporting'
                    if (self.lines.pattern_signal[0] *
                        self.lines.trend_context[0] > 0)
                    else 'opposing'
                )
            },
            'volume_analysis': {
                'confirmation': (
                    'confirmed'
                    if self.lines.volume_confirmation[0]
                    else 'unconfirmed'
                ),
                'strength': (
                    'high'
                    if self.lines.volume_confirmation[0] > 1.5
                    else 'moderate'
                    if self.lines.volume_confirmation[0] > 1
                    else 'low'
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
                    self.lines.pattern_strength[0] *
                    self.lines.volume_confirmation[0]
                )
            },
            'market_conditions': {
                'pattern_quality': (
                    'high'
                    if self.lines.pattern_strength[0] >
                       self.p.pattern_threshold
                    else 'low'
                ),
                'trend_clarity': (
                    'clear'
                    if abs(self.lines.trend_context[0]) > 0.01
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.pattern_strength[0] >
                        self.p.pattern_threshold and
                        self.lines.volume_confirmation[0])
                    else 'unfavorable'
                )
            }
        }
