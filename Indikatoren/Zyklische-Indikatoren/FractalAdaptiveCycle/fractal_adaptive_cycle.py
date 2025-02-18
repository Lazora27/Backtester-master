import backtrader as bt
import numpy as np

class FractalAdaptiveCycle(bt.Indicator):
    """
    Fractal Adaptive Cycle Indicator
    
    Ein adaptiver Zyklusindikator, der fraktale Dimensionen
    verwendet, um Marktzyklen zu identifizieren und zu analysieren.
    
    Features:
    - Fraktale Dimensionsanalyse
    - Adaptive Zykluserkennung
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (40): Analysezeitraum
    - fractal_dimension (1.5): Fraktale Dimension
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('cycle', 'fractal_dim',
             'cycle_quality', 'adaptive_band',
             'signal')
             
    params = (
        ('period', 40),
        ('fractal_dimension', 1.5),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        cycle=dict(color='blue', _name='Cycle'),
        fractal_dim=dict(color='red', _name='Fractal Dimension'),
        cycle_quality=dict(color='green', _name='Cycle Quality'),
        adaptive_band=dict(color='purple', _name='Adaptive Band'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(FractalAdaptiveCycle, self).__init__()
        
        # Historie
        self.price_history = []
        self.cycle_history = []
        
    def calculate_fractal_dimension(self):
        """
        Berechnet die fraktale Dimension der Preisreihe.
        """
        if len(self.price_history) < self.p.period:
            return self.p.fractal_dimension
            
        # Hurst-Exponent Schätzung
        prices = np.array(
            self.price_history[-self.p.period:]
        )
        n = len(prices)
        
        # Berechne Log Returns
        log_returns = np.diff(np.log(prices))
        
        # R/S Analyse
        cumsum = np.cumsum(log_returns - np.mean(log_returns))
        r = np.max(cumsum) - np.min(cumsum)
        s = np.std(log_returns)
        
        if s == 0:
            return self.p.fractal_dimension
            
        rs = r/s
        hurst = np.log(rs) / np.log(n)
        
        # Fraktale Dimension
        return 2 - hurst
        
    def calculate_adaptive_cycle(self):
        """
        Berechnet den adaptiven Zyklus.
        """
        if len(self.price_history) < 4:
            return 0
            
        # Ehlers' Adaptive Cycle
        price = self.price_history[-1]
        price1 = self.price_history[-2]
        price2 = self.price_history[-3]
        
        fractal_dim = self.calculate_fractal_dimension()
        alpha = np.power(0.5, fractal_dim)
        
        cycle = (
            (1 - alpha) * price +
            alpha * (2 * price1 - price2)
        )
        
        return cycle
        
    def calculate_cycle_quality(self):
        """
        Berechnet die Zyklusqualität.
        """
        if len(self.cycle_history) < self.p.smooth_period:
            return 0
            
        cycles = np.array(
            self.cycle_history[-self.p.smooth_period:]
        )
        
        # Autokorrelation
        corr = np.correlate(cycles, cycles, mode='full')
        corr = corr[len(corr)//2:]
        
        if len(corr) > 1:
            return corr[1] / corr[0]
        return 0
        
    def calculate_adaptive_band(self):
        """
        Berechnet das adaptive Band.
        """
        if len(self.cycle_history) < self.p.smooth_period:
            return 0
            
        cycles = np.array(
            self.cycle_history[-self.p.smooth_period:]
        )
        
        return np.std(cycles) * 2
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Fraktale Dimension
        fractal_dim = self.calculate_fractal_dimension()
        
        # Adaptiver Zyklus
        cycle = self.calculate_adaptive_cycle()
        self.cycle_history.append(cycle)
        
        # Linien aktualisieren
        self.lines.cycle[0] = cycle
        self.lines.fractal_dim[0] = fractal_dim
        self.lines.cycle_quality[0] = self.calculate_cycle_quality()
        self.lines.adaptive_band[0] = self.calculate_adaptive_band()
        
        # Signal
        if len(self.cycle_history) >= 2:
            if (cycle > self.cycle_history[-2] and
                self.lines.cycle_quality[0] > 0.7):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (cycle < self.cycle_history[-2] and
                  self.lines.cycle_quality[0] > 0.7):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.cycle_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'value': self.lines.cycle[0],
                'quality': self.lines.cycle_quality[0],
                'band': self.lines.adaptive_band[0],
                'fractal_dimension': self.lines.fractal_dim[0]
            },
            'cycle_state': {
                'strength': (
                    abs(self.lines.cycle[0])
                    if abs(self.lines.cycle[0]) <= 1
                    else 1
                ),
                'stability': (
                    'stable'
                    if self.lines.cycle_quality[0] > 0.7
                    else 'unstable'
                ),
                'complexity': (
                    'high'
                    if self.lines.fractal_dim[0] > 1.7
                    else 'low'
                )
            },
            'market_structure': {
                'fractal_state': (
                    'trending'
                    if self.lines.fractal_dim[0] < 1.5
                    else 'cyclic'
                    if self.lines.fractal_dim[0] < 1.8
                    else 'chaotic'
                ),
                'cycle_dominance': (
                    'strong'
                    if self.lines.cycle_quality[0] > 0.8
                    else 'weak'
                ),
                'adaptivity': (
                    'high'
                    if self.lines.adaptive_band[0] >
                       0.01 * self.data.close[0]
                    else 'low'
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
                    self.lines.cycle_quality[0] *
                    (2 - self.lines.fractal_dim[0])
                )
            },
            'trading_conditions': {
                'market_state': (
                    'favorable'
                    if (self.lines.cycle_quality[0] > 0.7 and
                        self.lines.fractal_dim[0] < 1.6)
                    else 'unfavorable'
                ),
                'risk_level': (
                    'high'
                    if self.lines.fractal_dim[0] > 1.8
                    else 'medium'
                    if self.lines.fractal_dim[0] > 1.5
                    else 'low'
                ),
                'opportunity_quality': (
                    'excellent'
                    if (self.lines.cycle_quality[0] > 0.8 and
                        self.lines.fractal_dim[0] < 1.5)
                    else 'poor'
                )
            }
        }
