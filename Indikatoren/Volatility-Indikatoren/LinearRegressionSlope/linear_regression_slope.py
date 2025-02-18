import backtrader as bt
import numpy as np
from scipy import stats

class LinearRegressionSlope(bt.Indicator):
    """
    Linear Regression Slope (LRS)
    
    Ein Volatilitätsindikator, der die Steigung der linearen Regression
    als Maß für die Trendstärke und Volatilität verwendet.
    
    Features:
    - Lineare Regressionsanalyse
    - Trendstärkeberechnung
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - smooth_period (10): Glättungsperiode
    - std_dev_period (10): Standardabweichungsperiode
    """
    
    lines = ('slope', 'smoothed_slope',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('smooth_period', 10),
        ('std_dev_period', 10)
    )
    
    plotlines = dict(
        slope=dict(color='blue', _name='Slope'),
        smoothed_slope=dict(color='red', _name='Smoothed Slope'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(LinearRegressionSlope, self).__init__()
        
        # Historie
        self.slope_history = []
        self.r_squared_history = []
        
    def calculate_regression(self):
        """
        Berechnet die Regressionssteigung.
        """
        if len(self.data) < self.p.period:
            return 0, 0
            
        x = np.arange(self.p.period)
        y = np.array([self.data.close[-i] for i in range(self.p.period)])
        
        slope, _, r_value, _, _ = stats.linregress(x, y)
        r_squared = r_value ** 2
        
        return slope, r_squared
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.slope_history) < 2:
            return 0
            
        return (
            self.slope_history[-1] -
            self.slope_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.data) < self.p.std_dev_period:
            return 1.0
            
        current_vol = np.std([
            self.data.close[-i] for i in range(5)
        ])
        historical_vol = np.std([
            self.data.close[-i]
            for i in range(self.p.std_dev_period)
        ])
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Regression berechnen
        slope, r_squared = self.calculate_regression()
        
        # Historie aktualisieren
        self.slope_history.append(slope)
        self.r_squared_history.append(r_squared)
        
        # Steigung
        self.lines.slope[0] = slope
        
        # Geglättete Steigung
        if len(self.slope_history) >= self.p.smooth_period:
            self.lines.smoothed_slope[0] = np.mean(
                self.slope_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_slope[0] = slope
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if len(self.slope_history) >= 2:
            current_r_squared = self.r_squared_history[-1]
            
            if (slope > 0 and
                self.lines.trend_strength[0] > 0 and
                current_r_squared > 0.7):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (slope < 0 and
                  self.lines.trend_strength[0] < 0 and
                  current_r_squared > 0.7):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period,
            self.p.std_dev_period
        )
        for hist in [self.slope_history, self.r_squared_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_r_squared = (
            self.r_squared_history[-1]
            if self.r_squared_history else 0
        )
        
        return {
            'regression': {
                'slope': self.lines.slope[0],
                'smoothed': self.lines.smoothed_slope[0],
                'r_squared': current_r_squared,
                'quality': (
                    'excellent' if current_r_squared > 0.9
                    else 'good' if current_r_squared > 0.7
                    else 'poor' if current_r_squared < 0.3
                    else 'fair'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.slope[0] > 0
                    else 'down'
                ),
                'acceleration': (
                    'increasing'
                    if self.lines.trend_strength[0] > 0
                    else 'decreasing'
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
                    current_r_squared *
                    abs(self.lines.trend_strength[0])
                )
            },
            'risk': {
                'model_risk': (
                    1 - current_r_squared
                    if current_r_squared <= 1
                    else 0
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
