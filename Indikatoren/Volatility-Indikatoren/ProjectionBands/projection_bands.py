import backtrader as bt
import numpy as np
from scipy import stats

class ProjectionBands(bt.Indicator):
    """
    Projection Bands Indicator
    
    Ein Volatilitätsindikator, der statistische Projektionsbänder
    basierend auf historischer Volatilität berechnet.
    
    Features:
    - Statistische Bandberechnung
    - Trendprojektion
    - Volatilitätsgewichtung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - std_dev (2.0): Standardabweichungsfaktor
    - projection_period (5): Projektionszeitraum
    """
    
    lines = ('upper', 'lower', 'mid',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('std_dev', 2.0),
        ('projection_period', 5)
    )
    
    plotlines = dict(
        upper=dict(color='blue', _name='Upper Band'),
        lower=dict(color='red', _name='Lower Band'),
        mid=dict(color='green', _name='Mid Line'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        volatility_ratio=dict(color='orange', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ProjectionBands, self).__init__()
        
        # Historie
        self.price_history = []
        self.slope_history = []
        self.vol_history = []
        
    def calculate_projection(self):
        """
        Berechnet die Projektionsbänder.
        """
        if len(self.price_history) < self.p.period:
            return 0, 0, 0
            
        # Zeitreihe
        x = np.arange(len(self.price_history[-self.p.period:]))
        y = np.array(self.price_history[-self.p.period:])
        
        # Lineare Regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        
        # Projektion
        proj_x = self.p.period + self.p.projection_period
        mid_proj = slope * proj_x + intercept
        
        # Standardfehler
        std_dev = np.std(y)
        
        # Bänder
        upper_proj = mid_proj + self.p.std_dev * std_dev
        lower_proj = mid_proj - self.p.std_dev * std_dev
        
        return upper_proj, lower_proj, mid_proj
        
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
        if len(self.vol_history) < self.p.period:
            return 1.0
            
        current_vol = np.std(self.price_history[-5:])
        historical_vol = np.std(self.price_history[-self.p.period:])
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        
        # Projektionsbänder berechnen
        upper, lower, mid = self.calculate_projection()
        
        self.lines.upper[0] = upper
        self.lines.lower[0] = lower
        self.lines.mid[0] = mid
        
        # Steigung für Trendstärke
        if len(self.price_history) >= self.p.period:
            x = np.arange(self.p.period)
            y = np.array(self.price_history[-self.p.period:])
            slope, _, _, _, _ = stats.linregress(x, y)
            self.slope_history.append(slope)
        else:
            self.slope_history.append(0)
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if len(self.price_history) >= self.p.period:
            if (self.data.close[0] <= self.lines.lower[0] and
                self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.data.close[0] >= self.lines.upper[0] and
                  self.lines.trend_strength[0] < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Volatilitätshistorie
        if len(self.price_history) >= 5:
            self.vol_history.append(
                np.std(self.price_history[-5:])
            )
            
        # Historie begrenzen
        max_period = self.p.period + self.p.projection_period
        for hist in [self.price_history, self.slope_history,
                    self.vol_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'bands': {
                'upper': self.lines.upper[0],
                'lower': self.lines.lower[0],
                'mid': self.lines.mid[0],
                'width': (
                    self.lines.upper[0] - self.lines.lower[0]
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'reliability': abs(
                    self.lines.trend_strength[0]
                )
            },
            'volatility': {
                'ratio': self.lines.volatility_ratio[0],
                'state': (
                    'increasing' if self.lines.volatility_ratio[0] > 1
                    else 'decreasing'
                ),
                'relative_level': (
                    'high' if self.lines.volatility_ratio[0] > 1.5
                    else 'low' if self.lines.volatility_ratio[0] < 0.5
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
                'confidence': (
                    abs(self.lines.trend_strength[0]) *
                    (1 / self.lines.volatility_ratio[0])
                    if self.lines.volatility_ratio[0] > 0
                    else 0
                )
            },
            'risk': {
                'band_risk': (
                    (self.lines.upper[0] - self.lines.lower[0]) /
                    self.lines.mid[0]
                    if self.lines.mid[0] != 0
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
