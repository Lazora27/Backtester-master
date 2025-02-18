import backtrader as bt
import numpy as np
from enum import Enum
from typing import List, Dict, Optional

class StopType(Enum):
    """Trailing Stop Typen"""
    LONG = "Long"
    SHORT = "Short"
    NONE = "None"

class ATRTrailingStopIndicator(bt.Indicator):
    """
    ATR Trailing Stop Indicator
    
    Ein fortgeschrittener Indikator für adaptive
    Trailing Stops basierend auf ATR.
    
    Features:
    - Adaptive Stop-Levels
    - Trendbasierte Anpassung
    - Volatilitätsfilter
    - Risikomanagement
    
    Parameter:
    - atr_period (14): ATR Periode
    - atr_multiplier (2.0): ATR Multiplikator
    - trend_filter (True): Trendfilter aktivieren
    - risk_factor (1.0): Risikofaktor
    """
    
    lines = ('stop_level', 'stop_distance', 'risk_level',
             'volatility')
    params = (
        ('atr_period', 14),
        ('atr_multiplier', 2.0),
        ('trend_filter', True),
        ('risk_factor', 1.0),
    )
    
    plotlines = dict(
        stop_level=dict(color='red', _name='Stop'),
        stop_distance=dict(color='blue', _name='Distance'),
        risk_level=dict(color='green', _name='Risk'),
        volatility=dict(color='purple', _name='Volatility')
    )
    
    def __init__(self):
        super(ATRTrailingStopIndicator, self).__init__()
        
        # ATR berechnen
        self.atr = bt.indicators.ATR(
            self.data,
            period=self.p.atr_period
        )
        
        # Preispuffer
        self.price_buffer = []
        
        # Stop-Level Historie
        self.stop_history = []
        
        # Trend-Daten
        self.trend_data = []
        
        # Volatilitäts-Historie
        self.volatility_history = []
        
    def calculate_true_range(self) -> float:
        """Berechnet True Range"""
        if len(self.price_buffer) < 2:
            return 0
            
        high = self.data.high[0]
        low = self.data.low[0]
        prev_close = self.price_buffer[-2]
        
        return max(
            high - low,
            abs(high - prev_close),
            abs(low - prev_close)
        )
        
    def calculate_stop_level(self, current_price: float,
                           current_atr: float) -> float:
        """Berechnet Stop-Level"""
        if not self.stop_history:
            return current_price - (
                current_atr * self.p.atr_multiplier *
                self.p.risk_factor
            )
            
        prev_stop = self.stop_history[-1]
        new_stop = current_price - (
            current_atr * self.p.atr_multiplier *
            self.p.risk_factor
        )
        
        return max(prev_stop, new_stop)
        
    def calculate_trend(self) -> Optional[StopType]:
        """Bestimmt den aktuellen Trend"""
        if len(self.price_buffer) < 20:
            return None
            
        # Einfacher MA
        ma20 = np.mean(self.price_buffer[-20:])
        current_price = self.price_buffer[-1]
        
        if current_price > ma20:
            return StopType.LONG
        elif current_price < ma20:
            return StopType.SHORT
            
        return StopType.NONE
        
    def calculate_volatility(self, current_atr: float) -> float:
        """Berechnet normalisierte Volatilität"""
        if len(self.volatility_history) < self.p.atr_period:
            return 0
            
        avg_atr = np.mean(self.volatility_history)
        if avg_atr == 0:
            return 0
            
        return current_atr / avg_atr
        
    def calculate_risk_level(self, stop_distance: float,
                           volatility: float) -> float:
        """Berechnet Risikolevel"""
        if not self.price_buffer:
            return 0
            
        current_price = self.price_buffer[-1]
        
        # Basis-Risiko
        base_risk = stop_distance / current_price
        
        # Volatilitäts-Adjustierung
        vol_factor = min(2.0, max(0.5, volatility))
        
        return base_risk * vol_factor
        
    def next(self):
        current_price = self.data.close[0]
        
        # Puffer aktualisieren
        self.price_buffer.append(current_price)
        if len(self.price_buffer) > self.p.atr_period * 2:
            self.price_buffer.pop(0)
            
        # True Range berechnen
        tr = self.calculate_true_range()
        
        # ATR aktualisieren
        current_atr = self.atr[0]
        self.volatility_history.append(current_atr)
        if len(self.volatility_history) > self.p.atr_period:
            self.volatility_history.pop(0)
            
        # Trend bestimmen
        current_trend = self.calculate_trend()
        self.trend_data.append(current_trend)
        if len(self.trend_data) > self.p.atr_period:
            self.trend_data.pop(0)
            
        # Stop-Level berechnen
        if (not self.p.trend_filter or
            current_trend == StopType.LONG):
            stop_level = self.calculate_stop_level(
                current_price,
                current_atr
            )
        else:
            stop_level = (
                self.stop_history[-1]
                if self.stop_history
                else current_price - current_atr *
                self.p.atr_multiplier
            )
            
        self.stop_history.append(stop_level)
        if len(self.stop_history) > self.p.atr_period:
            self.stop_history.pop(0)
            
        # Stop-Distanz
        stop_distance = current_price - stop_level
        
        # Volatilität
        volatility = self.calculate_volatility(current_atr)
        
        # Risikolevel
        risk_level = self.calculate_risk_level(
            stop_distance,
            volatility
        )
        
        # Linien aktualisieren
        self.lines.stop_level[0] = stop_level
        self.lines.stop_distance[0] = stop_distance
        self.lines.risk_level[0] = risk_level
        self.lines.volatility[0] = volatility
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.price_buffer:
            return None
            
        current_price = self.price_buffer[-1]
        current_stop = self.stop_history[-1]
        current_distance = current_price - current_stop
        current_volatility = self.lines.volatility[0]
        current_risk = self.lines.risk_level[0]
        
        return {
            'stop_analysis': {
                'current_level': current_stop,
                'distance': current_distance,
                'distance_percent': (
                    current_distance / current_price * 100
                ),
                'trend_aligned': (
                    self.trend_data[-1] == StopType.LONG
                    if self.trend_data else None
                )
            },
            'risk_analysis': {
                'current_risk': current_risk,
                'risk_category': (
                    'high'
                    if current_risk > 0.05
                    else 'moderate'
                    if current_risk > 0.02
                    else 'low'
                ),
                'stop_quality': (
                    'optimal'
                    if (current_distance > 0 and
                        current_risk < 0.03)
                    else 'acceptable'
                    if (current_distance > 0 and
                        current_risk < 0.05)
                    else 'risky'
                )
            },
            'volatility_analysis': {
                'current_level': current_volatility,
                'trend': (
                    'increasing'
                    if (len(self.volatility_history) > 1 and
                        current_volatility >
                        np.mean(self.volatility_history[:-1]))
                    else 'decreasing'
                    if (len(self.volatility_history) > 1 and
                        current_volatility <
                        np.mean(self.volatility_history[:-1]))
                    else 'stable'
                ),
                'stability': (
                    'high'
                    if (len(self.volatility_history) > 5 and
                        np.std(self.volatility_history[-5:]) <
                        np.mean(self.volatility_history[-5:]) * 0.1)
                    else 'moderate'
                    if (len(self.volatility_history) > 5 and
                        np.std(self.volatility_history[-5:]) <
                        np.mean(self.volatility_history[-5:]) * 0.2)
                    else 'low'
                )
            },
            'trend_analysis': {
                'current_trend': (
                    self.trend_data[-1].value
                    if self.trend_data else None
                ),
                'strength': (
                    'strong'
                    if (len(self.trend_data) > 5 and
                        all(t == self.trend_data[-1]
                            for t in self.trend_data[-5:]))
                    else 'moderate'
                    if (len(self.trend_data) > 5 and
                        sum(1 for t in self.trend_data[-5:]
                            if t == self.trend_data[-1]) >= 3)
                    else 'weak'
                ),
                'consistency': (
                    'high'
                    if (len(self.trend_data) > 10 and
                        sum(1 for t in self.trend_data[-10:]
                            if t == self.trend_data[-1]) >= 8)
                    else 'moderate'
                    if (len(self.trend_data) > 10 and
                        sum(1 for t in self.trend_data[-10:]
                            if t == self.trend_data[-1]) >= 6)
                    else 'low'
                )
            },
            'trading_signals': {
                'stop_status': (
                    'active'
                    if current_price > current_stop
                    else 'triggered'
                ),
                'risk_warning': (
                    'high'
                    if current_risk > 0.05
                    else 'moderate'
                    if current_risk > 0.02
                    else 'low'
                ),
                'adjustment_needed': (
                    'immediate'
                    if (current_distance < 0 or
                        current_risk > 0.05)
                    else 'consider'
                    if current_risk > 0.03
                    else 'none'
                )
            },
            'position_management': {
                'stop_adjustment': (
                    'tighten'
                    if (current_risk > 0.05 or
                        current_volatility < 0.8)
                    else 'loosen'
                    if (current_risk < 0.02 and
                        current_volatility > 1.2)
                    else 'maintain'
                ),
                'risk_management': {
                    'position_size': (
                        'reduce'
                        if current_risk > 0.05
                        else 'increase'
                        if current_risk < 0.02
                        else 'maintain'
                    ),
                    'stop_width': (
                        'narrow'
                        if current_volatility < 0.8
                        else 'widen'
                        if current_volatility > 1.2
                        else 'maintain'
                    )
                }
            }
        }
