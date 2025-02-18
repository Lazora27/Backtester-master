import backtrader as bt
import numpy as np

class TrueRangeIndicator(bt.Indicator):
    """
    True Range Indicator (TRI)
    
    Ein Volatilitätsindikator, der den True Range und seine
    Ableitungen für die Volatilitätsanalyse verwendet.
    
    Features:
    - True Range Berechnung
    - Trendstärkeanalyse
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - smooth_period (10): Glättungsperiode
    - std_period (20): Standardabweichungsperiode
    """
    
    lines = ('tr', 'smoothed_tr',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 14),
        ('smooth_period', 10),
        ('std_period', 20)
    )
    
    plotlines = dict(
        tr=dict(color='blue', _name='True Range'),
        smoothed_tr=dict(color='red', _name='Smoothed TR'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TrueRangeIndicator, self).__init__()
        
        # Historie
        self.tr_history = []
        self.normalized_tr_history = []
        
    def calculate_tr(self):
        """
        Berechnet den True Range.
        """
        if len(self.data) < 2:
            return self.data.high[0] - self.data.low[0]
            
        return max(
            self.data.high[0] - self.data.low[0],
            abs(self.data.high[0] - self.data.close[-1]),
            abs(self.data.low[0] - self.data.close[-1])
        )
        
    def normalize_tr(self, tr):
        """
        Normalisiert den True Range.
        """
        if len(self.data) < self.p.period:
            return tr
            
        avg_price = np.mean([
            self.data.close[-i]
            for i in range(self.p.period)
        ])
        
        return tr / avg_price if avg_price != 0 else tr
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.normalized_tr_history) < 2:
            return 0
            
        return (
            self.normalized_tr_history[-1] -
            self.normalized_tr_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.tr_history) < self.p.std_period:
            return 1.0
            
        current_vol = np.std(self.tr_history[-5:])
        historical_vol = np.std(
            self.tr_history[-self.p.std_period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # True Range berechnen
        tr = self.calculate_tr()
        self.tr_history.append(tr)
        self.lines.tr[0] = tr
        
        # Normalisierter True Range
        normalized_tr = self.normalize_tr(tr)
        self.normalized_tr_history.append(normalized_tr)
        
        # Geglätteter True Range
        if len(self.tr_history) >= self.p.smooth_period:
            self.lines.smoothed_tr[0] = np.mean(
                self.tr_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_tr[0] = tr
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if len(self.tr_history) >= self.p.period:
            tr_mean = np.mean(
                self.tr_history[-self.p.period:]
            )
            tr_std = np.std(
                self.tr_history[-self.p.period:]
            )
            
            if (tr < tr_mean - tr_std and
                self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (tr > tr_mean + tr_std and
                  self.lines.trend_strength[0] < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period,
            self.p.std_period
        )
        for hist in [self.tr_history,
                    self.normalized_tr_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'true_range': {
                'value': self.lines.tr[0],
                'smoothed': self.lines.smoothed_tr[0],
                'normalized': (
                    self.normalized_tr_history[-1]
                    if self.normalized_tr_history
                    else 0
                ),
                'trend': (
                    'increasing'
                    if self.lines.tr[0] >
                       self.lines.smoothed_tr[0]
                    else 'decreasing'
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
                    (1 - self.lines.volatility_ratio[0])
                    if self.lines.volatility_ratio[0] <= 1
                    else 0
                )
            },
            'risk': {
                'tr_risk': (
                    self.lines.tr[0] /
                    self.lines.smoothed_tr[0]
                    if self.lines.smoothed_tr[0] != 0
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
