import backtrader as bt
import numpy as np
from enum import Enum

class TimeFrame(Enum):
    """Unterstützte Zeitrahmen"""
    M1 = bt.TimeFrame.Minutes
    M5 = bt.TimeFrame.Minutes * 5
    M15 = bt.TimeFrame.Minutes * 15
    M30 = bt.TimeFrame.Minutes * 30
    H1 = bt.TimeFrame.Minutes * 60
    H4 = bt.TimeFrame.Minutes * 240
    D1 = bt.TimeFrame.Days
    W1 = bt.TimeFrame.Weeks
    MN1 = bt.TimeFrame.Months

class TrendStrength(Enum):
    """Trendstärke-Klassifikation"""
    STRONG_UP = 3
    MODERATE_UP = 2
    WEAK_UP = 1
    NEUTRAL = 0
    WEAK_DOWN = -1
    MODERATE_DOWN = -2
    STRONG_DOWN = -3

class MultiTimeframeTrendFinder(bt.Indicator):
    """
    Multi Timeframe Trend Finder
    
    Ein fortgeschrittener Indikator zur Analyse von
    Trends über mehrere Zeitrahmen.
    
    Features:
    - Multi-Timeframe-Analyse
    - Trendstärke-Berechnung
    - Trend-Konsistenz-Prüfung
    - Konflikt-Erkennung
    - Adaptive Gewichtung
    
    Parameter:
    - timeframes: Liste der zu analysierenden Zeitrahmen
    - ema_periods: EMA-Perioden für jeden Zeitrahmen
    - weights: Gewichtung der Zeitrahmen
    """
    
    lines = ('trend_strength', 'consensus', 'volatility')
    params = (
        ('timeframes', [
            TimeFrame.M15.value,
            TimeFrame.H1.value,
            TimeFrame.H4.value,
            TimeFrame.D1.value
        ]),
        ('ema_periods', [20, 50, 100]),
        ('weights', [0.1, 0.2, 0.3, 0.4])  # Höhere Gewichtung für höhere TFs
    )
    
    plotlines = dict(
        trend_strength=dict(color='blue', _name='Trend Strength'),
        consensus=dict(color='green', _name='Consensus'),
        volatility=dict(color='red', _name='Volatility')
    )
    
    def __init__(self):
        super(MultiTimeframeTrendFinder, self).__init__()
        
        # Trend-Indikatoren für jeden Zeitrahmen
        self.trend_indicators = {}
        
        # EMAs für jeden Zeitrahmen
        self.emas = {}
        
        # Initialisierung der Indikatoren
        for tf in self.p.timeframes:
            self.trend_indicators[tf] = {}
            self.emas[tf] = {}
            
            # EMAs für verschiedene Perioden
            for period in self.p.ema_periods:
                self.emas[tf][period] = bt.indicators.EMA(
                    self.data(timeframe=tf),
                    period=period
                )
                
        # Volatilitätsindikator
        self.atr = bt.indicators.ATR(self.data)
        
    def calculate_trend_strength(self, tf_data, tf):
        """Berechnet die Trendstärke für einen Zeitrahmen"""
        strength = 0
        
        # EMA-Crossover-Analyse
        for i, period1 in enumerate(self.p.ema_periods[:-1]):
            for period2 in self.p.ema_periods[i+1:]:
                ema1 = self.emas[tf][period1][0]
                ema2 = self.emas[tf][period2][0]
                
                if ema1 > ema2:
                    strength += 1
                elif ema1 < ema2:
                    strength -= 1
                    
        # Preis vs. EMAs
        current_price = tf_data[0]
        for period in self.p.ema_periods:
            ema = self.emas[tf][period][0]
            if current_price > ema:
                strength += 0.5
            elif current_price < ema:
                strength -= 0.5
                
        return strength
        
    def calculate_consensus(self):
        """Berechnet den Trend-Konsens über alle Zeitrahmen"""
        weighted_strength = 0
        total_weight = sum(self.p.weights)
        
        for tf, weight in zip(self.p.timeframes, self.p.weights):
            tf_strength = self.trend_indicators[tf].get(
                'strength',
                0
            )
            weighted_strength += tf_strength * (weight / total_weight)
            
        return weighted_strength
        
    def next(self):
        # Trendstärke für jeden Zeitrahmen berechnen
        for tf in self.p.timeframes:
            tf_data = self.data(timeframe=tf)
            
            if len(tf_data) > max(self.p.ema_periods):
                strength = self.calculate_trend_strength(tf_data, tf)
                self.trend_indicators[tf]['strength'] = strength
                
        # Gesamtkonsens berechnen
        consensus = self.calculate_consensus()
        
        # Volatilität normalisieren
        volatility = self.atr[0] / self.data[0]
        
        # Linien aktualisieren
        self.lines.trend_strength[0] = consensus
        self.lines.consensus[0] = abs(consensus)
        self.lines.volatility[0] = volatility
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        consensus = self.lines.consensus[0]
        trend_strength = self.lines.trend_strength[0]
        volatility = self.lines.volatility[0]
        
        # Trendstärke klassifizieren
        if trend_strength > 2:
            trend_class = TrendStrength.STRONG_UP
        elif trend_strength > 1:
            trend_class = TrendStrength.MODERATE_UP
        elif trend_strength > 0:
            trend_class = TrendStrength.WEAK_UP
        elif trend_strength < -2:
            trend_class = TrendStrength.STRONG_DOWN
        elif trend_strength < -1:
            trend_class = TrendStrength.MODERATE_DOWN
        elif trend_strength < 0:
            trend_class = TrendStrength.WEAK_DOWN
        else:
            trend_class = TrendStrength.NEUTRAL
            
        # Trend-Konsistenz prüfen
        timeframe_conflicts = []
        for tf1_idx, tf1 in enumerate(self.p.timeframes[:-1]):
            for tf2 in self.p.timeframes[tf1_idx+1:]:
                if (self.trend_indicators[tf1]['strength'] *
                    self.trend_indicators[tf2]['strength'] < 0):
                    timeframe_conflicts.append((tf1, tf2))
                    
        return {
            'trend_analysis': {
                'strength': trend_class.name,
                'consensus': consensus,
                'volatility': volatility,
                'conflicts': len(timeframe_conflicts)
            },
            'timeframe_analysis': {
                tf: {
                    'strength': self.trend_indicators[tf]['strength']
                }
                for tf in self.p.timeframes
            },
            'trading_signals': {
                'primary_trend': (
                    'bullish' if trend_strength > 0
                    else 'bearish' if trend_strength < 0
                    else 'neutral'
                ),
                'confidence': abs(consensus),
                'volatility_regime': (
                    'high' if volatility > 0.02
                    else 'moderate' if volatility > 0.01
                    else 'low'
                )
            },
            'risk_assessment': {
                'trend_reliability': (
                    'high' if len(timeframe_conflicts) == 0
                    else 'moderate' if len(timeframe_conflicts) <= 2
                    else 'low'
                ),
                'market_condition': (
                    'trending' if abs(consensus) > 0.7
                    else 'ranging' if abs(consensus) < 0.3
                    else 'transitioning'
                ),
                'trading_environment': (
                    'favorable' if (
                        abs(consensus) > 0.7 and
                        len(timeframe_conflicts) == 0
                    )
                    else 'challenging' if (
                        abs(consensus) < 0.3 or
                        len(timeframe_conflicts) > 2
                    )
                    else 'neutral'
                )
            }
        }
