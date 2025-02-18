import backtrader as bt
import numpy as np
from scipy import stats

class ProjectionOscillator(bt.Indicator):
    """
    Projection Oscillator (PO)
    
    Ein Volatilitätsindikator, der Preisprojektionen und
    Volatilitätsmuster für Trendvorhersagen nutzt.
    
    Features:
    - Preisprojektion
    - Volatilitätsanalyse
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - projection_period (5): Projektionszeitraum
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('po', 'smoothed_po',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('projection_period', 5),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        po=dict(color='blue', _name='PO'),
        smoothed_po=dict(color='red', _name='Smoothed PO'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ProjectionOscillator, self).__init__()
        
        # Historie
        self.price_history = []
        self.po_history = []
        self.projection_history = []
        
    def calculate_projection(self):
        """
        Berechnet die Preisprojektion.
        """
        if len(self.price_history) < self.p.period:
            return 0, 0
            
        x = np.arange(len(self.price_history[-self.p.period:]))
        y = np.array(self.price_history[-self.p.period:])
        
        # Lineare Regression
        slope, intercept, r_value, _, _ = stats.linregress(x, y)
        
        # Projektion
        proj_x = self.p.period + self.p.projection_period
        projection = slope * proj_x + intercept
        
        return projection, r_value ** 2
        
    def calculate_po(self, projection, r_squared):
        """
        Berechnet den Projection Oscillator.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        current_price = self.price_history[-1]
        
        if current_price == 0:
            return 0
            
        # Oszillator berechnen
        po = (
            (projection - current_price) /
            current_price * 100
        )
        
        # Mit R² gewichten
        return po * r_squared
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.po_history) < 2:
            return 0
            
        return (
            self.po_history[-1] -
            self.po_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.price_history) < self.p.period:
            return 1.0
            
        current_vol = np.std(self.price_history[-5:])
        historical_vol = np.std(
            self.price_history[-self.p.period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        
        # Projektion berechnen
        projection, r_squared = self.calculate_projection()
        self.projection_history.append(projection)
        
        # PO berechnen
        self.lines.po[0] = self.calculate_po(
            projection, r_squared
        )
        self.po_history.append(self.lines.po[0])
        
        # Geglätteter PO
        if len(self.po_history) >= self.p.smooth_period:
            self.lines.smoothed_po[0] = np.mean(
                self.po_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_po[0] = self.lines.po[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.po[0] > 0 and
            self.lines.trend_strength[0] > 0 and
            r_squared > 0.7):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.po[0] < 0 and
              self.lines.trend_strength[0] < 0 and
              r_squared > 0.7):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period + self.p.projection_period,
            self.p.smooth_period
        )
        for hist in [self.price_history, self.po_history,
                    self.projection_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'po': {
                'value': self.lines.po[0],
                'smoothed': self.lines.smoothed_po[0],
                'state': (
                    'overbought' if self.lines.po[0] > 20
                    else 'oversold' if self.lines.po[0] < -20
                    else 'neutral'
                ),
                'trend': (
                    'up' if self.lines.po[0] > 0
                    else 'down'
                )
            },
            'projection': {
                'value': (
                    self.projection_history[-1]
                    if self.projection_history else 0
                ),
                'accuracy': (
                    abs(
                        self.projection_history[-2] -
                        self.price_history[-1]
                    ) / self.price_history[-1]
                    if len(self.projection_history) > 1 and
                       self.price_history[-1] != 0
                    else 1
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
                    (1 - abs(self.lines.po[0]) / 100)
                    if abs(self.lines.po[0]) <= 100
                    else 0
                )
            },
            'risk': {
                'po_risk': (
                    abs(self.lines.po[0]) / 100
                    if abs(self.lines.po[0]) <= 100
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
