import backtrader as bt
import numpy as np

class ShortTermVolatilityIndex(bt.Indicator):
    """
    Short-Term Volatility Index (STVI)
    
    Ein Volatilitätsindikator, der kurzfristige Volatilitätsmuster
    und deren Auswirkungen auf den Preis analysiert.
    
    Features:
    - Kurzfristige Volatilitätsanalyse
    - Trendstärkeberechnung
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - short_period (5): Kurzfristiger Analysezeitraum
    - long_period (20): Langfristiger Analysezeitraum
    - smooth_period (3): Glättungsperiode
    """
    
    lines = ('stvi', 'smoothed_stvi',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('short_period', 5),
        ('long_period', 20),
        ('smooth_period', 3)
    )
    
    plotlines = dict(
        stvi=dict(color='blue', _name='STVI'),
        smoothed_stvi=dict(color='red', _name='Smoothed STVI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ShortTermVolatilityIndex, self).__init__()
        
        # Historie
        self.vol_history = []
        self.stvi_history = []
        
    def calculate_stvi(self):
        """
        Berechnet den STVI.
        """
        if len(self.vol_history) < self.p.long_period:
            return 0
            
        short_vol = np.std(self.vol_history[-self.p.short_period:])
        long_vol = np.std(self.vol_history[-self.p.long_period:])
        
        if long_vol == 0:
            return 0
            
        return (short_vol / long_vol - 1) * 100
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.stvi_history) < 2:
            return 0
            
        return (
            self.stvi_history[-1] -
            self.stvi_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.vol_history) < self.p.long_period:
            return 1.0
            
        current_vol = np.std(self.vol_history[-self.p.short_period:])
        historical_vol = np.std(self.vol_history[-self.p.long_period:])
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Volatilität berechnen
        if len(self.data) > 1:
            volatility = abs(
                self.data.close[0] - self.data.close[-1]
            ) / self.data.close[-1]
        else:
            volatility = 0
            
        # Historie aktualisieren
        self.vol_history.append(volatility)
        
        # STVI berechnen
        self.lines.stvi[0] = self.calculate_stvi()
        self.stvi_history.append(self.lines.stvi[0])
        
        # Geglätteter STVI
        if len(self.stvi_history) >= self.p.smooth_period:
            self.lines.smoothed_stvi[0] = np.mean(
                self.stvi_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_stvi[0] = self.lines.stvi[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.stvi[0] < -20 and
            self.lines.trend_strength[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.stvi[0] > 20 and
              self.lines.trend_strength[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.long_period,
            self.p.short_period,
            self.p.smooth_period
        )
        for hist in [self.vol_history, self.stvi_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'stvi': {
                'value': self.lines.stvi[0],
                'smoothed': self.lines.smoothed_stvi[0],
                'state': (
                    'high' if self.lines.stvi[0] > 20
                    else 'low' if self.lines.stvi[0] < -20
                    else 'normal'
                ),
                'divergence': (
                    self.lines.stvi[0] -
                    self.lines.smoothed_stvi[0]
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
                'reliability': (
                    abs(self.lines.trend_strength[0]) *
                    (1 - abs(self.lines.stvi[0]) / 100)
                    if abs(self.lines.stvi[0]) <= 100
                    else 0
                )
            },
            'risk': {
                'stvi_risk': (
                    abs(self.lines.stvi[0]) / 100
                    if abs(self.lines.stvi[0]) <= 100
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
