import backtrader as bt
import numpy as np

class SharpeRatioIndicator(bt.Indicator):
    """
    Sharpe Ratio Indicator
    
    Ein Volatilitätsindikator, der das Risiko-Rendite-Verhältnis
    basierend auf dem Sharpe Ratio berechnet.
    
    Features:
    - Risikoadjustierte Renditeberechnung
    - Trendstärkeanalyse
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - risk_free_rate (0.0): Risikofreier Zinssatz
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('sharpe', 'smoothed_sharpe',
             'trend_strength', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 20),
        ('risk_free_rate', 0.0),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        sharpe=dict(color='blue', _name='Sharpe Ratio'),
        smoothed_sharpe=dict(color='red', _name='Smoothed Sharpe'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SharpeRatioIndicator, self).__init__()
        
        # Historie
        self.returns_history = []
        self.sharpe_history = []
        
    def calculate_sharpe(self):
        """
        Berechnet den Sharpe Ratio.
        """
        if len(self.returns_history) < self.p.period:
            return 0
            
        returns = np.array(self.returns_history[-self.p.period:])
        
        mean_return = np.mean(returns)
        std_return = np.std(returns)
        
        if std_return == 0:
            return 0
            
        return (
            (mean_return - self.p.risk_free_rate) /
            std_return
        )
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.sharpe_history) < 2:
            return 0
            
        return (
            self.sharpe_history[-1] -
            self.sharpe_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.returns_history) < self.p.period:
            return 1.0
            
        current_vol = np.std(self.returns_history[-5:])
        historical_vol = np.std(self.returns_history[-self.p.period:])
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Rendite berechnen
        if len(self.data) > 1:
            returns = (
                self.data.close[0] - self.data.close[-1]
            ) / self.data.close[-1]
        else:
            returns = 0
            
        # Historie aktualisieren
        self.returns_history.append(returns)
        
        # Sharpe Ratio berechnen
        self.lines.sharpe[0] = self.calculate_sharpe()
        self.sharpe_history.append(self.lines.sharpe[0])
        
        # Geglätteter Sharpe Ratio
        if len(self.sharpe_history) >= self.p.smooth_period:
            self.lines.smoothed_sharpe[0] = np.mean(
                self.sharpe_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_sharpe[0] = self.lines.sharpe[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.sharpe[0] > 1.0 and
            self.lines.trend_strength[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.sharpe[0] < -1.0 and
              self.lines.trend_strength[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(self.p.period, self.p.smooth_period)
        for hist in [self.returns_history, self.sharpe_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'sharpe': {
                'value': self.lines.sharpe[0],
                'smoothed': self.lines.smoothed_sharpe[0],
                'quality': (
                    'excellent' if self.lines.sharpe[0] > 2
                    else 'good' if self.lines.sharpe[0] > 1
                    else 'poor' if self.lines.sharpe[0] < 0
                    else 'fair'
                ),
                'trend': (
                    'improving' if self.lines.trend_strength[0] > 0
                    else 'deteriorating'
                )
            },
            'returns': {
                'current': (
                    self.returns_history[-1]
                    if self.returns_history else 0
                ),
                'mean': (
                    np.mean(self.returns_history[-self.p.period:])
                    if len(self.returns_history) >= self.p.period
                    else 0
                ),
                'volatility': (
                    np.std(self.returns_history[-self.p.period:])
                    if len(self.returns_history) >= self.p.period
                    else 0
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
                    abs(self.lines.sharpe[0]) *
                    abs(self.lines.trend_strength[0])
                )
            },
            'risk': {
                'sharpe_risk': (
                    1 / (1 + abs(self.lines.sharpe[0]))
                    if self.lines.sharpe[0] != 0
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
