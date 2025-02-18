import backtrader as bt
import numpy as np
from enum import Enum
from typing import List, Tuple, Optional

class StochSignal(Enum):
    """Stochastic Signal Typen"""
    STRONG_BUY = "Strong Buy"
    BUY = "Buy"
    NEUTRAL = "Neutral"
    SELL = "Sell"
    STRONG_SELL = "Strong Sell"

class ZeroLagStochasticIndicator(bt.Indicator):
    """
    Zero Lag Stochastic Indicator
    
    Ein fortgeschrittener Stochastic-Indikator mit
    Verzögerungskorrektur.
    
    Features:
    - Verzögerungskorrektur
    - Adaptive Glättung
    - Momentum-Analyse
    - Divergenz-Erkennung
    
    Parameter:
    - period (14): Hauptperiode
    - smooth_k (3): %K Glättung
    - smooth_d (3): %D Glättung
    - zero_lag_factor (0.5): Verzögerungsfaktor
    """
    
    lines = ('k', 'd', 'momentum', 'strength')
    params = (
        ('period', 14),
        ('smooth_k', 3),
        ('smooth_d', 3),
        ('zero_lag_factor', 0.5),
    )
    
    plotlines = dict(
        k=dict(color='blue', _name='%K'),
        d=dict(color='red', _name='%D'),
        momentum=dict(color='green', _name='Momentum'),
        strength=dict(color='purple', _name='Strength')
    )
    
    def __init__(self):
        super(ZeroLagStochasticIndicator, self).__init__()
        
        # Preispuffer
        self.high_buffer = []
        self.low_buffer = []
        self.close_buffer = []
        
        # Stochastic-Komponenten
        self.k_values = []
        self.d_values = []
        
        # Momentum-Daten
        self.momentum_values = []
        
        # Divergenz-Daten
        self.divergence_data = []
        
    def calculate_zero_lag_ma(self, data: List[float],
                            period: int) -> float:
        """Berechnet MA mit Verzögerungskorrektur"""
        if len(data) < period:
            return data[-1] if data else 0
            
        # Standard MA
        ma = np.mean(data[-period:])
        
        # Verzögerungskorrektur
        lag_correction = (
            (ma - data[-period]) *
            self.p.zero_lag_factor
        )
        
        return ma + lag_correction
        
    def calculate_stochastic(self) -> Tuple[float, float]:
        """Berechnet Stochastic-Komponenten"""
        if len(self.close_buffer) < self.p.period:
            return 0, 0
            
        # Höchst-/Tiefstkurse
        high = max(self.high_buffer[-self.p.period:])
        low = min(self.low_buffer[-self.p.period:])
        
        # %K berechnen
        if high == low:
            raw_k = 50
        else:
            raw_k = 100 * (
                (self.close_buffer[-1] - low) /
                (high - low)
            )
            
        # %K glätten
        self.k_values.append(raw_k)
        if len(self.k_values) > self.p.period:
            self.k_values.pop(0)
            
        k = self.calculate_zero_lag_ma(
            self.k_values,
            self.p.smooth_k
        )
        
        # %D berechnen
        self.d_values.append(k)
        if len(self.d_values) > self.p.period:
            self.d_values.pop(0)
            
        d = self.calculate_zero_lag_ma(
            self.d_values,
            self.p.smooth_d
        )
        
        return k, d
        
    def calculate_momentum(self) -> float:
        """Berechnet das Momentum"""
        if len(self.k_values) < 5:
            return 0
            
        # Richtungsänderung
        k_change = (
            self.k_values[-1] -
            self.k_values[-5]
        )
        
        # Normalisierung
        max_change = max(
            abs(self.k_values[-1] - k)
            for k in self.k_values[-5:]
        )
        
        if max_change == 0:
            return 0
            
        return k_change / max_change
        
    def calculate_strength(self) -> float:
        """Berechnet die Signalstärke"""
        if len(self.k_values) < 5:
            return 0
            
        # Trend-Konsistenz
        k_direction = np.sign(
            self.k_values[-1] -
            self.k_values[-5]
        )
        
        consistency = sum(
            1 for i in range(1, 5)
            if np.sign(
                self.k_values[-i] -
                self.k_values[-i-1]
            ) == k_direction
        ) / 4
        
        # Momentum-Magnitude
        momentum = abs(self.calculate_momentum())
        
        # Position im Band
        band_position = abs(
            50 - self.k_values[-1]
        ) / 50
        
        # Kombinierte Stärke
        strength = (
            consistency * 0.4 +
            momentum * 0.3 +
            band_position * 0.3
        )
        
        return min(1.0, strength)
        
    def check_divergence(self) -> Optional[str]:
        """Prüft auf Divergenzen"""
        if len(self.close_buffer) < 10:
            return None
            
        # Preishochs/-tiefs
        price_high = max(self.close_buffer[-5:])
        price_low = min(self.close_buffer[-5:])
        prev_price_high = max(self.close_buffer[-10:-5])
        prev_price_low = min(self.close_buffer[-10:-5])
        
        # Stochastic-Hochs/-Tiefs
        stoch_high = max(self.k_values[-5:])
        stoch_low = min(self.k_values[-5:])
        prev_stoch_high = max(self.k_values[-10:-5])
        prev_stoch_low = min(self.k_values[-10:-5])
        
        # Bullische Divergenz
        if (price_low < prev_price_low and
            stoch_low > prev_stoch_low):
            return "bullish"
            
        # Bärische Divergenz
        if (price_high > prev_price_high and
            stoch_high < prev_stoch_high):
            return "bearish"
            
        return None
        
    def next(self):
        # Preisdaten sammeln
        self.high_buffer.append(self.data.high[0])
        self.low_buffer.append(self.data.low[0])
        self.close_buffer.append(self.data.close[0])
        
        if len(self.close_buffer) > self.p.period * 2:
            self.high_buffer.pop(0)
            self.low_buffer.pop(0)
            self.close_buffer.pop(0)
            
        # Stochastic berechnen
        k, d = self.calculate_stochastic()
        
        # Momentum berechnen
        momentum = self.calculate_momentum()
        self.momentum_values.append(momentum)
        if len(self.momentum_values) > self.p.period:
            self.momentum_values.pop(0)
            
        # Stärke berechnen
        strength = self.calculate_strength()
        
        # Divergenz prüfen
        divergence = self.check_divergence()
        self.divergence_data.append(divergence)
        if len(self.divergence_data) > self.p.period:
            self.divergence_data.pop(0)
            
        # Linien aktualisieren
        self.lines.k[0] = k
        self.lines.d[0] = d
        self.lines.momentum[0] = momentum
        self.lines.strength[0] = strength
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.k_values:
            return None
            
        current_k = self.lines.k[0]
        current_d = self.lines.d[0]
        current_momentum = self.lines.momentum[0]
        current_strength = self.lines.strength[0]
        
        return {
            'stochastic_analysis': {
                'k_value': current_k,
                'd_value': current_d,
                'momentum': current_momentum,
                'strength': current_strength,
                'position': (
                    'overbought' if current_k > 80
                    else 'oversold' if current_k < 20
                    else 'neutral'
                )
            },
            'signal_analysis': {
                'crossover': (
                    'bullish'
                    if (len(self.k_values) > 1 and
                        self.k_values[-2] < self.d_values[-2] and
                        current_k > current_d)
                    else 'bearish'
                    if (len(self.k_values) > 1 and
                        self.k_values[-2] > self.d_values[-2] and
                        current_k < current_d)
                    else 'none'
                ),
                'momentum': (
                    'increasing'
                    if current_momentum > 0
                    else 'decreasing'
                    if current_momentum < 0
                    else 'stable'
                ),
                'strength': (
                    'strong'
                    if current_strength > 0.7
                    else 'moderate'
                    if current_strength > 0.4
                    else 'weak'
                )
            },
            'divergence_analysis': {
                'type': (
                    self.divergence_data[-1]
                    if self.divergence_data else None
                ),
                'confirmation': (
                    'strong'
                    if (self.divergence_data[-1] and
                        current_strength > 0.7)
                    else 'moderate'
                    if (self.divergence_data[-1] and
                        current_strength > 0.4)
                    else 'weak'
                    if self.divergence_data[-1]
                    else 'none'
                )
            },
            'trend_analysis': {
                'primary': (
                    'strong_uptrend'
                    if (current_k > current_d and
                        current_momentum > 0.5 and
                        current_strength > 0.7)
                    else 'uptrend'
                    if current_k > current_d
                    else 'strong_downtrend'
                    if (current_k < current_d and
                        current_momentum < -0.5 and
                        current_strength > 0.7)
                    else 'downtrend'
                    if current_k < current_d
                    else 'neutral'
                ),
                'strength': current_strength,
                'momentum_quality': (
                    'high'
                    if abs(current_momentum) > 0.7
                    else 'moderate'
                    if abs(current_momentum) > 0.4
                    else 'low'
                )
            },
            'trading_signals': {
                'primary': (
                    StochSignal.STRONG_BUY.value
                    if (current_k < 20 and
                        current_k > current_d and
                        current_strength > 0.7)
                    else StochSignal.BUY.value
                    if current_k < 20 and current_k > current_d
                    else StochSignal.STRONG_SELL.value
                    if (current_k > 80 and
                        current_k < current_d and
                        current_strength > 0.7)
                    else StochSignal.SELL.value
                    if current_k > 80 and current_k < current_d
                    else StochSignal.NEUTRAL.value
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
                    if (abs(current_momentum) > 0.7 and
                        current_strength > 0.7)
                    else 'suboptimal'
                    if (abs(current_momentum) > 0.4 or
                        current_strength > 0.4)
                    else 'poor'
                )
            },
            'risk_assessment': {
                'signal_quality': (
                    'high'
                    if (current_strength > 0.7 and
                        not self.divergence_data[-1])
                    else 'moderate'
                    if current_strength > 0.4
                    else 'low'
                ),
                'reversal_risk': (
                    'high'
                    if (self.divergence_data[-1] or
                        (current_k > 80 and current_strength < 0.4) or
                        (current_k < 20 and current_strength < 0.4))
                    else 'moderate'
                    if current_strength < 0.4
                    else 'low'
                ),
                'volatility': (
                    'high'
                    if abs(current_momentum) > 0.7
                    else 'moderate'
                    if abs(current_momentum) > 0.4
                    else 'low'
                )
            }
        }
