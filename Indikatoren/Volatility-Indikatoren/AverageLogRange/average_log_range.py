import backtrader as bt
import numpy as np

class AverageLogRange(bt.Indicator):
    """
    Average Log Range (ALR) Indicator
    
    Ein Volatilitätsindikator, der den logarithmischen Bereich
    der Preisbewegungen analysiert.
    
    Features:
    - Logarithmische Bereichsberechnung
    - Gleitende Mittelwertanalyse
    - Trendstärkebestimmung
    - Volatilitätsnormalisierung
    
    Parameter:
    - period (20): Analysezeitraum
    - smooth_period (10): Glättungsperiode
    - vol_threshold (1.5): Volatilitätsschwelle
    """
    
    lines = ('alr', 'smoothed_alr',
             'normalized_alr', 'trend_strength',
             'volatility_signal')
             
    params = (
        ('period', 20),
        ('smooth_period', 10),
        ('vol_threshold', 1.5)
    )
    
    plotlines = dict(
        alr=dict(color='blue', _name='ALR'),
        smoothed_alr=dict(color='red', _name='Smoothed ALR'),
        normalized_alr=dict(color='green', _name='Normalized ALR'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        volatility_signal=dict(color='orange', _name='Volatility Signal')
    )
    
    def __init__(self):
        super(AverageLogRange, self).__init__()
        
        # Historie
        self.log_range_history = []
        self.alr_history = []
        
    def calculate_log_range(self):
        """
        Berechnet den logarithmischen Bereich.
        """
        if self.data.high[0] <= 0 or self.data.low[0] <= 0:
            return 0
            
        return np.log(self.data.high[0]) - np.log(self.data.low[0])
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.alr_history) < self.p.period:
            return 0
            
        recent_alr = np.mean(self.alr_history[-5:])
        overall_alr = np.mean(self.alr_history)
        
        return (recent_alr - overall_alr) / overall_alr if overall_alr != 0 else 0
        
    def next(self):
        # Log Range berechnen
        log_range = self.calculate_log_range()
        self.log_range_history.append(log_range)
        
        # ALR berechnen
        if len(self.log_range_history) >= self.p.period:
            self.lines.alr[0] = np.mean(
                self.log_range_history[-self.p.period:]
            )
        else:
            self.lines.alr[0] = log_range
            
        self.alr_history.append(self.lines.alr[0])
        
        # Geglätteter ALR
        if len(self.alr_history) >= self.p.smooth_period:
            self.lines.smoothed_alr[0] = np.mean(
                self.alr_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_alr[0] = self.lines.alr[0]
            
        # Normalisierter ALR
        if len(self.alr_history) >= self.p.period:
            mean_alr = np.mean(self.alr_history[-self.p.period:])
            std_alr = np.std(self.alr_history[-self.p.period:])
            
            self.lines.normalized_alr[0] = (
                (self.lines.alr[0] - mean_alr) / std_alr
                if std_alr != 0 else 0
            )
        else:
            self.lines.normalized_alr[0] = 0
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätssignal
        self.lines.volatility_signal[0] = (
            1 if self.lines.normalized_alr[0] > self.p.vol_threshold
            else -1 if self.lines.normalized_alr[0] < -self.p.vol_threshold
            else 0
        )
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.smooth_period)
        for hist in [self.log_range_history, self.alr_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'alr': {
                'current': self.lines.alr[0],
                'smoothed': self.lines.smoothed_alr[0],
                'normalized': self.lines.normalized_alr[0],
                'trend': (
                    'increasing' if self.lines.trend_strength[0] > 0
                    else 'decreasing'
                )
            },
            'volatility': {
                'signal': (
                    'high' if self.lines.volatility_signal[0] > 0
                    else 'low' if self.lines.volatility_signal[0] < 0
                    else 'normal'
                ),
                'strength': abs(self.lines.normalized_alr[0]),
                'trend_impact': self.lines.trend_strength[0]
            },
            'analysis': {
                'mean': np.mean(self.alr_history) if self.alr_history else 0,
                'std': np.std(self.alr_history) if len(self.alr_history) > 1 else 0,
                'stability': (
                    1 - abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 0
                )
            },
            'risk': {
                'current': abs(self.lines.normalized_alr[0]),
                'trend_risk': abs(self.lines.trend_strength[0]),
                'volatility_risk': (
                    np.std(self.alr_history) / np.mean(self.alr_history)
                    if len(self.alr_history) > 1 and np.mean(self.alr_history) > 0
                    else 0
                )
            }
        }
