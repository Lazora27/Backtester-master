import backtrader as bt
import numpy as np

class RelativeVolatilityIndex(bt.Indicator):
    """
    Relative Volatility Index (RVI)
    
    Ein Volatilitätsindikator, der die relative Stärke der
    Volatilität zwischen Aufwärts- und Abwärtsbewegungen misst.
    
    Features:
    - Relative Volatilitätsanalyse
    - Trendstärkeberechnung
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - smooth_period (10): Glättungsperiode
    - std_dev_period (10): Standardabweichungsperiode
    """
    
    lines = ('rvi', 'smoothed_rvi',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 14),
        ('smooth_period', 10),
        ('std_dev_period', 10)
    )
    
    plotlines = dict(
        rvi=dict(color='blue', _name='RVI'),
        smoothed_rvi=dict(color='red', _name='Smoothed RVI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(RelativeVolatilityIndex, self).__init__()
        
        # Historie
        self.up_vol_history = []
        self.down_vol_history = []
        self.rvi_history = []
        
    def calculate_rvi(self):
        """
        Berechnet den RVI.
        """
        if len(self.up_vol_history) < self.p.period:
            return 50
            
        up_sum = sum(self.up_vol_history[-self.p.period:])
        down_sum = sum(self.down_vol_history[-self.p.period:])
        
        total = up_sum + down_sum
        
        if total == 0:
            return 50
            
        return 100 * (up_sum / total)
        
    def calculate_volatility(self):
        """
        Berechnet die Volatilitätskomponenten.
        """
        if len(self.data) < 2:
            return 0, 0
            
        change = self.data.close[0] - self.data.close[-1]
        std_dev = np.std([
            self.data.close[i] - self.data.close[i-1]
            for i in range(-self.p.std_dev_period+1, 1)
        ])
        
        if change > 0:
            return std_dev, 0
        else:
            return 0, std_dev
            
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.rvi_history) < 2:
            return 0
            
        return (
            self.rvi_history[-1] -
            self.rvi_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.rvi_history) < self.p.period:
            return 1.0
            
        current_vol = np.std(self.rvi_history[-5:])
        historical_vol = np.std(self.rvi_history[-self.p.period:])
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Volatilitätskomponenten
        up_vol, down_vol = self.calculate_volatility()
        
        # Historie aktualisieren
        self.up_vol_history.append(up_vol)
        self.down_vol_history.append(down_vol)
        
        # RVI berechnen
        self.lines.rvi[0] = self.calculate_rvi()
        self.rvi_history.append(self.lines.rvi[0])
        
        # Geglätteter RVI
        if len(self.rvi_history) >= self.p.smooth_period:
            self.lines.smoothed_rvi[0] = np.mean(
                self.rvi_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_rvi[0] = self.lines.rvi[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.rvi[0] > 70 and
            self.lines.trend_strength[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.rvi[0] < 30 and
              self.lines.trend_strength[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period,
            self.p.std_dev_period
        )
        for hist in [self.up_vol_history, self.down_vol_history,
                    self.rvi_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'rvi': {
                'value': self.lines.rvi[0],
                'smoothed': self.lines.smoothed_rvi[0],
                'state': (
                    'overbought' if self.lines.rvi[0] > 70
                    else 'oversold' if self.lines.rvi[0] < 30
                    else 'neutral'
                ),
                'divergence': (
                    self.lines.rvi[0] -
                    self.lines.smoothed_rvi[0]
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
                    (1 - abs(70 - self.lines.rvi[0]) / 70)
                    if self.lines.rvi[0] > 70
                    else abs(self.lines.trend_strength[0]) *
                    (1 - abs(30 - self.lines.rvi[0]) / 30)
                    if self.lines.rvi[0] < 30
                    else 0
                )
            },
            'risk': {
                'rvi_risk': (
                    abs(50 - self.lines.rvi[0]) / 50
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
