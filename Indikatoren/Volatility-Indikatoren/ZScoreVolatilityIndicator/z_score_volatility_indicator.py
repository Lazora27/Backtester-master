import backtrader as bt
import numpy as np
from scipy import stats

class ZScoreVolatilityIndicator(bt.Indicator):
    """
    Z-Score Volatility Indicator
    
    Ein Volatilitätsindikator, der Z-Scores verwendet, um
    statistische Ausreißer in der Volatilität zu identifizieren.
    
    Features:
    - Z-Score Berechnung
    - Trendanalyse
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - z_threshold (2.0): Z-Score Schwellenwert
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('z_score', 'smoothed_z',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('z_threshold', 2.0),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        z_score=dict(color='blue', _name='Z-Score'),
        smoothed_z=dict(color='red', _name='Smoothed Z'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ZScoreVolatilityIndicator, self).__init__()
        
        # Historie
        self.returns_history = []
        self.z_score_history = []
        
    def calculate_returns(self):
        """
        Berechnet die logarithmischen Returns.
        """
        if len(self.data) < 2:
            return 0
            
        return np.log(
            self.data.close[0] /
            self.data.close[-1]
        )
        
    def calculate_z_score(self):
        """
        Berechnet den Z-Score.
        """
        if len(self.returns_history) < self.p.period:
            return 0
            
        returns = np.array(
            self.returns_history[-self.p.period:]
        )
        
        return stats.zscore(returns)[-1]
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.z_score_history) < 2:
            return 0
            
        return (
            self.z_score_history[-1] -
            self.z_score_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.returns_history) < self.p.period:
            return 1.0
            
        current_vol = np.std(
            self.returns_history[-5:]
        )
        historical_vol = np.std(
            self.returns_history[-self.p.period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Returns berechnen
        returns = self.calculate_returns()
        self.returns_history.append(returns)
        
        # Z-Score berechnen
        z_score = self.calculate_z_score()
        self.z_score_history.append(z_score)
        self.lines.z_score[0] = z_score
        
        # Geglätteter Z-Score
        if len(self.z_score_history) >= self.p.smooth_period:
            self.lines.smoothed_z[0] = np.mean(
                self.z_score_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_z[0] = z_score
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if abs(z_score) > self.p.z_threshold:
            if (z_score < -self.p.z_threshold and
                self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (z_score > self.p.z_threshold and
                  self.lines.trend_strength[0] < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.returns_history,
                    self.z_score_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'z_score': {
                'value': self.lines.z_score[0],
                'smoothed': self.lines.smoothed_z[0],
                'threshold_exceeded': (
                    abs(self.lines.z_score[0]) >
                    self.p.z_threshold
                ),
                'direction': (
                    'positive' if self.lines.z_score[0] > 0
                    else 'negative'
                )
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
                    'increasing'
                    if self.lines.volatility_ratio[0] > 1
                    else 'decreasing'
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
                    abs(self.lines.trend_strength[0]) *
                    (1 - abs(self.lines.z_score[0]) /
                     (2 * self.p.z_threshold))
                    if abs(self.lines.z_score[0]) <=
                       2 * self.p.z_threshold
                    else 0
                )
            },
            'risk': {
                'z_score_risk': (
                    abs(self.lines.z_score[0]) /
                    self.p.z_threshold
                    if abs(self.lines.z_score[0]) <=
                       self.p.z_threshold
                    else 1
                ),
                'trend_risk': (
                    1 - abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
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
