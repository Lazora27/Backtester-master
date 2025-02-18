import backtrader as bt
import numpy as np

class TTMSqueezeIndicator(bt.Indicator):
    """
    TTM Squeeze Indicator
    
    Ein Volatilitätsindikator, der Bollinger Bands und Keltner
    Channels kombiniert, um Volatilitätskompressionen zu identifizieren.
    
    Features:
    - Volatilitätskompression
    - Momentum-Berechnung
    - Trendstärkeanalyse
    - Signalgenerierung
    
    Parameter:
    - bb_period (20): Bollinger Bands Periode
    - bb_std (2.0): Bollinger Bands Standardabweichungen
    - kc_period (20): Keltner Channel Periode
    - kc_atr_period (20): Keltner Channel ATR Periode
    - kc_factor (1.5): Keltner Channel Faktor
    """
    
    lines = ('squeeze_on', 'momentum',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('bb_period', 20),
        ('bb_std', 2.0),
        ('kc_period', 20),
        ('kc_atr_period', 20),
        ('kc_factor', 1.5)
    )
    
    plotlines = dict(
        squeeze_on=dict(color='blue', _name='Squeeze'),
        momentum=dict(color='red', _name='Momentum'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TTMSqueezeIndicator, self).__init__()
        
        # Bollinger Bands
        self.bb_mid = bt.indicators.SMA(period=self.p.bb_period)
        self.bb_std = bt.indicators.StdDev(period=self.p.bb_period)
        self.bb_upper = self.bb_mid + self.p.bb_std * self.bb_std
        self.bb_lower = self.bb_mid - self.p.bb_std * self.bb_std
        
        # Keltner Channel
        self.kc_mid = bt.indicators.EMA(period=self.p.kc_period)
        self.kc_atr = bt.indicators.ATR(period=self.p.kc_atr_period)
        self.kc_upper = (
            self.kc_mid +
            self.p.kc_factor * self.kc_atr
        )
        self.kc_lower = (
            self.kc_mid -
            self.p.kc_factor * self.kc_atr
        )
        
        # Historie
        self.momentum_history = []
        self.squeeze_history = []
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Indikator.
        """
        if len(self.data) < self.p.bb_period:
            return 0
            
        # Lineare Regression für Momentum
        x = np.arange(self.p.bb_period)
        y = np.array([
            self.data.close[-i] - (
                (self.bb_upper[-i] + self.bb_lower[-i]) / 2
            )
            for i in range(self.p.bb_period)
        ])
        
        A = np.vstack([x, np.ones(len(x))]).T
        slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
        
        return slope
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.momentum_history) < 2:
            return 0
            
        return (
            self.momentum_history[-1] -
            self.momentum_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        bb_width = self.bb_upper[0] - self.bb_lower[0]
        kc_width = self.kc_upper[0] - self.kc_lower[0]
        
        return (
            bb_width / kc_width
            if kc_width != 0 else 1.0
        )
        
    def next(self):
        # Squeeze berechnen
        self.lines.squeeze_on[0] = (
            1 if (
                self.bb_upper[0] <= self.kc_upper[0] and
                self.bb_lower[0] >= self.kc_lower[0]
            )
            else 0
        )
        self.squeeze_history.append(self.lines.squeeze_on[0])
        
        # Momentum berechnen
        self.lines.momentum[0] = self.calculate_momentum()
        self.momentum_history.append(self.lines.momentum[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.squeeze_on[0] == 0 and
            len(self.squeeze_history) > 1 and
            self.squeeze_history[-2] == 1):
            if self.lines.momentum[0] > 0:
                self.lines.signal[0] = 1  # Kaufsignal
            else:
                self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.bb_period,
            self.p.kc_period,
            self.p.kc_atr_period
        )
        for hist in [self.momentum_history, self.squeeze_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'squeeze': {
                'active': bool(self.lines.squeeze_on[0]),
                'duration': (
                    sum(1 for x in reversed(self.squeeze_history)
                        if x == 1)
                ),
                'intensity': (
                    1 - self.lines.volatility_ratio[0]
                    if self.lines.squeeze_on[0]
                    else 0
                )
            },
            'momentum': {
                'value': self.lines.momentum[0],
                'direction': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.momentum[0])
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 1
                )
            },
            'volatility': {
                'ratio': self.lines.volatility_ratio[0],
                'state': (
                    'compressed'
                    if self.lines.squeeze_on[0]
                    else 'expanding'
                ),
                'relative_level': (
                    'high'
                    if self.lines.volatility_ratio[0] > 1.5
                    else 'low'
                    if self.lines.volatility_ratio[0] < 0.5
                    else 'normal'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    abs(self.lines.momentum[0]) *
                    (1 - self.lines.volatility_ratio[0])
                    if self.lines.squeeze_on[0] == 0
                    else 0
                )
            },
            'risk': {
                'squeeze_risk': (
                    1 if self.lines.squeeze_on[0]
                    else self.lines.volatility_ratio[0]
                ),
                'momentum_risk': (
                    1 - abs(self.lines.momentum[0])
                    if abs(self.lines.momentum[0]) <= 1
                    else 0
                ),
                'volatility_risk': (
                    self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 1
                    else 1 / self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 0
                    else 1
                )
            }
        }
