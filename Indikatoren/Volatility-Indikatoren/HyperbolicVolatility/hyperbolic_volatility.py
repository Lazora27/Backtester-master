import backtrader as bt
import numpy as np

class HyperbolicVolatility(bt.Indicator):
    """
    Hyperbolic Volatility Indicator
    
    Ein fortgeschrittener Volatilitätsindikator, der hyperbolische
    Funktionen verwendet, um Volatilitätsmuster zu analysieren.
    
    Features:
    - Hyperbolische Volatilitätsberechnung
    - Trendstärkeanalyse
    - Volatilitätsregimeerkennung
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - alpha (0.2): Hyperbolischer Faktor
    - threshold (0.5): Signalschwelle
    """
    
    lines = ('hvi', 'smoothed_hvi',
             'trend_strength', 'volatility_regime',
             'signal')
             
    params = (
        ('period', 14),
        ('alpha', 0.2),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        hvi=dict(color='blue', _name='HVI'),
        smoothed_hvi=dict(color='red', _name='Smoothed HVI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_regime=dict(color='purple', _name='Volatility Regime'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(HyperbolicVolatility, self).__init__()
        
        # Volatilität
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.hvi_history = []
        self.vol_history = []
        
    def hyperbolic_transform(self, x):
        """
        Wendet eine hyperbolische Transformation an.
        """
        return np.tanh(self.p.alpha * x)
        
    def calculate_hvi(self):
        """
        Berechnet den Hyperbolic Volatility Index.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        returns = [
            (self.data.close[-i] - self.data.close[-i-1]) /
            self.data.close[-i-1] if self.data.close[-i-1] != 0 else 0
            for i in range(self.p.period)
            if i < len(self.data) - 1
        ]
        
        # Hyperbolische Transformation
        hyp_returns = [
            self.hyperbolic_transform(r)
            for r in returns
        ]
        
        return np.mean(hyp_returns) if hyp_returns else 0
        
    def calculate_regime(self):
        """
        Bestimmt das Volatilitätsregime.
        """
        if len(self.hvi_history) < self.p.period:
            return 0
            
        mean_hvi = np.mean(self.hvi_history)
        current_hvi = self.lines.hvi[0]
        
        if current_hvi > mean_hvi + self.p.threshold:
            regime = 1  # Hochvolatilitätsregime
        elif current_hvi < mean_hvi - self.p.threshold:
            regime = -1  # Niedrigvolatilitätsregime
        else:
            regime = 0  # Neutrales Regime
            
        return regime
        
    def next(self):
        # HVI berechnen
        self.lines.hvi[0] = self.calculate_hvi()
        self.hvi_history.append(self.lines.hvi[0])
        
        # Geglätteter HVI
        if len(self.hvi_history) >= self.p.period:
            self.lines.smoothed_hvi[0] = np.mean(
                self.hvi_history[-self.p.period:]
            )
        else:
            self.lines.smoothed_hvi[0] = self.lines.hvi[0]
            
        # Volatilitätsregime
        self.lines.volatility_regime[0] = self.calculate_regime()
        
        # Trendstärke
        if len(self.hvi_history) >= 2:
            self.lines.trend_strength[0] = abs(
                self.lines.hvi[0] -
                self.lines.hvi[-1]
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.hvi[0] > self.lines.smoothed_hvi[0] and
                self.lines.volatility_regime[0] > 0
            )
            else -1 if (
                self.lines.hvi[0] < self.lines.smoothed_hvi[0] and
                self.lines.volatility_regime[0] < 0
            )
            else 0
        )
        
        # Volatilitätshistorie aktualisieren
        self.vol_history.append(self.vol[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.hvi_history, self.vol_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volatility': {
                'hvi': self.lines.hvi[0],
                'smoothed': self.lines.smoothed_hvi[0],
                'regime': (
                    'high' if self.lines.volatility_regime[0] > 0
                    else 'low' if self.lines.volatility_regime[0] < 0
                    else 'normal'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'increasing' if self.lines.hvi[0] > self.lines.hvi[-1]
                    else 'decreasing'
                ),
                'persistence': (
                    np.mean([
                        1 if h > self.lines.smoothed_hvi[0] else -1
                        for h in self.hvi_history[-5:]
                    ]) if len(self.hvi_history) >= 5
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
                    self.lines.trend_strength[0] *
                    abs(self.lines.volatility_regime[0])
                )
            },
            'risk': {
                'volatility_risk': abs(self.lines.hvi[0]),
                'trend_risk': (
                    1 - self.lines.trend_strength[0]
                    if self.lines.trend_strength[0] <= 1
                    else 0
                ),
                'regime_risk': abs(self.lines.volatility_regime[0])
            },
            'analysis': {
                'mean_hvi': np.mean(self.hvi_history) if self.hvi_history else 0,
                'std_hvi': np.std(self.hvi_history) if len(self.hvi_history) > 1 else 0,
                'stability': (
                    1 - (np.std(self.hvi_history) / np.mean(self.hvi_history))
                    if len(self.hvi_history) > 1 and np.mean(self.hvi_history) != 0
                    else 0
                )
            }
        }
