import backtrader as bt
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional

class VSASignal(Enum):
    """Volume Spread Analysis Signale"""
    NO_DEMAND = "No Demand"
    NO_SUPPLY = "No Supply"
    EFFORT_UP = "Effort Up"
    EFFORT_DOWN = "Effort Down"
    STOPPING_VOLUME = "Stopping Volume"
    CLIMACTIC_ACTION = "Climactic Action"
    NEUTRAL = "Neutral"

@dataclass
class VSABar:
    """Repräsentiert einen VSA-Balken"""
    open: float
    high: float
    low: float
    close: float
    volume: float
    spread: float
    close_location: float
    signal: VSASignal

class WyckoffVolumeSpreadIndicator(bt.Indicator):
    """
    Wyckoff Volume Spread Analysis Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    Volumen-Spread-Beziehungen nach Wyckoff.
    
    Features:
    - VSA-Signale
    - Volumenanalyse
    - Spread-Analyse
    - Preisposition-Analyse
    
    Parameter:
    - volume_threshold (1.5): Volumenschwelle
    - spread_threshold (1.2): Spread-Schwelle
    - lookback (20): Rückblickperiode
    """
    
    lines = ('signal', 'strength', 'spread_ratio',
             'volume_ratio')
    params = (
        ('volume_threshold', 1.5),
        ('spread_threshold', 1.2),
        ('lookback', 20),
    )
    
    plotlines = dict(
        signal=dict(color='blue', _name='Signal'),
        strength=dict(color='red', _name='Strength'),
        spread_ratio=dict(color='green', _name='Spread'),
        volume_ratio=dict(color='purple', _name='Volume')
    )
    
    def __init__(self):
        super(WyckoffVolumeSpreadIndicator, self).__init__()
        
        # VSA-Balken
        self.bars: List[VSABar] = []
        
        # Volumen- und Spread-Statistiken
        self.volume_stats = []
        self.spread_stats = []
        
        # Signal-Historie
        self.signal_history = []
        
    def calculate_spread(self, high: float, low: float) -> float:
        """Berechnet den Spread eines Balkens"""
        return high - low
        
    def calculate_close_location(self, open: float, high: float,
                               low: float, close: float) -> float:
        """Berechnet die relative Position des Schlusskurses"""
        if high == low:
            return 0.5
            
        return (close - low) / (high - low)
        
    def analyze_volume(self, volume: float) -> float:
        """Analysiert das Volumen relativ zum Durchschnitt"""
        if len(self.volume_stats) < self.p.lookback:
            return 1.0
            
        avg_volume = np.mean(self.volume_stats[-self.p.lookback:])
        return volume / avg_volume if avg_volume > 0 else 1.0
        
    def analyze_spread(self, spread: float) -> float:
        """Analysiert den Spread relativ zum Durchschnitt"""
        if len(self.spread_stats) < self.p.lookback:
            return 1.0
            
        avg_spread = np.mean(self.spread_stats[-self.p.lookback:])
        return spread / avg_spread if avg_spread > 0 else 1.0
        
    def identify_signal(self, bar: VSABar) -> VSASignal:
        """Identifiziert das VSA-Signal"""
        # Relative Werte berechnen
        volume_ratio = self.analyze_volume(bar.volume)
        spread_ratio = self.analyze_spread(bar.spread)
        
        # Preisbewegung
        price_change = bar.close - bar.open
        is_up_bar = price_change > 0
        
        # No Demand
        if (is_up_bar and
            volume_ratio < 0.8 and
            spread_ratio < 0.8):
            return VSASignal.NO_DEMAND
            
        # No Supply
        if (not is_up_bar and
            volume_ratio < 0.8 and
            spread_ratio < 0.8):
            return VSASignal.NO_SUPPLY
            
        # Effort Up
        if (is_up_bar and
            volume_ratio > self.p.volume_threshold and
            spread_ratio > self.p.spread_threshold):
            return VSASignal.EFFORT_UP
            
        # Effort Down
        if (not is_up_bar and
            volume_ratio > self.p.volume_threshold and
            spread_ratio > self.p.spread_threshold):
            return VSASignal.EFFORT_DOWN
            
        # Stopping Volume
        if (not is_up_bar and
            volume_ratio > self.p.volume_threshold and
            bar.close_location > 0.7):
            return VSASignal.STOPPING_VOLUME
            
        # Climactic Action
        if (volume_ratio > self.p.volume_threshold * 1.5 and
            spread_ratio > self.p.spread_threshold * 1.5):
            return VSASignal.CLIMACTIC_ACTION
            
        return VSASignal.NEUTRAL
        
    def calculate_signal_strength(self, signal: VSASignal,
                                volume_ratio: float,
                                spread_ratio: float) -> float:
        """Berechnet die Signalstärke"""
        if signal == VSASignal.NEUTRAL:
            return 0.0
            
        # Basisstärke
        base_strength = (volume_ratio + spread_ratio) / 2
        
        # Signalspezifische Modifikationen
        if signal in [VSASignal.EFFORT_UP, VSASignal.EFFORT_DOWN]:
            return min(1.0, base_strength * 1.2)
        elif signal == VSASignal.CLIMACTIC_ACTION:
            return min(1.0, base_strength * 1.5)
        elif signal in [VSASignal.NO_DEMAND, VSASignal.NO_SUPPLY]:
            return min(1.0, (2 - base_strength) * 0.8)
        elif signal == VSASignal.STOPPING_VOLUME:
            return min(1.0, base_strength * 1.1)
            
        return min(1.0, base_strength)
        
    def next(self):
        # Balkendaten sammeln
        current_spread = self.calculate_spread(
            self.data.high[0],
            self.data.low[0]
        )
        
        current_close_loc = self.calculate_close_location(
            self.data.open[0],
            self.data.high[0],
            self.data.low[0],
            self.data.close[0]
        )
        
        # Neuen VSA-Balken erstellen
        new_bar = VSABar(
            open=self.data.open[0],
            high=self.data.high[0],
            low=self.data.low[0],
            close=self.data.close[0],
            volume=self.data.volume[0],
            spread=current_spread,
            close_location=current_close_loc,
            signal=VSASignal.NEUTRAL
        )
        
        # Statistiken aktualisieren
        self.volume_stats.append(new_bar.volume)
        self.spread_stats.append(new_bar.spread)
        
        if len(self.volume_stats) > self.p.lookback * 2:
            self.volume_stats.pop(0)
            self.spread_stats.pop(0)
            
        # Volumen und Spread analysieren
        volume_ratio = self.analyze_volume(new_bar.volume)
        spread_ratio = self.analyze_spread(new_bar.spread)
        
        # Signal identifizieren
        signal = self.identify_signal(new_bar)
        new_bar.signal = signal
        
        # Signalstärke berechnen
        strength = self.calculate_signal_strength(
            signal,
            volume_ratio,
            spread_ratio
        )
        
        # Balken speichern
        self.bars.append(new_bar)
        if len(self.bars) > self.p.lookback * 2:
            self.bars.pop(0)
            
        # Signal-Historie aktualisieren
        self.signal_history.append(signal)
        if len(self.signal_history) > self.p.lookback:
            self.signal_history.pop(0)
            
        # Linien aktualisieren
        self.lines.signal[0] = signal.value
        self.lines.strength[0] = strength
        self.lines.spread_ratio[0] = spread_ratio
        self.lines.volume_ratio[0] = volume_ratio
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.bars:
            return None
            
        current_bar = self.bars[-1]
        
        return {
            'current_signal': {
                'type': current_bar.signal.value,
                'strength': self.lines.strength[0],
                'reliability': (
                    'high'
                    if self.lines.strength[0] > 0.8
                    else 'moderate'
                    if self.lines.strength[0] > 0.5
                    else 'low'
                )
            },
            'volume_analysis': {
                'current_ratio': self.lines.volume_ratio[0],
                'trend': (
                    'increasing'
                    if (len(self.volume_stats) > 1 and
                        np.mean(self.volume_stats[-5:]) >
                        np.mean(self.volume_stats[-10:-5]))
                    else 'decreasing'
                    if (len(self.volume_stats) > 1 and
                        np.mean(self.volume_stats[-5:]) <
                        np.mean(self.volume_stats[-10:-5]))
                    else 'neutral'
                ),
                'consistency': (
                    'high'
                    if np.std(self.volume_stats[-10:]) <
                    np.mean(self.volume_stats[-10:]) * 0.5
                    else 'moderate'
                    if np.std(self.volume_stats[-10:]) <
                    np.mean(self.volume_stats[-10:])
                    else 'low'
                )
            },
            'spread_analysis': {
                'current_ratio': self.lines.spread_ratio[0],
                'trend': (
                    'widening'
                    if (len(self.spread_stats) > 1 and
                        np.mean(self.spread_stats[-5:]) >
                        np.mean(self.spread_stats[-10:-5]))
                    else 'narrowing'
                    if (len(self.spread_stats) > 1 and
                        np.mean(self.spread_stats[-5:]) <
                        np.mean(self.spread_stats[-10:-5]))
                    else 'stable'
                ),
                'volatility': (
                    'high'
                    if np.std(self.spread_stats[-10:]) >
                    np.mean(self.spread_stats[-10:])
                    else 'moderate'
                    if np.std(self.spread_stats[-10:]) >
                    np.mean(self.spread_stats[-10:]) * 0.5
                    else 'low'
                )
            },
            'signal_statistics': {
                'signal_distribution': {
                    signal.value: (
                        sum(1 for s in self.signal_history
                            if s == signal) /
                        len(self.signal_history)
                    )
                    for signal in VSASignal
                },
                'trend_strength': (
                    'strong'
                    if (sum(1 for s in self.signal_history[-5:]
                           if s in [VSASignal.EFFORT_UP,
                                  VSASignal.EFFORT_DOWN]) >= 3)
                    else 'moderate'
                    if (sum(1 for s in self.signal_history[-5:]
                           if s != VSASignal.NEUTRAL) >= 3)
                    else 'weak'
                ),
                'signal_quality': (
                    'improving'
                    if (np.mean([
                        self.calculate_signal_strength(
                            s,
                            self.lines.volume_ratio[0],
                            self.lines.spread_ratio[0]
                        )
                        for s in self.signal_history[-5:]
                    ]) > np.mean([
                        self.calculate_signal_strength(
                            s,
                            self.lines.volume_ratio[0],
                            self.lines.spread_ratio[0]
                        )
                        for s in self.signal_history[-10:-5]
                    ]))
                    else 'deteriorating'
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (current_bar.signal in
                        [VSASignal.EFFORT_UP,
                         VSASignal.STOPPING_VOLUME] and
                        self.lines.strength[0] > 0.8)
                    else 'buy'
                    if (current_bar.signal in
                        [VSASignal.EFFORT_UP,
                         VSASignal.STOPPING_VOLUME] and
                        self.lines.strength[0] > 0.5)
                    else 'strong_sell'
                    if (current_bar.signal in
                        [VSASignal.EFFORT_DOWN,
                         VSASignal.CLIMACTIC_ACTION] and
                        self.lines.strength[0] > 0.8)
                    else 'sell'
                    if (current_bar.signal in
                        [VSASignal.EFFORT_DOWN,
                         VSASignal.CLIMACTIC_ACTION] and
                        self.lines.strength[0] > 0.5)
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if self.lines.strength[0] > 0.8
                    else 'moderate'
                    if self.lines.strength[0] > 0.5
                    else 'low'
                ),
                'timing': (
                    'optimal'
                    if (current_bar.signal != VSASignal.NEUTRAL and
                        self.lines.strength[0] > 0.8)
                    else 'suboptimal'
                    if (current_bar.signal != VSASignal.NEUTRAL and
                        self.lines.strength[0] > 0.5)
                    else 'poor'
                )
            },
            'risk_assessment': {
                'signal_reliability': (
                    'high'
                    if (self.lines.strength[0] > 0.8 and
                        current_bar.signal != VSASignal.NEUTRAL)
                    else 'moderate'
                    if (self.lines.strength[0] > 0.5 and
                        current_bar.signal != VSASignal.NEUTRAL)
                    else 'low'
                ),
                'market_context': (
                    'supportive'
                    if (sum(1 for s in self.signal_history[-5:]
                           if s != VSASignal.NEUTRAL) >= 4)
                    else 'mixed'
                    if (sum(1 for s in self.signal_history[-5:]
                           if s != VSASignal.NEUTRAL) >= 2)
                    else 'unclear'
                ),
                'volatility_risk': (
                    'high'
                    if (self.lines.spread_ratio[0] > 1.5 and
                        self.lines.volume_ratio[0] > 1.5)
                    else 'moderate'
                    if (self.lines.spread_ratio[0] > 1.2 or
                        self.lines.volume_ratio[0] > 1.2)
                    else 'low'
                )
            }
        }
