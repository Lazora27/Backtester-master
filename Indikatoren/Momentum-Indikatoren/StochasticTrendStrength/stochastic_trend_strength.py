import backtrader as bt
import numpy as np

class StochasticTrendStrength(bt.Indicator):
    """
    Stochastic Trend Strength Indicator
    
    Ein fortgeschrittener Trendstärke-Indikator, der stochastische
    Berechnungen mit Trendanalyse kombiniert.
    
    Features:
    - Stochastische Trendstärke
    - Adaptive Glättung
    - Momentum-Bestätigung
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - smooth_period (3): Glättungsperiode
    - trend_period (10): Trendperiode
    - upper_threshold (80): Obere Schwelle
    - lower_threshold (20): Untere Schwelle
    """
    
    lines = ('strength', 'smoothed_strength',
             'trend', 'momentum', 'divergence',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('smooth_period', 3),
        ('trend_period', 10),
        ('upper_threshold', 80),
        ('lower_threshold', 20)
    )
    
    plotlines = dict(
        strength=dict(color='blue', _name='Strength'),
        smoothed_strength=dict(color='red', _name='Smoothed'),
        trend=dict(color='green', _name='Trend'),
        momentum=dict(color='purple', _name='Momentum'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(StochasticTrendStrength, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.strength_history = []
        self.trend_history = []
        self.price_history = []
        
    def calculate_strength(self):
        """
        Berechnet die stochastische Trendstärke.
        """
        if len(self.price_history) < self.p.period:
            return 50
            
        # Hochs und Tiefs
        high = max(self.data.high.get(ago=0, size=self.p.period))
        low = min(self.data.low.get(ago=0, size=self.p.period))
        
        if high == low:
            return 50
            
        # Stochastische Berechnung
        k = 100 * (self.data.close[0] - low) / (high - low)
        
        # Trendstärke
        trend = sum(
            1 if self.data[i] > self.data[i-1] else -1
            for i in range(self.p.trend_period)
            if i > 0
        )
        
        # Kombinierte Stärke
        strength = k * (1 + abs(trend) / self.p.trend_period)
        return min(100, max(0, strength))
        
    def calculate_trend(self):
        """
        Berechnet den Trendwert.
        """
        if len(self.strength_history) < 2:
            return 0
            
        return self.strength_history[-1] - self.strength_history[-2]
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Stärke.
        """
        if len(self.price_history) < self.p.period or len(self.strength_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # Stärke-Hochs/-Tiefs
        strength_high = max(self.strength_history[-self.p.period:])
        strength_low = min(self.strength_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and strength_low > strength_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and strength_low < strength_high:
            return -1
            
        return 0
        
    def next(self):
        # Stärke berechnen
        self.lines.strength[0] = self.calculate_strength()
        
        # Historie aktualisieren
        self.strength_history.append(self.lines.strength[0])
        self.price_history.append(self.data[0])
        
        # Geglättete Stärke
        self.lines.smoothed_strength[0] = bt.indicators.SMA(
            self.lines.strength, period=self.p.smooth_period
        )[0]
        
        # Trend
        self.lines.trend[0] = self.calculate_trend()
        self.trend_history.append(self.lines.trend[0])
        
        # Momentum
        self.lines.momentum[0] = (
            self.lines.smoothed_strength[0] -
            self.lines.smoothed_strength[-1]
        )
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        self.lines.mid[0] = 50
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.trend_period)
        for hist in [self.strength_history, self.trend_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_strength[0] < self.p.lower_threshold and
            self.lines.momentum[0] > 0 and
            self.lines.trend[0] > 0 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_strength[0] > self.p.upper_threshold and
            self.lines.momentum[0] < 0 and
            self.lines.trend[0] < 0 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'strength': {
                'raw': self.lines.strength[0],
                'smoothed': self.lines.smoothed_strength[0],
                'trend': self.lines.trend[0],
                'momentum': self.lines.momentum[0]
            },
            'trend': {
                'direction': np.sign(self.lines.trend[0]),
                'strength': abs(self.lines.trend[0]),
                'consistency': (
                    np.mean([
                        1 if np.sign(t) == np.sign(self.lines.trend[0])
                        else 0
                        for t in self.trend_history[-5:]
                    ]) if len(self.trend_history) >= 5
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
                'strength': abs(self.lines.trend[0]),
                'reliability': (
                    abs(self.lines.trend[0]) *
                    (1 + abs(self.lines.divergence[0])) *
                    abs(self.lines.momentum[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'strength_stability': (
                    np.std(self.strength_history)
                    if len(self.strength_history) > 1
                    else 0
                ),
                'trend_stability': (
                    np.std(self.trend_history)
                    if len(self.trend_history) > 1
                    else 0
                )
            }
        }
