import backtrader as bt
import numpy as np
from enum import Enum

class TrendState(Enum):
    STRONG_UP = 4
    UP = 3
    NEUTRAL = 2
    DOWN = 1
    STRONG_DOWN = 0

class HeikenAshiTrend(bt.Indicator):
    """
    Heiken Ashi Trend Indicator
    
    Ein fortgeschrittener Trendfolge-Indikator basierend auf Heiken Ashi
    mit zusätzlicher Trend-Analyse und Signalgenerierung.
    
    Features:
    - Trend-Stärke Klassifizierung
    - Momentum-Integration
    - Volumen-Analyse
    - Multi-Timeframe Signale
    - Adaptive Trendlinien
    
    Parameter:
    - fast_period (10): Schnelle EMA Periode
    - slow_period (20): Langsame EMA Periode
    - volume_period (14): Volumen-Analyse Periode
    - trend_strength_threshold (0.5): Schwelle für Trendstärke
    """
    
    lines = ('ha_trend', 'trend_strength', 'volume_trend',
             'fast_ma', 'slow_ma', 'momentum',
             'support', 'resistance',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 10),
        ('slow_period', 20),
        ('volume_period', 14),
        ('trend_strength_threshold', 0.5)
    )
    
    plotlines = dict(
        ha_trend=dict(color='blue', _name='HA Trend'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volume_trend=dict(color='purple', _name='Volume Trend'),
        fast_ma=dict(color='red', _name='Fast MA'),
        slow_ma=dict(color='orange', _name='Slow MA'),
        momentum=dict(color='brown', _name='Momentum'),
        support=dict(color='gray', _name='Support'),
        resistance=dict(color='gray', _name='Resistance'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(HeikenAshiTrend, self).__init__()
        
        # Basis Heiken Ashi
        self.ha_open = bt.indicators.HeikinAshi(self.data).open
        self.ha_high = bt.indicators.HeikinAshi(self.data).high
        self.ha_low = bt.indicators.HeikinAshi(self.data).low
        self.ha_close = bt.indicators.HeikinAshi(self.data).close
        
        # Moving Averages
        self.fast_ema = bt.indicators.EMA(
            self.ha_close, period=self.p.fast_period
        )
        self.slow_ema = bt.indicators.EMA(
            self.ha_close, period=self.p.slow_period
        )
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.volume_sma = bt.indicators.SMA(
            self.data.volume, period=self.p.volume_period
        )
        
        # Historie
        self.trend_history = []
        self.volume_history = []
        self.price_history = []
        
    def calculate_trend_state(self):
        """
        Bestimmt den aktuellen Trend-Zustand.
        """
        if len(self) < 2:
            return TrendState.NEUTRAL
            
        # Trend-Bestimmung
        price_trend = (
            1 if self.ha_close[0] > self.ha_open[0] else
            -1 if self.ha_close[0] < self.ha_open[0] else
            0
        )
        
        ma_trend = (
            1 if self.fast_ema[0] > self.slow_ema[0] else
            -1 if self.fast_ema[0] < self.slow_ema[0] else
            0
        )
        
        # Trendstärke
        strength = abs(self.ha_close[0] - self.ha_open[0]) / (
            self.ha_high[0] - self.ha_low[0]
            if self.ha_high[0] != self.ha_low[0]
            else 1
        )
        
        # Trend-Zustand bestimmen
        if price_trend > 0 and ma_trend > 0 and strength > self.p.trend_strength_threshold:
            return TrendState.STRONG_UP
        elif price_trend > 0 and ma_trend > 0:
            return TrendState.UP
        elif price_trend < 0 and ma_trend < 0 and strength > self.p.trend_strength_threshold:
            return TrendState.STRONG_DOWN
        elif price_trend < 0 and ma_trend < 0:
            return TrendState.DOWN
        else:
            return TrendState.NEUTRAL
            
    def calculate_volume_trend(self):
        """
        Analysiert den Volumen-Trend.
        """
        if len(self) < self.p.volume_period:
            return 0
            
        current_volume = self.data.volume[0]
        avg_volume = self.volume_sma[0]
        
        if avg_volume == 0:
            return 0
            
        # Volumen-Trend (-1 bis 1)
        volume_trend = (current_volume - avg_volume) / avg_volume
        
        return volume_trend
        
    def calculate_support_resistance(self):
        """
        Berechnet Support und Resistance Levels.
        """
        if len(self.price_history) < self.p.slow_period:
            return self.ha_low[0], self.ha_high[0]
            
        window = self.price_history[-self.p.slow_period:]
        
        # Lokale Extrema
        highs = [p for i, p in enumerate(window[1:-1])
                if p > window[i] and p > window[i+2]]
        lows = [p for i, p in enumerate(window[1:-1])
               if p < window[i] and p < window[i+2]]
               
        if not highs or not lows:
            return self.ha_low[0], self.ha_high[0]
            
        return min(lows), max(highs)
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.ha_close[0])
        if len(self.price_history) > self.p.slow_period * 2:
            self.price_history.pop(0)
            
        # Trend-Zustand
        trend_state = self.calculate_trend_state()
        self.lines.ha_trend[0] = trend_state.value
        
        # Moving Averages
        self.lines.fast_ma[0] = self.fast_ema[0]
        self.lines.slow_ma[0] = self.slow_ema[0]
        
        # Trendstärke
        strength = abs(self.ha_close[0] - self.ha_open[0]) / (
            self.ha_high[0] - self.ha_low[0]
            if self.ha_high[0] != self.ha_low[0]
            else 1
        )
        self.lines.trend_strength[0] = strength
        
        # Volumen-Trend
        self.lines.volume_trend[0] = self.calculate_volume_trend()
        
        # Support/Resistance
        support, resistance = self.calculate_support_resistance()
        self.lines.support[0] = support
        self.lines.resistance[0] = resistance
        
        # Momentum
        self.lines.momentum[0] = (
            self.ha_close[0] - self.ha_close[-1]
            if len(self) > 1 else 0
        )
        
        # Signal-Generierung
        # Buy Signal
        if (trend_state in [TrendState.STRONG_UP, TrendState.UP] and
            self.lines.volume_trend[0] > 0 and
            self.lines.momentum[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (trend_state in [TrendState.STRONG_DOWN, TrendState.DOWN] and
            self.lines.volume_trend[0] > 0 and
            self.lines.momentum[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'trend': {
                'state': TrendState(int(self.lines.ha_trend[0])).name,
                'strength': self.lines.trend_strength[0],
                'momentum': self.lines.momentum[0],
                'volume_trend': self.lines.volume_trend[0]
            },
            'levels': {
                'support': self.lines.support[0],
                'resistance': self.lines.resistance[0],
                'fast_ma': self.lines.fast_ma[0],
                'slow_ma': self.lines.slow_ma[0]
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'trend_quality': (
                    'strong' if self.lines.trend_strength[0] > self.p.trend_strength_threshold
                    else 'weak'
                ),
                'volume_confirmed': self.lines.volume_trend[0] > 0
            },
            'risk': {
                'atr': self.atr[0],
                'volatility': self.atr[0] / self.ha_close[0] if self.ha_close[0] != 0 else 0,
                'trend_stability': np.std([
                    x for x in self.trend_history[-self.p.slow_period:]
                ]) if self.trend_history else 0
            }
        }
