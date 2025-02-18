import backtrader as bt
import numpy as np

class MACDHistogram(bt.Indicator):
    """
    MACD Histogram
    
    Eine erweiterte Version des MACD-Histogramms mit zusätzlichen
    Analysetools und Signalgenerierung.
    
    Features:
    - Erweitertes MACD-Histogramm
    - Divergenz-Erkennung
    - Momentum-Analyse
    - Histogramm-Muster
    - Signal-Validierung
    
    Parameter:
    - fast_period (12): Schnelle EMA Periode
    - slow_period (26): Langsame EMA Periode
    - signal_period (9): Signal EMA Periode
    - histogram_threshold (0.0): Histogramm-Schwelle
    """
    
    lines = ('macd', 'signal', 'histogram',
             'divergence', 'pattern', 'strength',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('histogram_threshold', 0.0)
    )
    
    plotlines = dict(
        macd=dict(color='blue', _name='MACD'),
        signal=dict(color='red', _name='Signal'),
        histogram=dict(color='green', _name='Histogram'),
        divergence=dict(color='purple', _name='Divergence'),
        pattern=dict(color='orange', _name='Pattern'),
        strength=dict(color='gray', _name='Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MACDHistogram, self).__init__()
        
        # EMAs berechnen
        self.fast_ma = bt.indicators.EMA(period=self.p.fast_period)
        self.slow_ma = bt.indicators.EMA(period=self.p.slow_period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.histogram_history = []
        self.price_history = []
        self.pattern_history = []
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Histogramm.
        """
        if len(self.price_history) < self.p.signal_period or len(self.histogram_history) < self.p.signal_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.signal_period:])
        price_low = min(self.price_history[-self.p.signal_period:])
        
        # Histogramm-Hochs/-Tiefs
        hist_high = max(self.histogram_history[-self.p.signal_period:])
        hist_low = min(self.histogram_history[-self.p.signal_period:])
        
        # Bullische Divergenz
        if price_low < price_high and hist_low > hist_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and hist_low < hist_high:
            return -1
            
        return 0
        
    def detect_pattern(self):
        """
        Erkennt Histogramm-Muster.
        """
        if len(self.histogram_history) < 3:
            return 0
            
        # Doppel-Boden
        if (self.histogram_history[-3] < 0 and
            self.histogram_history[-2] < self.histogram_history[-3] and
            self.histogram_history[-1] > self.histogram_history[-2]):
            return 1
            
        # Doppel-Top
        if (self.histogram_history[-3] > 0 and
            self.histogram_history[-2] > self.histogram_history[-3] and
            self.histogram_history[-1] < self.histogram_history[-2]):
            return -1
            
        return 0
        
    def calculate_strength(self):
        """
        Berechnet die Stärke des Histogramm-Signals.
        """
        if len(self.histogram_history) < 2:
            return 0
            
        # Momentum
        momentum = self.histogram_history[-1] - self.histogram_history[-2]
        
        # Relative Stärke
        if self.data[0] != 0:
            strength = abs(momentum) / self.data[0]
        else:
            strength = 0
            
        return min(1.0, strength)
        
    def next(self):
        # MACD berechnen
        self.lines.macd[0] = self.fast_ma[0] - self.slow_ma[0]
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.macd, period=self.p.signal_period
        )[0]
        
        # Histogramm
        self.lines.histogram[0] = self.lines.macd[0] - self.lines.signal[0]
        
        # Historie aktualisieren
        self.histogram_history.append(self.lines.histogram[0])
        self.price_history.append(self.data[0])
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Muster
        pattern = self.detect_pattern()
        self.lines.pattern[0] = pattern
        self.pattern_history.append(pattern)
        
        # Stärke
        self.lines.strength[0] = self.calculate_strength()
        
        # Historie begrenzen
        max_period = max(self.p.slow_period, self.p.signal_period)
        for hist in [self.histogram_history, self.price_history, self.pattern_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.histogram[0] > self.p.histogram_threshold and
            self.lines.histogram[0] > self.histogram_history[-2] and
            self.lines.divergence[0] >= 0 and
            self.lines.pattern[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.histogram[0] < -self.p.histogram_threshold and
            self.lines.histogram[0] < self.histogram_history[-2] and
            self.lines.divergence[0] <= 0 and
            self.lines.pattern[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'macd': {
                'value': self.lines.macd[0],
                'signal': self.lines.signal[0],
                'histogram': self.lines.histogram[0],
                'trend': (
                    'bullish' if self.lines.histogram[0] > 0
                    else 'bearish'
                )
            },
            'patterns': {
                'current': self.lines.pattern[0],
                'type': (
                    'double_bottom' if self.lines.pattern[0] > 0
                    else 'double_top' if self.lines.pattern[0] < 0
                    else 'none'
                ),
                'strength': self.lines.strength[0],
                'reliability': (
                    abs(self.lines.pattern[0]) *
                    self.lines.strength[0]
                )
            },
            'divergence': {
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'momentum': {
                'direction': np.sign(
                    self.lines.histogram[0] -
                    self.histogram_history[-2]
                    if len(self.histogram_history) > 1
                    else 0
                ),
                'acceleration': (
                    self.lines.histogram[0] -
                    2 * self.histogram_history[-2] +
                    self.histogram_history[-3]
                    if len(self.histogram_history) > 2
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.strength[0],
                'reliability': (
                    self.lines.strength[0] *
                    (1 + abs(self.lines.divergence[0])) *
                    (1 + abs(self.lines.pattern[0]))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'histogram_stability': (
                    np.std(self.histogram_history)
                    if len(self.histogram_history) > 1
                    else 0
                ),
                'pattern_consistency': (
                    np.std(self.pattern_history)
                    if len(self.pattern_history) > 1
                    else 0
                )
            }
        }
