import backtrader as bt
import numpy as np

class LaggingVolatilityIndex(bt.Indicator):
    """
    Lagging Volatility Index (LVI)
    
    Ein Volatilitätsindikator, der verzögerte Volatilitätsmuster
    analysiert und deren Auswirkungen auf zukünftige Preisbewegungen
    untersucht.
    
    Features:
    - Verzögerte Volatilitätsanalyse
    - Trendstärkeberechnung
    - Volatilitätsregimeerkennung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - lag_period (10): Verzögerungsperiode
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('lvi', 'smoothed_lvi',
             'trend_strength', 'volatility_regime',
             'signal')
             
    params = (
        ('period', 20),
        ('lag_period', 10),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        lvi=dict(color='blue', _name='LVI'),
        smoothed_lvi=dict(color='red', _name='Smoothed LVI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_regime=dict(color='purple', _name='Volatility Regime'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(LaggingVolatilityIndex, self).__init__()
        
        # Volatilität
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.vol_history = []
        self.lvi_history = []
        self.price_history = []
        
    def calculate_lvi(self):
        """
        Berechnet den Lagging Volatility Index.
        """
        if len(self.vol_history) < self.p.lag_period:
            return 0
            
        # Aktuelle Volatilität
        current_vol = self.vol[0]
        
        # Verzögerte Volatilität
        lagged_vol = self.vol_history[-self.p.lag_period]
        
        # LVI berechnen
        if lagged_vol != 0:
            return (current_vol - lagged_vol) / lagged_vol
        return 0
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderungen
        returns = [
            (self.price_history[i] - self.price_history[i-1]) /
            self.price_history[i-1] if self.price_history[i-1] != 0 else 0
            for i in range(1, len(self.price_history))
        ]
        
        # Trendstärke
        return np.mean(returns) if returns else 0
        
    def calculate_regime(self):
        """
        Bestimmt das Volatilitätsregime.
        """
        if len(self.lvi_history) < self.p.period:
            return 0
            
        mean_lvi = np.mean(self.lvi_history)
        std_lvi = np.std(self.lvi_history)
        
        if std_lvi == 0:
            return 0
            
        z_score = (self.lines.lvi[0] - mean_lvi) / std_lvi
        
        if z_score > 1:
            regime = 1  # Steigende Volatilität
        elif z_score < -1:
            regime = -1  # Fallende Volatilität
        else:
            regime = 0  # Stabile Volatilität
            
        return regime
        
    def next(self):
        # Historie aktualisieren
        self.vol_history.append(self.vol[0])
        self.price_history.append(self.data.close[0])
        
        # LVI berechnen
        self.lines.lvi[0] = self.calculate_lvi()
        self.lvi_history.append(self.lines.lvi[0])
        
        # Geglätteter LVI
        if len(self.lvi_history) >= self.p.smooth_period:
            self.lines.smoothed_lvi[0] = np.mean(
                self.lvi_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_lvi[0] = self.lines.lvi[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsregime
        self.lines.volatility_regime[0] = self.calculate_regime()
        
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.lvi[0] < 0 and
                self.lines.trend_strength[0] > 0 and
                self.lines.volatility_regime[0] < 0
            )
            else -1 if (
                self.lines.lvi[0] > 0 and
                self.lines.trend_strength[0] < 0 and
                self.lines.volatility_regime[0] > 0
            )
            else 0
        )
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.lag_period,
            self.p.smooth_period
        )
        for hist in [self.vol_history, self.lvi_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volatility': {
                'lvi': self.lines.lvi[0],
                'smoothed': self.lines.smoothed_lvi[0],
                'regime': (
                    'increasing' if self.lines.volatility_regime[0] > 0
                    else 'decreasing' if self.lines.volatility_regime[0] < 0
                    else 'stable'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    1 - abs(self.lines.lvi[0])
                    if abs(self.lines.lvi[0]) <= 1
                    else 0
                )
            },
            'lag': {
                'effect': (
                    'leading' if self.lines.lvi[0] > self.lines.smoothed_lvi[0]
                    else 'lagging'
                ),
                'magnitude': abs(
                    self.lines.lvi[0] - self.lines.smoothed_lvi[0]
                ),
                'persistence': (
                    np.mean([
                        1 if l > self.lines.smoothed_lvi[0] else -1
                        for l in self.lvi_history[-5:]
                    ]) if len(self.lvi_history) >= 5
                    else 0
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
                    (1 - abs(self.lines.lvi[0]))
                    if abs(self.lines.lvi[0]) <= 1
                    else 0
                )
            },
            'risk': {
                'volatility_risk': abs(self.lines.lvi[0]),
                'trend_risk': (
                    1 - abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 0
                ),
                'lag_risk': abs(
                    self.lines.lvi[0] - self.lines.smoothed_lvi[0]
                )
            }
        }
