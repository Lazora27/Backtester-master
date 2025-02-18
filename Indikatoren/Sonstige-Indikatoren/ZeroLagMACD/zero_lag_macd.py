import backtrader as bt
import numpy as np
from enum import Enum
from typing import List, Tuple

class SignalType(Enum):
    """MACD Signal Typen"""
    STRONG_BUY = "Strong Buy"
    BUY = "Buy"
    NEUTRAL = "Neutral"
    SELL = "Sell"
    STRONG_SELL = "Strong Sell"

class ZeroLagMACDIndicator(bt.Indicator):
    """
    Zero Lag MACD Indicator
    
    Ein fortgeschrittener MACD-Indikator mit
    Verzögerungskorrektur.
    
    Features:
    - Verzögerungskorrektur
    - Adaptive Glättung
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    
    Parameter:
    - fast_period (12): Schnelle Periode
    - slow_period (26): Langsame Periode
    - signal_period (9): Signal Periode
    - zero_lag_factor (0.5): Verzögerungsfaktor
    """
    
    lines = ('macd', 'signal', 'histogram', 'trend_strength')
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('zero_lag_factor', 0.5),
    )
    
    plotlines = dict(
        macd=dict(color='blue', _name='MACD'),
        signal=dict(color='red', _name='Signal'),
        histogram=dict(color='green', _name='Histogram'),
        trend_strength=dict(color='purple', _name='Strength')
    )
    
    def __init__(self):
        super(ZeroLagMACDIndicator, self).__init__()
        
        # Preispuffer
        self.price_buffer = []
        
        # MACD-Komponenten
        self.macd_values = []
        self.signal_values = []
        self.histogram_values = []
        
        # Divergenz-Daten
        self.divergence_data = []
        
        # Trendstärke-Daten
        self.strength_data = []
        
    def calculate_zero_lag_ema(self, data: List[float],
                             period: int) -> float:
        """Berechnet EMA mit Verzögerungskorrektur"""
        if len(data) < period:
            return data[-1] if data else 0
            
        # Standard EMA
        alpha = 2.0 / (period + 1)
        ema = data[-1]
        
        for i in range(2, period + 1):
            if i <= len(data):
                ema = (1 - alpha) * ema + alpha * data[-i]
                
        # Verzögerungskorrektur
        lag_correction = (
            (ema - data[-period]) *
            self.p.zero_lag_factor
        )
        
        return ema + lag_correction
        
    def calculate_macd(self) -> Tuple[float, float, float]:
        """Berechnet MACD-Komponenten"""
        if len(self.price_buffer) < self.p.slow_period:
            return 0, 0, 0
            
        # Fast & Slow EMAs
        fast_ema = self.calculate_zero_lag_ema(
            self.price_buffer,
            self.p.fast_period
        )
        slow_ema = self.calculate_zero_lag_ema(
            self.price_buffer,
            self.p.slow_period
        )
        
        # MACD Line
        macd_line = fast_ema - slow_ema
        
        # Signal Line
        self.macd_values.append(macd_line)
        if len(self.macd_values) > self.p.slow_period:
            self.macd_values.pop(0)
            
        signal_line = self.calculate_zero_lag_ema(
            self.macd_values,
            self.p.signal_period
        )
        
        # Histogram
        histogram = macd_line - signal_line
        
        return macd_line, signal_line, histogram
        
    def calculate_trend_strength(self) -> float:
        """Berechnet die Trendstärke"""
        if len(self.histogram_values) < 5:
            return 0
            
        # Histogramm-Analyse
        recent_hist = self.histogram_values[-5:]
        hist_direction = np.sign(recent_hist[-1])
        
        # Konsistenz
        direction_consistency = sum(
            1 for h in recent_hist
            if np.sign(h) == hist_direction
        ) / len(recent_hist)
        
        # Magnitude
        hist_magnitude = abs(recent_hist[-1]) / max(
            abs(h) for h in recent_hist
        )
        
        # Momentum
        hist_momentum = (
            (recent_hist[-1] - recent_hist[0]) /
            max(abs(h) for h in recent_hist)
        )
        
        # Kombinierte Stärke
        strength = (
            direction_consistency * 0.4 +
            hist_magnitude * 0.3 +
            abs(hist_momentum) * 0.3
        )
        
        return min(1.0, strength)
        
    def check_divergence(self) -> bool:
        """Prüft auf Divergenzen"""
        if len(self.price_buffer) < 10:
            return False
            
        # Preishochs/-tiefs
        price_high = max(self.price_buffer[-5:])
        price_low = min(self.price_buffer[-5:])
        prev_price_high = max(self.price_buffer[-10:-5])
        prev_price_low = min(self.price_buffer[-10:-5])
        
        # MACD-Hochs/-Tiefs
        macd_high = max(self.macd_values[-5:])
        macd_low = min(self.macd_values[-5:])
        prev_macd_high = max(self.macd_values[-10:-5])
        prev_macd_low = min(self.macd_values[-10:-5])
        
        # Bullische Divergenz
        bullish_div = (
            price_low < prev_price_low and
            macd_low > prev_macd_low
        )
        
        # Bärische Divergenz
        bearish_div = (
            price_high > prev_price_high and
            macd_high < prev_macd_high
        )
        
        return bullish_div or bearish_div
        
    def next(self):
        current_price = self.data.close[0]
        
        # Preispuffer aktualisieren
        self.price_buffer.append(current_price)
        if len(self.price_buffer) > self.p.slow_period * 2:
            self.price_buffer.pop(0)
            
        # MACD berechnen
        macd, signal, histogram = self.calculate_macd()
        
        # Komponenten speichern
        self.histogram_values.append(histogram)
        if len(self.histogram_values) > self.p.slow_period:
            self.histogram_values.pop(0)
            
        # Trendstärke berechnen
        strength = self.calculate_trend_strength()
        self.strength_data.append(strength)
        if len(self.strength_data) > self.p.slow_period:
            self.strength_data.pop(0)
            
        # Divergenz prüfen
        has_divergence = self.check_divergence()
        self.divergence_data.append(has_divergence)
        if len(self.divergence_data) > self.p.slow_period:
            self.divergence_data.pop(0)
            
        # Linien aktualisieren
        self.lines.macd[0] = macd
        self.lines.signal[0] = signal
        self.lines.histogram[0] = histogram
        self.lines.trend_strength[0] = strength
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.macd_values:
            return None
            
        current_macd = self.lines.macd[0]
        current_signal = self.lines.signal[0]
        current_histogram = self.lines.histogram[0]
        current_strength = self.lines.trend_strength[0]
        
        return {
            'macd_analysis': {
                'value': current_macd,
                'signal': current_signal,
                'histogram': current_histogram,
                'trend': (
                    'bullish'
                    if current_macd > current_signal
                    else 'bearish'
                    if current_macd < current_signal
                    else 'neutral'
                ),
                'strength': current_strength
            },
            'signal_analysis': {
                'crossover': (
                    'bullish'
                    if (len(self.macd_values) > 1 and
                        self.macd_values[-2] < self.signal_values[-2]
                        and current_macd > current_signal)
                    else 'bearish'
                    if (len(self.macd_values) > 1 and
                        self.macd_values[-2] > self.signal_values[-2]
                        and current_macd < current_signal)
                    else 'none'
                ),
                'momentum': (
                    'increasing'
                    if (len(self.histogram_values) > 1 and
                        current_histogram >
                        self.histogram_values[-2])
                    else 'decreasing'
                    if (len(self.histogram_values) > 1 and
                        current_histogram <
                        self.histogram_values[-2])
                    else 'stable'
                )
            },
            'divergence_analysis': {
                'present': any(self.divergence_data[-5:]),
                'type': (
                    'bullish'
                    if (self.divergence_data[-1] and
                        current_macd > current_signal)
                    else 'bearish'
                    if (self.divergence_data[-1] and
                        current_macd < current_signal)
                    else 'none'
                ),
                'strength': (
                    'strong'
                    if (self.divergence_data[-1] and
                        current_strength > 0.7)
                    else 'moderate'
                    if (self.divergence_data[-1] and
                        current_strength > 0.4)
                    else 'weak'
                )
            },
            'trend_analysis': {
                'primary': (
                    'strong_uptrend'
                    if (current_macd > 0 and
                        current_histogram > 0 and
                        current_strength > 0.7)
                    else 'uptrend'
                    if current_macd > 0
                    else 'strong_downtrend'
                    if (current_macd < 0 and
                        current_histogram < 0 and
                        current_strength > 0.7)
                    else 'downtrend'
                    if current_macd < 0
                    else 'neutral'
                ),
                'strength': current_strength,
                'reliability': (
                    'high'
                    if current_strength > 0.7
                    else 'moderate'
                    if current_strength > 0.4
                    else 'low'
                )
            },
            'trading_signals': {
                'primary': (
                    SignalType.STRONG_BUY.value
                    if (current_macd > current_signal and
                        current_strength > 0.7 and
                        not self.divergence_data[-1])
                    else SignalType.BUY.value
                    if current_macd > current_signal
                    else SignalType.STRONG_SELL.value
                    if (current_macd < current_signal and
                        current_strength > 0.7 and
                        not self.divergence_data[-1])
                    else SignalType.SELL.value
                    if current_macd < current_signal
                    else SignalType.NEUTRAL.value
                ),
                'confidence': (
                    'high'
                    if current_strength > 0.7
                    else 'moderate'
                    if current_strength > 0.4
                    else 'low'
                ),
                'timing': (
                    'optimal'
                    if (abs(current_histogram) > 
                        np.mean([abs(h) for h in
                                self.histogram_values[-5:]]))
                    else 'suboptimal'
                )
            },
            'risk_assessment': {
                'trend_stability': (
                    'high'
                    if (current_strength > 0.7 and
                        not self.divergence_data[-1])
                    else 'moderate'
                    if current_strength > 0.4
                    else 'low'
                ),
                'reversal_risk': (
                    'high'
                    if self.divergence_data[-1]
                    else 'moderate'
                    if current_strength < 0.4
                    else 'low'
                ),
                'volatility': (
                    'high'
                    if np.std(self.histogram_values[-5:]) >
                    np.mean([abs(h) for h in
                            self.histogram_values[-5:]])
                    else 'moderate'
                    if np.std(self.histogram_values[-5:]) >
                    np.mean([abs(h) for h in
                            self.histogram_values[-5:]]) * 0.5
                    else 'low'
                )
            }
        }
