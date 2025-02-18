import backtrader as bt
import numpy as np
from enum import Enum

class TrendState(Enum):
    """Trend-Zustände"""
    STRONG_UP = "Strong Uptrend"
    UP = "Uptrend"
    NEUTRAL = "Neutral"
    DOWN = "Downtrend"
    STRONG_DOWN = "Strong Downtrend"

class VWAPBands(bt.Indicator):
    """
    VWAP Bands Indicator
    
    Ein fortgeschrittener Indikator, der VWAP-basierte
    Handelsbänder berechnet.
    
    Features:
    - Standard VWAP
    - Dynamische Bänder
    - Trend-Stärke-Analyse
    - Volumen-Profile
    - Preisabweichungen
    
    Parameter:
    - period (20): VWAP-Periode
    - num_stds (2): Anzahl Standardabweichungen
    - band_multiplier (1.0): Band-Multiplikator
    """
    
    lines = ('vwap', 'upper', 'lower', 'trend')
    params = (
        ('period', 20),
        ('num_stds', 2),
        ('band_multiplier', 1.0),
    )
    
    plotlines = dict(
        vwap=dict(color='blue', _name='VWAP'),
        upper=dict(color='red', _name='Upper Band'),
        lower=dict(color='green', _name='Lower Band'),
        trend=dict(color='purple', _name='Trend')
    )
    
    def __init__(self):
        super(VWAPBands, self).__init__()
        
        # Preis- und Volumenpuffer
        self.price_buffer = []
        self.volume_buffer = []
        self.vwap_buffer = []
        
        # Standardabweichungspuffer
        self.std_buffer = []
        
        # Trend-Tracking
        self.trend_history = []
        
    def calculate_vwap(self):
        """Berechnet VWAP und Standardabweichung"""
        if not self.price_buffer:
            return 0, 0
            
        # Typische Preise
        typical_prices = [
            (p['high'] + p['low'] + p['close']) / 3
            for p in self.price_buffer
        ]
        
        # Volumen
        volumes = [v for v in self.volume_buffer]
        
        # VWAP
        vwap = np.average(
            typical_prices,
            weights=volumes
        )
        
        # Standardabweichung
        variance = np.average(
            [(p - vwap) ** 2 for p in typical_prices],
            weights=volumes
        )
        std = np.sqrt(variance)
        
        return vwap, std
        
    def calculate_trend_strength(self, price, vwap):
        """Berechnet Trendstärke"""
        if not self.vwap_buffer:
            return 0
            
        # Preisabweichung von VWAP
        deviation = (price - vwap) / vwap
        
        # Trendstärke basierend auf Historie
        trend = 0
        if len(self.vwap_buffer) > 1:
            vwap_slope = (
                self.vwap_buffer[-1] -
                self.vwap_buffer[0]
            ) / len(self.vwap_buffer)
            
            trend = vwap_slope / vwap * 100
            
        # Kombinierte Stärke
        strength = (
            deviation * 0.7 +
            trend * 0.3
        )
        
        return strength
        
    def get_trend_state(self, strength):
        """Bestimmt Trend-Zustand"""
        if strength > 0.02:
            return TrendState.STRONG_UP
        elif strength > 0.01:
            return TrendState.UP
        elif strength < -0.02:
            return TrendState.STRONG_DOWN
        elif strength < -0.01:
            return TrendState.DOWN
        else:
            return TrendState.NEUTRAL
            
    def next(self):
        # Preisdaten sammeln
        price_data = {
            'high': self.data.high[0],
            'low': self.data.low[0],
            'close': self.data.close[0]
        }
        
        # Puffer aktualisieren
        self.price_buffer.append(price_data)
        self.volume_buffer.append(self.data.volume[0])
        
        if len(self.price_buffer) > self.p.period:
            self.price_buffer.pop(0)
            self.volume_buffer.pop(0)
            
        # VWAP und Standardabweichung berechnen
        vwap, std = self.calculate_vwap()
        
        # VWAP-Historie aktualisieren
        self.vwap_buffer.append(vwap)
        if len(self.vwap_buffer) > self.p.period:
            self.vwap_buffer.pop(0)
            
        # Bänder berechnen
        upper = vwap + (
            std * self.p.num_stds * self.p.band_multiplier
        )
        lower = vwap - (
            std * self.p.num_stds * self.p.band_multiplier
        )
        
        # Trendstärke berechnen
        trend_strength = self.calculate_trend_strength(
            self.data.close[0],
            vwap
        )
        
        # Trend-Historie aktualisieren
        self.trend_history.append(trend_strength)
        if len(self.trend_history) > self.p.period:
            self.trend_history.pop(0)
            
        # Linien aktualisieren
        self.lines.vwap[0] = vwap
        self.lines.upper[0] = upper
        self.lines.lower[0] = lower
        self.lines.trend[0] = trend_strength
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_price = self.data.close[0]
        current_vwap = self.lines.vwap[0]
        current_upper = self.lines.upper[0]
        current_lower = self.lines.lower[0]
        current_trend = self.lines.trend[0]
        
        # Trend-Zustand
        trend_state = self.get_trend_state(current_trend)
        
        # Preisposition relativ zu Bändern
        if current_price > current_upper:
            position = "above_bands"
        elif current_price < current_lower:
            position = "below_bands"
        else:
            position = "inside_bands"
            
        return {
            'vwap_analysis': {
                'value': current_vwap,
                'deviation': (
                    (current_price - current_vwap) /
                    current_vwap
                ),
                'band_width': (
                    current_upper - current_lower
                )
            },
            'trend_analysis': {
                'state': trend_state.value,
                'strength': abs(current_trend),
                'direction': (
                    'up' if current_trend > 0
                    else 'down' if current_trend < 0
                    else 'neutral'
                )
            },
            'price_position': {
                'location': position,
                'relative_strength': (
                    (current_price - current_vwap) /
                    (current_upper - current_vwap)
                    if current_price > current_vwap
                    else (current_price - current_vwap) /
                    (current_vwap - current_lower)
                )
            },
            'volatility': {
                'band_expansion': (
                    'expanding'
                    if len(self.std_buffer) > 1 and
                    self.std_buffer[-1] > self.std_buffer[-2]
                    else 'contracting'
                    if len(self.std_buffer) > 1 and
                    self.std_buffer[-1] < self.std_buffer[-2]
                    else 'stable'
                ),
                'relative_vol': (
                    (current_upper - current_lower) /
                    current_vwap
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (position == "below_bands" and
                        trend_state in [TrendState.UP,
                                      TrendState.STRONG_UP])
                    else 'buy'
                    if (position == "inside_bands" and
                        trend_state == TrendState.UP)
                    else 'strong_sell'
                    if (position == "above_bands" and
                        trend_state in [TrendState.DOWN,
                                      TrendState.STRONG_DOWN])
                    else 'sell'
                    if (position == "inside_bands" and
                        trend_state == TrendState.DOWN)
                    else 'neutral'
                ),
                'strength': (
                    'high' if abs(current_trend) > 0.02
                    else 'moderate' if abs(current_trend) > 0.01
                    else 'low'
                ),
                'reliability': (
                    'high'
                    if (abs(current_trend) > 0.02 and
                        position in ["above_bands",
                                   "below_bands"])
                    else 'moderate'
                    if abs(current_trend) > 0.01
                    else 'low'
                )
            }
        }
