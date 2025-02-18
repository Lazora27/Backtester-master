import backtrader as bt
import numpy as np

class SuperMACD(bt.Indicator):
    """
    Super MACD
    
    Eine erweiterte Version des MACD mit zusätzlichen
    Analysefunktionen und Signalgenerierung.
    
    Features:
    - Mehrfache MACD-Berechnung
    - Adaptive Signallinie
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - fast_period (12): Schnelle EMA Periode
    - slow_period (26): Langsame EMA Periode
    - signal_period (9): Signal EMA Periode
    - super_period (5): Super Signal Periode
    """
    
    lines = ('macd', 'signal', 'super_signal',
             'histogram', 'trend_strength',
             'divergence', 'upper', 'lower',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('super_period', 5),
        ('upper_threshold', 0.5),
        ('lower_threshold', -0.5)
    )
    
    plotlines = dict(
        macd=dict(color='blue', _name='MACD'),
        signal=dict(color='red', _name='Signal'),
        super_signal=dict(color='green', _name='Super Signal'),
        histogram=dict(color='gray', _name='Histogram'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(SuperMACD, self).__init__()
        
        # MACD Komponenten
        self.fast_ma = bt.indicators.EMA(period=self.p.fast_period)
        self.slow_ma = bt.indicators.EMA(period=self.p.slow_period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.macd_history = []
        self.histogram_history = []
        self.price_history = []
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.histogram_history) < 2:
            return 0
            
        # Histogramm-Momentum
        momentum = self.histogram_history[-1] - self.histogram_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und MACD.
        """
        if len(self.price_history) < self.p.slow_period or len(self.macd_history) < self.p.slow_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.slow_period:])
        price_low = min(self.price_history[-self.p.slow_period:])
        
        # MACD-Hochs/-Tiefs
        macd_high = max(self.macd_history[-self.p.slow_period:])
        macd_low = min(self.macd_history[-self.p.slow_period:])
        
        # Bullische Divergenz
        if price_low < price_high and macd_low > macd_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and macd_low < macd_high:
            return -1
            
        return 0
        
    def next(self):
        # MACD berechnen
        self.lines.macd[0] = self.fast_ma[0] - self.slow_ma[0]
        
        # Historie aktualisieren
        self.macd_history.append(self.lines.macd[0])
        self.price_history.append(self.data[0])
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.macd, period=self.p.signal_period
        )[0]
        
        # Super Signal-Linie
        self.lines.super_signal[0] = bt.indicators.EMA(
            self.lines.signal, period=self.p.super_period
        )[0]
        
        # Histogramm
        self.lines.histogram[0] = (
            self.lines.macd[0] - self.lines.super_signal[0]
        )
        self.histogram_history.append(self.lines.histogram[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        
        # Historie begrenzen
        max_period = max(self.p.slow_period, self.p.signal_period)
        for hist in [self.macd_history, self.histogram_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.macd[0] < self.p.lower_threshold and
            self.lines.histogram[0] > 0 and
            self.lines.macd[0] > self.lines.macd[-1] and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.macd[0] > self.p.upper_threshold and
            self.lines.histogram[0] < 0 and
            self.lines.macd[0] < self.lines.macd[-1] and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] <= 0):
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
                'super_signal': self.lines.super_signal[0],
                'histogram': self.lines.histogram[0]
            },
            'trend': {
                'direction': np.sign(self.lines.histogram[0]),
                'strength': self.lines.trend_strength[0],
                'momentum': (
                    self.lines.histogram[0] -
                    self.histogram_history[-2]
                    if len(self.histogram_history) > 1
                    else 0
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
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    (1 + abs(self.lines.divergence[0])) *
                    abs(self.lines.histogram[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'macd_stability': (
                    np.std(self.macd_history)
                    if len(self.macd_history) > 1
                    else 0
                ),
                'histogram_stability': (
                    np.std(self.histogram_history)
                    if len(self.histogram_history) > 1
                    else 0
                )
            }
        }
