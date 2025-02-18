import backtrader as bt
import numpy as np

class CenterOfGravity(bt.Indicator):
    """
    Center of Gravity (COG) Indicator
    
    Ein Volatilitätsindikator, der den Schwerpunkt der
    Preisbewegungen und deren Volatilität analysiert.
    
    Features:
    - Schwerpunktberechnung
    - Volatilitätsgewichtung
    - Trendstärkeanalyse
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - vol_factor (0.5): Volatilitätsgewichtung
    - threshold (0.3): Signalschwelle
    """
    
    lines = ('cog', 'vol_weighted_cog',
             'trend_strength', 'momentum',
             'signal')
             
    params = (
        ('period', 14),
        ('vol_factor', 0.5),
        ('threshold', 0.3)
    )
    
    plotlines = dict(
        cog=dict(color='blue', _name='COG'),
        vol_weighted_cog=dict(color='red', _name='Vol Weighted COG'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        momentum=dict(color='purple', _name='Momentum'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(CenterOfGravity, self).__init__()
        
        # Volatilität
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.price_history = []
        self.vol_history = []
        self.cog_history = []
        
    def calculate_cog(self):
        """
        Berechnet den Center of Gravity.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        weights = np.arange(1, len(self.price_history[-self.p.period:]) + 1)
        prices = np.array(self.price_history[-self.p.period:])
        
        numerator = np.sum(weights * prices)
        denominator = np.sum(weights)
        
        return numerator / denominator if denominator != 0 else 0
        
    def calculate_vol_weighted_cog(self):
        """
        Berechnet den volatilitätsgewichteten COG.
        """
        if len(self.vol_history) < self.p.period:
            return 0
            
        weights = np.array(self.vol_history[-self.p.period:])
        prices = np.array(self.price_history[-self.p.period:])
        
        numerator = np.sum(weights * prices)
        denominator = np.sum(weights)
        
        return numerator / denominator if denominator != 0 else 0
        
    def calculate_momentum(self):
        """
        Berechnet das Momentum.
        """
        if len(self.cog_history) < 2:
            return 0
            
        return (
            self.lines.cog[0] -
            self.lines.cog[-1]
        )
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.vol_history.append(self.vol[0])
        
        # COG berechnen
        self.lines.cog[0] = self.calculate_cog()
        self.cog_history.append(self.lines.cog[0])
        
        # Volatilitätsgewichteter COG
        self.lines.vol_weighted_cog[0] = self.calculate_vol_weighted_cog()
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Trendstärke
        if len(self.cog_history) >= self.p.period:
            self.lines.trend_strength[0] = abs(
                self.lines.cog[0] -
                np.mean(self.cog_history[-self.p.period:])
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.momentum[0] > self.p.threshold and
                self.lines.trend_strength[0] > self.p.threshold
            )
            else -1 if (
                self.lines.momentum[0] < -self.p.threshold and
                self.lines.trend_strength[0] > self.p.threshold
            )
            else 0
        )
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.price_history, self.vol_history,
                    self.cog_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cog': {
                'value': self.lines.cog[0],
                'vol_weighted': self.lines.vol_weighted_cog[0],
                'momentum': self.lines.momentum[0],
                'trend': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'momentum': abs(self.lines.momentum[0]),
                'persistence': (
                    np.mean([
                        1 if m > 0 else -1
                        for m in self.cog_history[-5:]
                    ]) if len(self.cog_history) >= 5
                    else 0
                )
            },
            'volatility': {
                'current': self.vol[0],
                'impact': (
                    abs(self.lines.vol_weighted_cog[0] -
                        self.lines.cog[0])
                ),
                'trend': (
                    'increasing' if self.vol[0] > self.vol[-1]
                    else 'decreasing'
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
                    self.lines.trend_strength[0] *
                    abs(self.lines.momentum[0])
                )
            },
            'risk': {
                'trend_risk': (
                    1 - self.lines.trend_strength[0]
                    if self.lines.trend_strength[0] <= 1
                    else 0
                ),
                'momentum_risk': abs(self.lines.momentum[0]),
                'volatility_risk': (
                    self.vol[0] / np.mean(self.vol_history)
                    if len(self.vol_history) > 0 and
                    np.mean(self.vol_history) > 0
                    else 1.0
                )
            }
        }
