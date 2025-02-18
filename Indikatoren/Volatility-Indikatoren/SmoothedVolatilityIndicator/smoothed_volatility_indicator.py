import backtrader as bt
import numpy as np

class SmoothedVolatilityIndicator(bt.Indicator):
    """
    Smoothed Volatility Indicator (SVI)
    
    Ein Volatilitätsindikator, der mehrfache Glättungsmethoden
    verwendet, um Rauschen zu reduzieren und klare Signale zu generieren.
    
    Features:
    - Mehrfache Glättung
    - Trendstärkeberechnung
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - alpha (0.2): Exponentieller Glättungsfaktor
    - smooth_period (10): Zusätzliche Glättungsperiode
    """
    
    lines = ('svi', 'smoothed_svi',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('alpha', 0.2),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        svi=dict(color='blue', _name='SVI'),
        smoothed_svi=dict(color='red', _name='Smoothed SVI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SmoothedVolatilityIndicator, self).__init__()
        
        # Historie
        self.vol_history = []
        self.svi_history = []
        self.ema_history = []
        
    def calculate_volatility(self):
        """
        Berechnet die Volatilität.
        """
        if len(self.data) < 2:
            return 0
            
        return abs(
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1]
        
    def calculate_ema(self, value):
        """
        Berechnet den exponentiellen gleitenden Durchschnitt.
        """
        if not self.ema_history:
            return value
            
        return (
            self.p.alpha * value +
            (1 - self.p.alpha) * self.ema_history[-1]
        )
        
    def calculate_svi(self):
        """
        Berechnet den geglätteten Volatilitätsindikator.
        """
        if len(self.vol_history) < self.p.period:
            return 0
            
        # Erste Glättung (EMA)
        ema = self.calculate_ema(self.vol_history[-1])
        self.ema_history.append(ema)
        
        # Zweite Glättung (SMA über EMA)
        if len(self.ema_history) >= self.p.smooth_period:
            return np.mean(self.ema_history[-self.p.smooth_period:])
        return ema
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.svi_history) < 2:
            return 0
            
        return (
            self.svi_history[-1] -
            self.svi_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.svi_history) < self.p.period:
            return 1.0
            
        current_vol = np.mean(self.svi_history[-5:])
        historical_vol = np.mean(
            self.svi_history[-self.p.period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Volatilität berechnen
        volatility = self.calculate_volatility()
        self.vol_history.append(volatility)
        
        # SVI berechnen
        self.lines.svi[0] = self.calculate_svi()
        self.svi_history.append(self.lines.svi[0])
        
        # Geglätteter SVI
        if len(self.svi_history) >= self.p.smooth_period:
            self.lines.smoothed_svi[0] = np.mean(
                self.svi_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_svi[0] = self.lines.svi[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.svi[0] < self.lines.smoothed_svi[0] and
            self.lines.trend_strength[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.svi[0] > self.lines.smoothed_svi[0] and
              self.lines.trend_strength[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.vol_history, self.svi_history,
                    self.ema_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'svi': {
                'value': self.lines.svi[0],
                'smoothed': self.lines.smoothed_svi[0],
                'trend': (
                    'increasing'
                    if self.lines.svi[0] >
                       self.lines.smoothed_svi[0]
                    else 'decreasing'
                ),
                'divergence': (
                    self.lines.svi[0] -
                    self.lines.smoothed_svi[0]
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
                    (1 - abs(
                        self.lines.svi[0] -
                        self.lines.smoothed_svi[0]
                    ) / self.lines.svi[0])
                    if self.lines.svi[0] != 0
                    else 0
                )
            },
            'risk': {
                'svi_risk': (
                    self.lines.svi[0] /
                    self.lines.smoothed_svi[0]
                    if self.lines.smoothed_svi[0] != 0
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
