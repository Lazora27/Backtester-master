import backtrader as bt
import numpy as np

class SmoothedRSI(bt.Indicator):
    """
    Smoothed RSI
    
    Eine geglättete Version des RSI mit mehreren
    Glättungsstufen und erweiterten Analysefunktionen.
    
    Features:
    - Mehrfache Glättung
    - Adaptive Parameter
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (14): RSI Periode
    - smooth_period1 (5): Erste Glättungsperiode
    - smooth_period2 (3): Zweite Glättungsperiode
    - upper_band (70): Obere Schwelle
    - lower_band (30): Untere Schwelle
    """
    
    lines = ('rsi', 'smoothed1', 'smoothed2',
             'trend_strength', 'divergence',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('smooth_period1', 5),
        ('smooth_period2', 3),
        ('upper_band', 70),
        ('lower_band', 30)
    )
    
    plotlines = dict(
        rsi=dict(color='blue', _name='RSI'),
        smoothed1=dict(color='red', _name='Smoothed1'),
        smoothed2=dict(color='green', _name='Smoothed2'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(SmoothedRSI, self).__init__()
        
        # Basis RSI
        self.rsi = bt.indicators.RSI(period=self.p.period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.rsi_history = []
        self.smoothed1_history = []
        self.smoothed2_history = []
        self.price_history = []
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.smoothed2_history) < 2:
            return 0
            
        # Smoothed RSI Momentum
        momentum = self.smoothed2_history[-1] - self.smoothed2_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Smoothed RSI.
        """
        if len(self.price_history) < self.p.period or len(self.smoothed2_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # RSI-Hochs/-Tiefs
        rsi_high = max(self.smoothed2_history[-self.p.period:])
        rsi_low = min(self.smoothed2_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and rsi_low > rsi_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and rsi_low < rsi_high:
            return -1
            
        return 0
        
    def next(self):
        # Basis RSI
        self.lines.rsi[0] = self.rsi[0]
        
        # Erste Glättung
        self.lines.smoothed1[0] = bt.indicators.EMA(
            self.lines.rsi, period=self.p.smooth_period1
        )[0]
        
        # Zweite Glättung
        self.lines.smoothed2[0] = bt.indicators.EMA(
            self.lines.smoothed1, period=self.p.smooth_period2
        )[0]
        
        # Historie aktualisieren
        self.rsi_history.append(self.lines.rsi[0])
        self.smoothed1_history.append(self.lines.smoothed1[0])
        self.smoothed2_history.append(self.lines.smoothed2[0])
        self.price_history.append(self.data[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_band
        self.lines.lower[0] = self.p.lower_band
        self.lines.mid[0] = 50
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.smooth_period1, self.p.smooth_period2)
        for hist in [self.rsi_history, self.smoothed1_history, self.smoothed2_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed2[0] < self.p.lower_band and
            self.lines.smoothed2[0] > self.lines.smoothed2[-1] and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed2[0] > self.p.upper_band and
            self.lines.smoothed2[0] < self.lines.smoothed2[-1] and
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
            'rsi': {
                'raw': self.lines.rsi[0],
                'smoothed1': self.lines.smoothed1[0],
                'smoothed2': self.lines.smoothed2[0],
                'trend_strength': self.lines.trend_strength[0]
            },
            'trend': {
                'direction': np.sign(
                    self.lines.smoothed2[0] - self.lines.smoothed2[-1]
                ),
                'strength': self.lines.trend_strength[0],
                'momentum': (
                    self.lines.smoothed2[0] - self.lines.smoothed2[-1]
                    if len(self.smoothed2_history) > 1
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
                    abs(self.lines.smoothed2[0] - 50) / 50
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'rsi_stability': (
                    np.std(self.rsi_history)
                    if len(self.rsi_history) > 1
                    else 0
                ),
                'smoothed_stability': (
                    np.std(self.smoothed2_history)
                    if len(self.smoothed2_history) > 1
                    else 0
                )
            }
        }
