import backtrader as bt
import numpy as np

class MomentumTrendStrength(bt.Indicator):
    """
    Momentum Trend Strength Indicator
    
    Ein fortgeschrittener Indikator zur Messung der Trendstärke
    basierend auf Momentum und verschiedenen Oszillatoren.
    
    Features:
    - Multi-Momentum Analyse
    - Trendstärke Berechnung
    - Divergenz-Erkennung
    - Adaptive Gewichtung
    - Signal-Generierung
    
    Parameter:
    - fast_period (10): Schnelle Momentum-Periode
    - slow_period (21): Langsame Momentum-Periode
    - signal_period (9): Signal-Periode
    - threshold (0.5): Signalschwelle
    """
    
    lines = ('trend_strength', 'momentum_fast', 'momentum_slow',
             'signal_line', 'divergence', 'overbought',
             'oversold', 'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 10),
        ('slow_period', 21),
        ('signal_period', 9),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        trend_strength=dict(color='blue', _name='Trend Strength'),
        momentum_fast=dict(color='green', _name='Fast Momentum'),
        momentum_slow=dict(color='red', _name='Slow Momentum'),
        signal_line=dict(color='orange', _name='Signal'),
        divergence=dict(color='purple', _name='Divergence'),
        overbought=dict(_name='Overbought', color='gray'),
        oversold=dict(_name='Oversold', color='gray'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MomentumTrendStrength, self).__init__()
        
        # Technische Indikatoren
        self.rsi = bt.indicators.RSI(period=14)
        self.macd = bt.indicators.MACD()
        self.stoch = bt.indicators.Stochastic()
        self.atr = bt.indicators.ATR(period=14)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.signal_period)
        
        # Historie
        self.momentum_history = []
        self.divergence_history = []
        self.strength_history = []
        
    def calculate_momentum(self, period):
        """
        Berechnet den Momentum-Wert für eine bestimmte Periode.
        """
        if len(self) < period:
            return 0
            
        # ROC (Rate of Change)
        roc = (self.data[0] - self.data[-period]) / self.data[-period]
        
        # Momentum normalisieren (-1 bis 1)
        normalized = np.tanh(roc)
        
        return normalized
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Momentum.
        """
        if len(self) < self.p.slow_period:
            return 0
            
        # Preis-Momentum Divergenz
        price_change = self.data[0] - self.data[-self.p.slow_period]
        momentum_change = (
            self.lines.momentum_slow[0] -
            self.lines.momentum_slow[-self.p.slow_period]
        )
        
        # Divergenz (-1 bis 1)
        if price_change * momentum_change < 0:
            divergence = -np.sign(price_change)
        else:
            divergence = 0
            
        return divergence
        
    def calculate_trend_strength(self):
        """
        Berechnet die Gesamttrendstärke.
        """
        if len(self) < 2:
            return 0
            
        # Momentum-Komponente
        momentum_strength = abs(
            self.lines.momentum_fast[0] +
            self.lines.momentum_slow[0]
        ) / 2
        
        # Oszillator-Komponente
        rsi_strength = abs(self.rsi[0] - 50) / 50
        stoch_strength = abs(self.stoch.percK[0] - 50) / 50
        macd_strength = abs(self.macd.macd[0]) / self.atr[0] if self.atr[0] != 0 else 0
        
        # Gewichtete Kombination
        strength = (
            momentum_strength * 0.4 +
            rsi_strength * 0.2 +
            stoch_strength * 0.2 +
            macd_strength * 0.2
        )
        
        return min(strength, 1.0)
        
    def next(self):
        # Momentum berechnen
        self.lines.momentum_fast[0] = self.calculate_momentum(
            self.p.fast_period
        )
        self.lines.momentum_slow[0] = self.calculate_momentum(
            self.p.slow_period
        )
        
        # Signal-Linie
        self.lines.signal_line[0] = self.ema(self.lines.momentum_slow)
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Overbought/Oversold
        self.lines.overbought[0] = self.p.threshold
        self.lines.oversold[0] = -self.p.threshold
        
        # Historie aktualisieren
        self.momentum_history.append(self.lines.momentum_slow[0])
        self.divergence_history.append(self.lines.divergence[0])
        self.strength_history.append(self.lines.trend_strength[0])
        
        if len(self.momentum_history) > self.p.slow_period:
            self.momentum_history.pop(0)
            self.divergence_history.pop(0)
            self.strength_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.momentum_slow[0] > self.lines.signal_line[0] and
            self.lines.trend_strength[0] > self.p.threshold and
            self.lines.momentum_slow[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.momentum_slow[0] < self.lines.signal_line[0] and
            self.lines.trend_strength[0] > self.p.threshold and
            self.lines.momentum_slow[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'momentum': {
                'fast': self.lines.momentum_fast[0],
                'slow': self.lines.momentum_slow[0],
                'signal': self.lines.signal_line[0],
                'divergence': self.lines.divergence[0]
            },
            'strength': {
                'current': self.lines.trend_strength[0],
                'average': np.mean(self.strength_history) if self.strength_history else 0,
                'momentum_quality': abs(
                    self.lines.momentum_fast[0] -
                    self.lines.momentum_slow[0]
                )
            },
            'oscillators': {
                'rsi': self.rsi[0],
                'stoch_k': self.stoch.percK[0],
                'macd': self.macd.macd[0]
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'momentum_aligned': (
                    self.lines.momentum_fast[0] *
                    self.lines.momentum_slow[0] > 0
                )
            },
            'risk': {
                'atr': self.atr[0],
                'volatility': self.atr[0] / self.data[0] if self.data[0] != 0 else 0,
                'momentum_stability': np.std(self.momentum_history) if self.momentum_history else 0
            }
        }
